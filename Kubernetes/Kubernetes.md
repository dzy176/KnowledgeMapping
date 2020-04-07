# 微服务治理：Kubernetes + Istio（一）

### 简介

​		本次分享主要介绍K8S基础概念以及系统架构，结合具体线上实践，了解K8S最基本的服务发布与管理流程。



### 架构概览

![1585843725969](images\1585843725969.png)

**两类角色：**

集群中，master节点与worker节点一般都是多节点的

- Master节点：管理调度集群资源

  - 根据所辖worker节点空闲状况，进行资源分配（POD具体部署到哪个节点）
  - 声明式指令保证整个集群状态处于理想状态，有自愈的能力

- Worker节点：资源的提供者

  - 每个节点提供的资源单位是POD

  - POD中运行的应用容器Containers（一个或多个）




### 基础概念

- **Namespace**
  
  - 逻辑分组，表征资源的所属，为集群提供了租户级别的隔离
- 通常情况下会依据不同的项目组，不同的开发环境（线上|测试）划分不同的Namespace
  
- **POD**

  <img src="images\1585843632389.png" alt="1585843632389" style="zoom:80%;" />

  - 由一个Pause容器和若干个关联密切业务容器构成

    - Pause容器作用： 网络和数据卷初始化 

  - POD中的容器共享网络栈以及存储卷

    - **共享网络：**container相互之间访问通过localhost方式

      <img src="images\a.jpg" style="zoom:25%;" /><img src="images\b.jpg" style="zoom:25%;" />

      ​                            普通docker方式                                                     POD方式

      - 传统的两个docker容器分别被分配了veth0与veth1两个虚拟网卡，ip分别为0.2， 0.3，两个容器可以通过网桥docker0进行通信，但必须知道对方的ip地址。docker的ip是动态分配的，因此给两个服务之间访问带来障碍
      - 在一个POD中的两台Docker容器通过相关配置（pause命令），共享虚拟网卡veth0，因此可以通过localhost方式进行通信，因此pod中的应用必须协调端口占用 

    - **存储卷：**

      - 实现同一个pod下多个容器共享文件系统
      - 典型的有filebeat日志采集系统

  - 为什么不直接管理每一个容器，而是抽象出了POD的概念？
    - POD中的业务容器共享Pause容器的IP和挂载的Volume，简化业务容器之间通信与交互
    
    - 通过进程间通信和文件共享这种简单高效的方式组合完成服务。 
    
      

**ReplicSet** 副本集

- 定义了对POD副本数的期望值（desired  state)，相当于状态机

- 控制POD中扩缩容

- 控制POD中容器的升级与回滚

  

**Deployment**

- 表征用户对k8s集群的一次更新操作
  - 滚动升级和回滚应用
  - 扩容和缩容
- 生成新ReplicaSet进行POD的管理，旧的RS控制旧版本POD不断减少
- 动态展示部署的中间状态（POD创建 | 调度 | 绑定节点 | 启动容器等）

**Service**

- 主要用于解决服务发现这个棘手的问题，为**集群内**客户端访问**集群内**的POD提供的负载均衡

  ![1585843695469](images\1585843695469.png)

  - 分配虚拟ClusterIP，用作负载均衡器
  - clusterIP做DNS域名映射解决服务发现问题



**Volume**

- 一个POD中声明的存储卷（volume）:

  - 可以是本地存储，worker节点上目录

    - 可以手动指定具体使用HOST节点已有具体目录
    - 可以让K8S帮助生成一个临时目录

  - 可以是外部存储，诸如各个云厂商各自的云硬盘

  - 可以是分布式存储系统，ceph，GlusterFS等

  本质上可以看作一个目录，被mount到POD上可被该pod下的所有容器共享，每个容器可以指定各自的mount路径



### 核心组件：

![1585843859599](images\1585843859599.png)

- **ETCD**
  -  保存集群网络配置
  - 保存集群对象的状态信息 
- **API Server**
  - 为k8s各类资源的操作提供了入口
  - 是各个子组件通信与交互的枢纽
  - 唯一可直接操作底层数据库ETCD
- **Scheduler**
  - 检索符合条件Node，调度POD部署到合适的Woker Node
- **Controller Manager**
  - 管理集群内的NODE，POD，Namespace，Quota等
  - 通过APIServer提供的**watch**接口进行监控，确保集群状态符合预期，是集群自愈的基础
- **Kubelet**
  - 通过APIServer提供的watch接口，监听POD信息，并执行相应的curd操作
  - 定期上报Node节点自身状态，APIServer更新至ETCD
- **Kube-proxy**
  - 外网访问内部POD
    - 反向代理
    - 负载均衡器
- **Docker**
  -  Docker引擎是kubernetes中最常用的容器运行时，管理容器的生命周期
- **Overlay-Network**
  - 开源的网络插件（flannel，calico等），保证集群内POD间相互访问
- **Ingress**
- **Egress**

### 存疑

- master node集群上的apiserver如何实现高可用？

  apiserver的高可用实现方式比较多，常用的就是给apiserver加一个负载均衡器做转发

