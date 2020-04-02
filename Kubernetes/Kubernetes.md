# Kubernetes + Istio 系统分享（一）

### 简介

​		本次分享主要介绍K8S基础概念以及系统架构，结合具体线上实践，了解K8S最基本的服务发布与管理流程。

### 基础概念

- **Namespace**
  - 逻辑分组，表征资源的所属
  - 通常情况下会依据不同的项目组，不同的开发环境（线上|测试）划分不同的Namespace

- **POD**

  ![1585843632389](images\1585843632389.png)

  - 由一个Pause容器和若干个关联密切业务容器构成
  - 为什么不直接管理每一个容器，而是抽象除了POD的概念？
    - POD中的业务容器共享Pause容器的IP和挂载的Volume，简化业务容器之间通信与交互

- **ReplicSet**

  - 定义了对POD副本数的期望值
  - 控制POD中扩缩容
  - 控制POD中容器的升级与回滚

- **Deployment**

  - 生成ReplicaSet进行POD的管理
  - 动态展示部署的中间状态（POD创建 | 调度 | 绑定节点 | 启动容器等）

- **Service**

  - 主要用于解决服务发现这个棘手的问题，为客户端访问集群内的POD提供的负载均衡

    ![1585843695469](images\1585843695469.png)

    - 分配虚拟ClusterIP，用作负载均衡器
    - clusterIP做DNS域名映射解决服务发现问题





### 架构概览

![1585843725969](images\1585843725969.png)

**两类角色：**

集群中，master节点与worker节点一般都是多节点的

- Master节点：管理调度集群资源

  - 根据所辖worker节点空闲状况，进行资源分配

- Worker节点：资源的提供者

  - 每个节点提供的资源单位是POD

  - POD中运行的应用容器Containers（一个或多个）

  - POD中的容器共享网络栈以及存储卷

    - **共享网络：**container相互之间访问通过localhost方式

       <img src="C:\Users\dzy17\Desktop\KnowledgeMapping\Kubernetes\images\a.jpg" alt="img" style="zoom:25%;" />     vs    <img src="C:\Users\dzy17\Desktop\KnowledgeMapping\Kubernetes\images\b.jpg" alt="共享网络的docker container模型" style="zoom:25%;" /> 

      ​                            普通docker方式                                                                    POD方式

      - 传统的两个docker容器分别被分配了veth0与veth1两个虚拟网卡，ip分别为0.2， 0.3，两个容器可以通过网桥docker0进行通信，但必须知道对方的ip地址。docker的ip是动态分配的，因此给两个服务之间访问带来障碍
      - 在一个POD中的两台Docker容器通过相关配置（pause命令），共享虚拟网卡veth0，因此可以通过localhost方式进行通信

    - **存储卷：**实现同一个pod下多个容器的文件共享





**核心组件：**

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
- **Overlay-Network**
  - 集群内POD间相互访问



#### 演示命令记录

```bash
# 通过PodIP访问
curl -g "http://[2002:ac1b:7f59:1:0:22:aae:92e]:8000"

# 通过clusterIp访问
curl -g "http://[2002:ac1f:a9c8:1::ce3]:80"

# 通过服务发现域名访问
curl http://hello-world.prj-sre-test.svc.a2.uae:80

```



