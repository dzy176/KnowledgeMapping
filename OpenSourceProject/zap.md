# zap学习笔记

​		作为一个日志记录器，zap必然对外提供了Logger结构体来实现打印日志的功能。

​		一般Go中通过接口定义API模式，但是zap并不是完全按照这种模式，对外提供的是struct，但是该struct中的core属性是接口，该接口真正实现了日志的编码与输出

```go
type Logger struct {
	core zapcore.Core
	development bool
	name        string
	errorOutput zapcore.WriteSyncer
	addCaller bool
	addStack  zapcore.LevelEnabler
	callerSkip int
}

type Core interface {
	LevelEnabler
	With([]Field) Core
	Check(Entry, *CheckedEntry) *CheckedEntry
	Write(Entry, []Field) error
	Sync() error
}
```

​		zap中创建Logger对象的方式：

- 建造者模式Build

  - Config结构体表征构建的logger的各项属性

    ```go
    type Config struct {
    	Level AtomicLevel `json:"level" yaml:"level"`
    	Development bool `json:"development" yaml:"development"`
    	DisableCaller bool `json:"disableCaller" yaml:"disableCaller"`
    	DisableStacktrace bool `json:"disableStacktrace" yaml:"disableStacktrace"`
    	Sampling *SamplingConfig `json:"sampling" yaml:"sampling"`
    	Encoding string `json:"encoding" yaml:"encoding"`
    	EncoderConfig zapcore.EncoderConfig `json:"encoderConfig" yaml:"encoderConfig"`
    	OutputPaths []string `json:"outputPaths" yaml:"outputPaths"`
    	ErrorOutputPaths []string `json:"errorOutputPaths" yaml:"errorOutputPaths"`
    	InitialFields map[string]interface{} `json:"initialFields" yaml:"initialFields"`
    }
    ```

    - Level: 配置日志级别：Debug | Info | Warn | Error | DPanic | Panic | Fatal

    - Devolopment: 表征是否为开发者模式

    - DisbaleCaller: 开启日志输出文件与行号

    - DisableStacktrace: 开启调用栈追踪，Develop与Produce环境下开启该功能时机不同

    - Sampling: 采用配置，减少重复日志输出，提高日志输出稳定性（文后有测试demo）

    - Encoding: 指定日志的编码器，这是zap的核心之一！目前支持json，console以及用户自定义编码器

    - EncoderConfig：用于配置zap编码器

      ```go
      type EncoderConfig struct {
      	MessageKey    string `json:"messageKey" yaml:"messageKey"`
      	LevelKey      string `json:"levelKey" yaml:"levelKey"`
      	TimeKey       string `json:"timeKey" yaml:"timeKey"`
      	NameKey       string `json:"nameKey" yaml:"nameKey"`
      	CallerKey     string `json:"callerKey" yaml:"callerKey"`
      	StacktraceKey string `json:"stacktraceKey" yaml:"stacktraceKey"`
      	LineEnding    string `json:"lineEnding" yaml:"lineEnding"`
      	EncodeLevel    LevelEncoder    `json:"levelEncoder" yaml:"levelEncoder"`
      	EncodeTime     TimeEncoder     `json:"timeEncoder" yaml:"timeEncoder"`
      	EncodeDuration DurationEncoder `json:"durationEncoder" yaml:"durationEncoder"`
      	EncodeCaller   CallerEncoder   `json:"callerEncoder" yaml:"callerEncoder"`
      	EncodeName NameEncoder `json:"nameEncoder" yaml:"nameEncoder"`
      }
      ```

      - MessageKey | LevelKey | TimeKey | NameKey | CallerKey | StacktracKey 主要用于配置json格式日志输出时的json字段名
    
      - LineEnding用于设置行分隔符
    
      - EncodeLevel用于设置level格式
    
        - dev环境采用大写字母标识日志等级(e.g. INFO), e.g.

          ```bash
        	2020-04-04T07:11:35.420+0800	INFO	zap/main.go:10	test
          ```

        - product环境采用小写字母标识日志等级(e.g. warn), e.g.
    
          ```json
          {"level":"warn","ts":1586268245.3651476,"caller":"zap/main.go:22","msg":"test"}
          ```
    
          
    
      - EncodeTime设置时间格式，dev与pro环境的区别如上
    
      - EncodeDuration
    
      - EncodeCaller设定caller返回格式
    
        - dev与pro两种logger默认采用ShortCallerEncoder返回 package/file:line
    
        - 用户可自定义采用FullCallerEncoder，返回fullpath:line, e.g.
    
          ```bash
          2020-04-07T22:23:22.538+0800	INFO	D:/GOPATH/src/test/zap/main.go:28	test
          ```
    
          
    
      - EncodeName
    
    - OutputPaths: 指定日志输出路径，支持文件路径，标准输出。用户还可以通过RegisterSink方法注册自定义输出路径
    
    -  ErrorOutputPaths: 输出zap自身内部错误日志路径
    
    - InitialFields: 可理解为日志输出额外信息
    
  -  NewProductionConfig，NewDevelopmentConfig这两个方法中分别调用了NewProductionConfig()和NewDevelopmentEncoderConfig()用以生成对应的encoderConfig

  - Build(opts ...Option)方法

    - 传参Option是一个接口

      ```go
      // An Option configures a Logger.
      type Option interface {
      	apply(*Logger)
      }
      
      ```

      该接口，可以实现对logger对象属性的变更与拓展
      
    - 1）buildEncoder(): 生成日志编码器zapcore.Encoder

      - 依据cfg.Encoding和cfg.EncodingConfig
      - 底层调用zapcore.NewConsoleEncoder或zapcore.NewJSONEncoder生成编码器

    - 2）openSinks()：生成两个日志输出对象（实现writeSyncer接口），分别是zap通用日志sink和内部错误输出errSink，该对象的作用是写日志和关闭日志对象。Sink对象就是带close的WriteSyncer

      ```go
      type Sink interface {
      	zapcore.WriteSyncer
      	io.Closer
      }
      
      type WriteSyncer interface {   
          io.Writer   
          Sync() error
      }
      ```
      
      - Open()
      
        - open()
        
          - newSink(path):
          
            - 依据path中的scheme选择对应的工厂函数生成日志输出对象
          
            - 用户可以通过RegisterSink注册自定义工厂函数，存放至全局的`_sinkFactories`字典，该工厂函数列表中默认初始化存放了key="file"，value=newFileSink工厂函数，该方法可以生成标准输出对象、标准错误输出对象和文件输出对象三种默认输出方式
          
              1. 如果输入的path为"stdout"或"stderr",会生成os.stdout与os.stderr对象
              2. 如果输入的path为"./xx.log", 日志输出到本地xx.log文件
              3. 如果输入的path形如"http://127.0.0.1:80/log/"等，用户需要实现日志接受端以及对应的工厂函数注册进zap
        - CombineWriteSyncers()：上一步open()生成的是WriteSyncer对象列表，这一步该函数将上一步的列表做了一层封装，生成的multiWriteSyncer对象也实现了WriteSyncer接口，其中Write方法就是循环调用列表中的对象的write方法
      
    - 3）New(core zapcore.Core, options ...Option)：构造Logger对象

      - NewCore(): 生成zapcore.Core接口实例ioCore

        ```go
        type Core interface {
        	LevelEnabler
        	With([]Field) Core
        	Check(Entry, *CheckedEntry) *CheckedEntry
        	Write(Entry, []Field) error
        	Sync() error
        }
        ```

        - LevelEnabler: 限定日志输出起始级别， e.g. product级别日志记录器，是不会输出debug级别的日志的，该日志记录器只会输出INFO级别及以上的日志

        - With(): 往日志context中加入额外字段

        - Check(Entry, *CheckedEntry): 根据LevelEnable等逻辑判断传入Entry是否应该被记录
          
          - AddCore(): 
            -  从对象池获取一个ce并重置， 将core对象加入ce的cores队列
            - 如果传入的ce是nil，则会通过sync.pool的new方法初始化一个。
          
        - Write(): 将日志序列化，写入目的地

          - Logger真正执行写操作并不是直接调用了Core.Write()方法，而是生成ce，ce的Write()方法中有遍历cores，并执行write方法

          - 该方法中判断ce是否dirty的理解：

            理论上，一个ce是通过getCheckedEntry()方法从对象池中获取的

            ```go
            func getCheckedEntry() *CheckedEntry {
            	ce := _cePool.Get().(*CheckedEntry)
            	ce.reset()
            	return ce
            }
            ```

            该方法中对ce进行了reset，所以dirty字段一定是false（非脏数据，没有上次一使用该对象遗留的历史数据）。但是不排除zap程序内部错误或者用户二次开发时获取ce对象没有进行reset，那么会导致日志输出不符合预期。因此，该做法提高了程序的健壮性

        - Sync(): 刷新缓冲区的日志

    

    

- 带参数的New方法

  预置了三种New方法可以直接获取开箱即用的logger，分别是

  - ```go
    NewExample()
    // 忽略了时间戳以及调用函数信息
    // 输出格式： {"level":"info","msg":"test"}
    ```

  - ```go
    NewDevelopment()
    // 日志已友好格式输出到标准错误输出，warn级别及以上的日志默认开启StackTrace
    // 输出格式：2020-04-04T07:11:35.420+0800	INFO	zap/main.go:10	test
    ```

  - ```go
    NewProduction()
    // 将日志以JSON格式输出到标准错误（debug级别日志被忽略）
    // Error级别及以上的日志默认开启StackTrace
    // 输出格式：{"level":"info","ts":1585956824.275472,"caller":"zap/main.go:20","msg":"test"}
    ```