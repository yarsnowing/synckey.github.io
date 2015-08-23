---
title: mldt chapter 11
notebook: ielts
layout: post
tags: ["machinelearning"]
---
# Chapter 11 Apache Spark
Apache Spark 项目最初作为数据分析的分布式计算框架诞生于UC Berkeley大学 AMPLab 实验室。本章简要介绍scala语言和它在Spark framework中的应用。同时，本章也会介绍相关的机器学习的外部类库，类SQL查询和如何使用Spark处理流式数据（ `streaming data,指的是流式计算还是streaming编程接口？要看到后面才能去定，此处留todo`）。

## Spark：会取代Hadoop么？

关于Spark会不会取代Hadoop的激烈争论由来已久。Mapreduce编程模型是Hadoop成功的原因，但也成了Hadoop最大的瓶颈。Mapreduce将计算任务切分成大量的task，每个task都可以在一定时间内完成（ps：此处展开了，原文太隐晦），这种模型非常适合对数据进行汇总处理。但是一旦Mapreuduce运行完，很难再对任务的中间过程进行再处理。

相对于Hadoop v1， Hadoop2 不仅仅只能运行Mapreduce作业。Hadoop2 将资源管理功能独立到YARN(Yet Another Resource Negotiator)，由YARN统一管理集群的资源，因此，Hadoop在处理数据时，更像是一个操作系统。集群的资源不再只能用于运行Mapreduce，事实上，可以运行任何提交到YARN的作业。Arun C. Murthy and Vinod Kumar Vavilapalli 在《Apache Hadoop YARN》(Addison-Wesley Professional, 2014; 在 书尾“引申阅读” 章节有更多介绍) 书中介绍了如何将JBoss应用部署到YARN的Container上，就是一个绝佳的例子。

Spark 项目并不依赖MapReduce，它比Mapreduce在速度上更有优势。 据称，它在内存模式下是Hadoop速度的100倍，从硬盘中读取输入，速度也有Hadooop的10倍。如果你非常在意速度，Spark绝对是要考虑的候选工具之一。在这种情况下，可以说Spark是Hadoop的替代品。事实上，我不想讨论是否Spark是Hadoop的替代品，这个问题还是留给教科书吧。你要解决的问题才是核心，工具仅仅是工具而已。

## Java,Scala,还是Python?

Spark 作业可以用Java,Scala,或者Python中的任何一个语言编写。通常，使用什么语言只是个人偏好。但是由于Spark是用基于JVM的Scala实现的，Scala是Spark作业的首选语言。另外，Spark还提供了一个基于Scala的命令行工具，从而可以更快的获取运行结果。

Spark提供了Java的API，但是需要做一些额外的工作才能使程序正常运行。Spark也支持Python，跟Scala一样，也能使用Python的命令行工具运行Spark作业。

可惜的是，如果你想用命令行工具，就只能用Scala或者Python。要是你被Scala的思想吓到的话，别担心，读下去，我会尽量让你熟悉这个语言。另外，如果你想跳过本节，你可以直接跳到"下载安装Spark"那节。

随着你对本章的学习，你可能会感觉用Java写Spark作业实在是太笨重了。不要忘了，语言只是个人喜好而已，你要用你最得心应手的工具来解决问题。

Scala 快速入门
-------------------
如果你是一个Java的开发者，并且想用Scala，本章提供了Scala的基础入门知识。

对于想深入学习Scala的读者，可以尝试[www.scala-lang.org/documentation](www.scala-lang.org/documentation)。

## 安装Scala
由于Scala执行的是JVM的Bytecode,它被认为是JVM编程语言。如果要通过Scala操作Spark,需要先下载Scala。但如果仅仅只是想用Spark，就没有必要下载Scala，因为依赖的类库都在Spark的发型版里了。另一方面，你要是想用Scala写一些Spark作业，下载一个Scala发行版并安装当然是最好的了。你可以从Scala的官方网站[www.scala-lang.org/download/all.html](www.scala-lang.org/download/all.html) 找到所有版本的下载地址。

挑一个跟你操作系统最匹配的最新发型的稳定版本（使用最新版不会有任何问题），下载下来并解压到安装目录即可。（通常，Scala的发行版在Mac OS/Linux上是一个.gz文件，在Windows上则是一个zip文件）。

把Scala的bin目录路径加到你操作系统的${PATH}环境变量，这样你就可以在命令行里直接敲scala启动scala了。上面的都做完了，就可以继续往下读了。

## Scala包

Scala的包引入跟Java类似，但是用在java中import语句中用`*`的地方，在Scala中都用`_`：

{% highlight scala %}
import java.util._
import org.my.thing._
{% endhighlight %}

由于Scala是基于JVM的编程语言，所有你可以在Scala中引用任何Java的类库和第三方类库。

## 数据类型
Scala支持以下7种数值类的数据类型。它们都是类。与Java不同，Scala并不支持基本数据类型。

- Byte
- Char 
- Short 
- Int
- Long
- Float
- Double
- Boolean

由于它们都是类，所以你可以像在Java中调用方法一样操作这些类型：
{% highlight scala %}
scala> 1000.toString
res10: String = 1000
scala> 1000.toDouble
res11: Double = 1000.0
scala> 1000.toInt
res13: Int = 1000
{% endhighlight  %}
Scala中使用`val`或`var`声明常量和变量，两个里面使用任意一个即可。

## 类
跟Java一样，一个Scala的源文件中可以包含任意多个类（`译者注：但是只能有一个是public的`）:
{% highlight scala %}
class MyClass {
    var myval = 0
}
{% endhighlight  %}
跟老的Java风格一样，可以创建一个public变量并提供getter和setter方法。可以像例子(例子中的myval变量)中那样访问变量:
{% highlight scala %}
val newclass = new Myclass
newclass.myval = 42
println(newclass.myval)
{% endhighlight  %}
Scala的默认构造函数是public的，所有的变量都必须初始化，这是强制的。

在Scala的类中，你可以像在Java中那样定义方法，所以一个基本的void方法可以这样定义：
{% highlight scala %}
def myMethod() {
}
{% endhighlight  %}
当然，跟在Java中一样，你也可以返回带类型的变量，假设你需要返回一个int类型的变量，你可以这样写：
{% highlight scala %}
def myMethod(): Int = {
    Return 42
}
{% endhighlight  %}

最后一个例子展示怎么向Scala的方法传递参数,把两个数相加并返回结果:
{% highlight scala %}
def addNums(a: Int, b: Int) : Int = {
    return a + b
}
{% endhighlight  %}
## 调用函数
Scala中的函数调用跟Java中很像，在调用对象后面加上点号和函数名，就可以调用这个对象的方法。如果没有参数传递（如 .addNumber(1,2)）,
则括号是可选的。跟Java不同，Scala中没有`static`方法。
## 操作符
Scala中的操作符跟Java的操作符基本一致。
## 控制流
Scala支持传统的`if`,`while`和`for`控制语句。
### for循环
`for` 循环可以作用在任何集合上，如：
{% highlight scala %}
val filesInDir = (new java.io.File("/home/user/").listFiles
    for(thisFile <- filesInDir)
        println(thisFile)
{% endhighlight  %}

当你想要循环指定次数的时候，在Scala中比Java中简单很多:
{% highlight scala %}
for(i <- 1 until 10)
      println(i)
  for(i <- 1 to 10)
      println(i)
{% endhighlight  %}
你也可以在`for`循环中过滤，下面是个列出我home目录中文件列表的例子（Scala命令用粗体显示）：
{% highlight scala %}
scala> val fileshere = (new java.io.File("/home/jason/").listFiles)
fileshere: Array[java.io.File] = Array(/home/jason/twitterstream.jar, /home/jason/.ssh, /home/jason/.profile, /home/jason/spring-shell.log, /home/jason/testyarn.jar, /home/jason/twitterstreamtransformer.xml, /home/jason/.bashrc, /home/jason/worldbrain.txt, /home/jason/.bash_ logout, /home/jason/.spark_history, /home/jason/.bash_history)
scala> for(file <- fileshere if file.getName.endsWith(".xml")) print(file)*
/home/jason/twitterstreamtransformer.xml
{% endhighlight  %}

### While循环

Scala中的while循环与Java中的一样：
{% highlight scala %}
while(value != 100) {
      value += 1
}
{% endhighlight  %}
### if 语句

正如你的预期Scala中的if语句也和Java中类似，Scala也支持三元操作符：
{% highlight scala %}
Java:
boolean debug = server.equals("localhost") ? true : false;
Scala:
var debug = if (server.equals("localhost")) true else false;
{% endhighlight  %}

## 下载安装Spark

有很多种方式可以试用Spark，最简单的方式就是从Spark的官方网站上下载已经编译好的二进制包。在下载前，先确定你（或者你所在的团队）使用的Hadoop
版本， 根据你们的Hadoop版本，选择对应的Spark程序包。在编写本书时，Spark支持一下版本的Hadoop:

- Hadoop 1—(Hortonworks HDP1 and Cloudera CDH3)
- Hadoop 2—(Hortonworks HDP2 and Cloudera CDH5)
- Cloudera CDH4

Spark也不仅仅只是支持Hortonworks 或者 Cloudera的发行版，Spark与Apache官方网站提供的Hadoop也能一起工作的很好。

在你下载好你所用的Hadoop发行版对应的Spark以后，你可以把它移动到你想安装它的目录。你可以用如下命令解压下载下来的.tgz文件:
{% highlight bash %}
tar xvzf spark-1.0.0-bin-hadoop2.tgz
{% endhighlight  %}
压缩文件中国年的内容，解压后就可以直接使用了。

### Spark概览

进入你安装Spark的目录，输入以下命令启动Spark shell:
{% highlight bash %}
./bin/spark-shell
{% endhighlight  %}

Spark启动时，你可以看到如下输出：
{% highlight bash %}
jason@cloudatics:/usr/local/spark$ bin/spark-shell
  Spark assembly has been built with Hive, including Datanucleus jars on
  classpath
  14/07/05 09:28:44 INFO SecurityManager: Using Spark's default log4j
  profile: org/apache/spark/log4j-defaults.properties
  14/07/05 09:28:44 INFO SecurityManager: Changing view acls to: jason
  14/07/05 09:28:44 INFO SecurityManager: SecurityManager: authentication
  disabled; ui acls disabled; users with view permissions: Set(jason)
  14/07/05 09:28:44 INFO HttpServer: Starting HTTP Server
  Welcome to
   ____              __
  / __/__  ___ _____/ /__
 _\ \/ _ \/ _ `/ __/  '_/
/___/ .__/\_,_/_/ /_/\_\
   /_/
version 1.0.0
Using Scala version 2.10.4 (OpenJDK 64-Bit Server VM, Java 1.6.0_31)
Type in expressions to have them evaluated.
Type :help for more information.
14/07/05 09:28:51 INFO SecurityManager: Changing view acls to: jason
14/07/05 09:28:51 INFO SecurityManager: SecurityManager: authentication
disabled; ui acls disabled; users with view permissions: Set(jason)
14/07/05 09:28:52 INFO Slf4jLogger: Slf4jLogger started
14/07/05 09:28:52 INFO Remoting: Starting remoting
14/07/05 09:28:52 INFO Remoting: Remoting started; listening on
addresses :[akka.tcp://spark@cloudatics.com:38921]
14/07/05 09:28:52 INFO Remoting: Remoting now listens on addresses:
[akka.tcp://spark@cloudatics.com:38921]
14/07/05 09:28:52 INFO SparkEnv: Registering MapOutputTracker
14/07/05 09:28:52 INFO SparkEnv: Registering BlockManagerMaster
14/07/05 09:28:52 INFO DiskBlockManager: Created local directory at /
tmp/spark-local-20140705092852-2f00
14/07/05 09:28:52 INFO MemoryStore: MemoryStore started with capacity
297.0 MB.
14/07/05 09:28:53 INFO ConnectionManager: Bound socket to port 48513
with id = ConnectionManagerId(cloudatics.com,48513)
14/07/05 09:28:53 INFO BlockManagerMaster: Trying to register
BlockManager
14/07/05 09:28:53 INFO BlockManagerInfo: Registering block manager
  cloudatics.com:48513 with 297.0 MB RAM
  14/07/05 09:28:53 INFO BlockManagerMaster: Registered BlockManager
  14/07/05 09:28:53 INFO HttpServer: Starting HTTP Server
  14/07/05 09:28:53 INFO HttpBroadcast: Broadcast server started at
  http://176.67.170.176:41692
  14/07/05 09:28:53 INFO HttpFileServer: HTTP File server directory is /
  tmp/spark-c6a5efed-113d-4dd9-9cd0-7618d901f389
  14/07/05 09:28:53 INFO HttpServer: Starting HTTP Server
  14/07/05 09:28:53 INFO SparkUI: Started SparkUI at http://cloudatics.
  com:4040
  14/07/05 09:28:54 WARN NativeCodeLoader: Unable to load native-hadoop
  library for your platform... using builtin-java classes where applicable
  14/07/05 09:28:54 INFO Executor: Using REPL class URI:
  http://176.67.170.176:39192
  14/07/05 09:28:54 INFO SparkILoop: Created spark context..
  Spark context available as sc.
scala>
{% endhighlight  %}

我给出了所有输出，因为有一些重要的东西下面要解释。现在你的终端底部出现了`scala>`的提示符，说明的你Scala已经安装好了。

### 数据源

Spark支持Hadoop的输入数据文件系统，只要你的数据源支持Hadoop的`InputFormat`接口，就可以轻松的把它读入Spark。

最简单的就是本地文件系统，亚马逊 S3 buckets，Hbash,Cassandra，已经已经保存在HDFS上的文件。在下一节，你会使用
sc.textFile方法加载文件。这个方法并不只是在指定的文件可用，你可以用这个方法对文件，压缩文件，甚至是目录进行通配符处理。

### 测试Spark

找一个文本文件，按照本章后面的步奏来测试Spark，我用了一个本地文件系统的文件来运行测试例子。

#### 加载文本文件

首先，加载文本文件，从scala的命令行，输入：
{% highlight scala %}
 scala> var textF = sc.textFile("/home/jason/worldbrain.txt")
{% endhighlight  %}

一般情况下，将文件内容赋值给一个变量`textF`,Spark的输出如下：
{% highlight scala %}
14/07/05 09:40:08 INFO MemoryStore: ensureFreeSpace(146579) called with
  curMem=0, maxMem=311387750
  14/07/05 09:40:08 INFO MemoryStore: Block broadcast_0 stored as values
  to memory (estimated size 143.1 KB, free 296.8 MB)
  textF: org.apache.spark.rdd.RDD[String] = MappedRDD[1] at textFile at
  <console>:12
scala>

{% endhighlight  %}
Spark 使用弹性分布式数据集(Resilient Distributed Datasets,RDD),所以在输出中可以看到你有了一个String 的MappredRDD， 
用加载好的文件你可以对它进行分析获取一些结论。

#### 快速分析

使用加载的数据，可以运行一些快速的分析，首先看一下RDD中有多少个元素:
{% highlight scala %}
scala> textF.count()
{% endhighlight  %}
输出如下:
{% highlight scala %}
14/07/05 09:58:01 INFO SparkContext: Job finished: count at
<console>:15, took 0.036546484 s
res4: Long = 469
scala>
{% endhighlight  %}
count的结果表名RDD中元素的个数而不是文件的行数，你可以查看RDD的第一个元素:
{% highlight scala %}
scala> textF.first()
And the output appears:
14/07/05 10:00:20 INFO SparkContext: Job finished: first at <console>:15, took 0.007266678 s
res5: String = THE papers and addresses I have collected in this little book are submitted as contributions,......
scala>
{% endhighlight  %}
可以看出，输出非常快，因为RDD是基于内存的。

#### 从RDD中过滤文本

使用`.filter`函数可以对文本文件进行过滤分析，假设你想要知道 "statistical"这个单词在文件中出现的次数，你可以运行如下代码：
{% highlight scala %}
scala> textF.filter(line => line.contains("statistical")).count()
{% endhighlight  %}
对Spark的RDD进行迭代并过滤，只要Scala的一行代码就能完成任务，因为你在最后调用了count函数，你可以得到如下输出:
{% highlight scala %}
14/07/05 10:16:55 INFO SparkContext: Job finished: count at
<console>:15, took 0.042640019 s
res7: Long = 2
{% endhighlight  %}

在这个文件中"statistical"一共出现了2次，整个查询在0.04s完成，如果需要，你可以将这个输出保存到另外一个Scala数组：
{% highlight scala %}
scala> var filtered = textF.filter(line => line.contains("statistical"))
  filtered: org.apache.spark.rdd.RDD[String] = FilteredRDD[4] at filter at
  <console>:14
  scala> filtered.count
  14/07/08 09:20:16 INFO SparkContext: Job finished: count at
  <console>:17, took 0.067395793 s
  res4: Long = 2
{% endhighlight  %}

利用Scala简明的语法，以及Spark强大的分布式内存数据集（RDD）处理，你拥有了快速处理海量数据的灵巧工具。

#### Spark web 页面


之前提到过，当你启动Spark时，一系列的后台进城就启动了。其中一个就是基于web的ui。你在浏览器里面输入`http://<yourdomain>:4040`,假设Spark还在运行，你应该能
得到`Figure 11-1`所示的网页。

到目前为止，你运行的每条命令都是Spark的一个作业，Spark会自动记录它的运行时间和输出。web ui上也能看到存储系统和运行环境的相关信息。

你可以点击每个Stage来查看job的详细信息和运行输出。如果你的作业遇到问题，在这里可以很方便的看到作业的概要信息。


### Spark和Hadoop对比

第十章提到了要用Java编写一个Mapreduce作业提交到Hadoop运行还是很麻烦的。

基本的Java代码模板通常都是在map和reduce阶段的分析:

{% highlight scala %}
  public static class Map extends MapReduceBase implements
              Mapper<LongWritable, Text, Text, IntWritable> {
          private final static IntWritable one = new IntWritable(1);
          private Text word = new Text();
          public void map(LongWritable key, Text value,
                  OutputCollector<Text, IntWritable> output, Reporter
reporter)
                  throws IOException {
              // ususally emit something to the reducer here....
} }
      public static class Reduce extends MapReduceBase implements
              Reducer<Text, IntWritable, Text, IntWritable> {
 public void reduce(Text key, Iterator<IntWritable> values,
                  OutputCollector<Text, IntWritable> output, Reporter
reporter)
                  throws IOException {
              // reducer would add the value +1 for example
} }

{% endhighlight  %}


接着定义一个Hadoop作业，就可以提交到Hadoop平台运行了：

{% highlight scala %}
public static void main(String[] args) throws IOException {
          JobConf conf = new JobConf(BlankHadoopJob.class);
          conf.setJobName("BlankHadoopJob");
          conf.setOutputKeyClass(Text.class);
          conf.setOutputValueClass(IntWritable.class);
          conf.setMapperClass(Map.class);
          conf.setCombinerClass(Reduce.class);
          conf.setReducerClass(Reduce.class);
          conf.setInputFormat(TextInputFormat.class);
          conf.setOutputFormat(TextOutputFormat.class);
          FileInputFormat.setInputPaths(conf, new Path(args[0]));
          FileOutputFormat.setOutputPath(conf, new Path(args[1]));
          JobClient.runJob(conf);
      }
{% endhighlight  %}

一些开发者抱怨使用Java编写完整的Mapreudce作业代码量太大了. 我从来没有遇到过这种问题(因为我使用模板)。但是当我告诉你同样的功能在Spark中怎么运行
，你就知道他们为什么要抱怨了。
在Spark中，你可以用一个Mapreduce最常见的作业word count 作业来展示Spark作业又多简单。使用刚才用过的文本文件，你可以用spark-shell运行Mapreduce作业。
首先，加载文件:
{% highlight scala %}
scala> var textF  = sc.textFile("/home/jason/worldbrain.txt")
{% endhighlight  %}
然后创建一个保存Mapreduce结果的变量:
{% highlight scala %}
scala> var mapred = textF.flatMap(line => line.split(" ")).map(word =>
  (word, 1)).reduceByKey((a,b) => a+b)
{% endhighlight  %}

输出结果:

{% highlight scala %}
scala> mapred.collect
{% endhighlight  %}

你会看到一些列的输出:
{% highlight scala %}
14/07/08 09:28:29 INFO SparkContext: Job finished: collect at
  <console>:17, took 0.78279487 s
  res7: Array[(String, Int)] = Array((professors,,1), (mattered,1),
  (intimately,1), (better.,3), (someone,3), (House,1), (manifestly,1),
  (order,13), (socialism.,1), (apprehension,4), (conclusively,1),
  (gowns,2), (behind,3), (Out",,1), (merge,1), (wasn't,1), (been,125),
  (Judea;,1), (gap,5), (underrate,1), (aspects;,1), (knows,8),
  (informative,15), (divorced,1), (are,259), (records,4), (2.,1),
  (Western,3), (politician,,1), (room—and,1), (newspapers,,3),
  (picture.,1), (interchange—from,1), (prete
{% endhighlight  %}

可以用RDD的`.saveAsTextFile`将结果保存为文本:
{% highlight scala %}
scala> mapred.saveAsTextFile("/home/jason/testoutput")
{% endhighlight  %}

与Hadoop一样，Spark将结果保存在一个目录中，我把这个目录称为`testoutput` ,在这个目录中，你可以看到reduce输出的part文件:
{% highlight scala %}
 -rw-r--r-- 1 1234 1234 52961 Jul  8 13:47 part-00000
   -rw-r--r-- 1 1234 1234 52861 Jul  8 13:47 part-00001
   -rw-r--r-- 1 1234 1234     0 Jul  8 13:47 _SUCCESS
{% endhighlight  %}

这些文件的内容就是基本的Word count:
{% highlight scala %}
(lags—throughout,1)
  (however,9)
  (cry.,1)
  (eminent,2)
  (dangerous,5)
  (varieties,1)
  (History.,1)
  (behind,,1)
  (late,3)
  (nineteenth,6)
  (helpless,1)
  (throwing,2)
  (aesthetic,4)
  (leapt,2)
{% endhighlight  %}

只用三行代码就完成了对原始文本文件的一个Mapreduce分析作业，注意我并没有过滤掉特殊的字符并将文本转为小写字母，但是依然是一个完整的word count
程序。

### 编写可以提交的Spark作业

前面的对Spark的简短减少显示了Spark的速度，并且可以很轻松的解决一些问题。尽管Spark shell可以用来很轻松的分析数据并且获取到一些基本信息：
如count,出现次数等，但是有时候我们需要编写完整的Spark作业。前面介绍过，由于Spark提供了Scala,Java,Python的api，Spark程序可以用
这些语言中的任何一种编写。本节主要介绍怎么用Scala和Java编写Spark作业。
{% highlight scala %}
注意：Scala程序需要Scala库和编译器的支持，本章的前面已经介绍过如何安装它们。
{% endhighlight  %}
#### 用Scala编写Spark作业

Scala应用和Java应用在代码上很相似，使用Scala Build Tool(sbt),你可以在一个地方管理构建的所有信息。

##### 安装SBT

由于Scala主要的类库并不提供Scala Build Tool，所以需要单独下载安装sbt。你可以从 [www.scala-sbt.org/download.html](www.scala-sbt.org/download.html)下载
与你的系统适配的版本并且解压它。确保安装文件的可执行目录在你的系统PATH环境变量中，这样就你可以直接在命令行中输入`sbt`来运行sbt了。

#### Scala程序代码

创建一个叫`ScalaMRExample`的项目，然后在这个目录下创建`src`和`main`目录。


{% highlight scala %}
mkdir –p ScalaMRExample/src/main
{% endhighlight  %}


与MapReduce的例子类似，在文件`ScalaMRExample.scala`中的Scala版本的Spark应用代码如下：

{% highlight scala %}
 import org.apache.spark.SparkContext
  import org.apache.spark.SparkContext._
  import org.apache.spark.SparkConf
  object ScalaMRExample {
    def main(args: Array[String]) {
      val configuration = new SparkConf().setAppName("Scala MapReduce
  Example")
      val sc = new SparkContext(conf)
      val textFile = "/home/jason/worldbrain.txt"
      val textSc = sc.textFile(textFile)
      val mapred = textFile.flatMap(line => line.split(" ")).map(word =>
  (word, 1)).reduceByKey((a,b) => a+b)
      mapred.collect
      mapred.saveAsTextFile("wboutput")
} }
{% endhighlight  %}

你需要根据你的开发环境改变文件名和路径，这个程序引入了需要的Spark库，设置了Spark应用的名字和运行的`main`
方法。这些都跟Java版的代码很像。

为了加载系统变量和classpath,你创建了一个`SparkConf`对象，传入你的应用名（在例子里面是`ScalaMapReduce Example`），程序中剩余的部分
跟前面的Java版本一样:加载文本文件，运行简单的MapReduce，输出结果，并将结果报错到某一个地方。

#### sbt工具

Scala的构建工具SBT与Java的构建工具Ant和Maven类似，你需要在`ScalaMRExample`目录下放一个构建文件来告诉
Scala项目信息，依赖，和依赖下载地址
{% highlight scala %}
  name := "ScalaMRExample"
  version := "0.1"
  scalaVersion := "2.10.4"
  libraryDependencies += "org.apache.spark" %% "spark-core" % "1.0.0"
  resolvers += "Akka Repository" at "http://repo.akka.io/releases/"
{% endhighlight  %}

讲这个文件保存为`scalamrexample.sbt`，然后就可以用sbt对项目进行打包了。检查目录结构以确保一切都准备好了。在Linux/MacOS X系统中，
你可以用find命令来检查:
{% highlight bash %}
 Jason-Bells-MacBook-Pro:ScalaMRExample Jason$ find . -print
  .
  ./scalamrexample.sbt
  ./src
  ./src/main
  ./src/main/scala
  ./src/main/scala/ScalaMRExample.scala
{% endhighlight  %}

当你看到文件列表已经准备好了（应该与前面的类似），你就可以用sbt工具对项目进行打包了。确保你在`ScalaMRExample`目录下，然后运行

{% highlight bash %}
sbt package
{% endhighlight  %}

第一次运行这个命令需要花费一些时间，因为`sbt`可能需要下载外部依赖库，命令执行完成后，代码就编译完成了，包也打好了：
{% highlight bash %}
Jason-Bells-MacBook-Pro:ScalaMRExample Jason$ sbt package[info] Set
  current project to ScalaMRExample (in build file:/Users/Jason/work/
  scala/ScalaMRExample/)
  [info] Compiling 1 Scala source to /Users/Jason/work/scala/
  ScalaMRExample/target/scala-2.10/classes...
  [info] Packaging /Users/Jason/work/scala/ScalaMRExample/target/scala-
  2.10/scalamrexample_2.10-1.0.jar ...
  [info] Done packaging.
  [success] Total time: 8 s, completed 09-Jul-2014 17:25:49
{% endhighlight  %}

新编译好的包在`target/scala-2.10`中:
{% highlight bash %}
 Jason-Bells-MacBook-Pro:ScalaMRExample Jason$ cd target/scala-2.10/
  Jason-Bells-MacBook-Pro:scala-2.10 Jason$ ls -l
  total 16
  drwxr-xr-x  7 Jason  staff   238  9 Jul 17:25 classes
  -rw-r--r--  1 Jason  staff  4495  9 Jul 17:25 scalamrexample_2.10-
  1.0.jar
  Jason-Bells-MacBook-Pro:scala-2.10 Jason$
{% endhighlight  %}








#### 运行Spark项目

你只要用编译好的jar文件就可以了。假设你就在jar文件所处的目录中，你可以使用spark-submit命令提交作业：
{% highlight bash %}

  /usr/local/spark/bin/spark-submit --class "ScalaMRExample" \
  --master local[4] scalamrexample_2.10-1.0.jar

{% endhighlight  %}

`--master local[4]`选项告诉Spark当程序启动时，创建4个本地节点。如果一切进展顺利，你就能看到spark开始
工作了:

{% highlight bash %}
  14/07/09 19:32:42 INFO TaskSetManager: Finished TID 5 in 922 ms on
  localhost (progress: 2/2)
  14/07/09 19:32:42 INFO TaskSchedulerImpl: Removed TaskSet 2.0, whose
  tasks have all completed, from pool
  14/07/09 19:32:42 INFO DAGScheduler: Completed ResultTask(2, 1)
  14/07/09 19:32:42 INFO DAGScheduler: Stage 2 (saveAsTextFile at
  ScalaMRExample.scala:15) finished in 0.924 s
  14/07/09 19:32:42 INFO SparkContext: Job finished: saveAsTextFile at
  ScalaMRExample.scala:15, took 1.014446651 s

{% endhighlight  %}

由于你将结果保存到了`wboutput`目录，你可以在你的目录结构中看到这个目录。与使用Hadoop相比，使用Scala编写
MapReduce作业变得非常简单。这病不是说哪个更好，只是完成任务又多了一种选择。下面看看用Java怎么编写Spark项目。

### 用Java编写Spark作业

用Java编写Spark作业与刚才介绍的用Scala的方法基本类似，主要的不同就是语言和构建工具。

Spark的Java api比scala的稍微难理解一点，你不能只用4行代码就能写好一个Mapreduce作业了。

{% highlight scala %}
import scala.Tuple2;
  import org.apache.spark.SparkConf;
  import org.apache.spark.api.java.JavaPairRDD;
  import org.apache.spark.api.java.JavaRDD;
  import org.apache.spark.api.java.JavaSparkContext;
  import org.apache.spark.api.java.function.FlatMapFunction;
  import org.apache.spark.api.java.function.Function2;
  import org.apache.spark.api.java.function.PairFunction;
  import java.util.Arrays;
  import java.util.List;
  import java.util.regex.Pattern;
  public final class JavaMRExample {
    private static final Pattern spacePattern = Pattern.compile(" ");
    public static void main(String[] args) throws Exception {
      SparkConf configuration = new SparkConf().
  setAppName("JavaMRExample");
      JavaSparkContext ctx = new JavaSparkContext(configuration);
      JavaRDD<String> linesOfText = ctx.textFile("/home/jason/worldbrain.
  txt", 1);
      JavaRDD<String> findWords = linesOfText.flatMap(new
  FlatMapFunction<String, String>() {
        @Override
        public Iterable<String> call(String thisString) {
          return Arrays.asList(spacePattern.split(thisString));
        }
  });
      JavaPairRDD<String, Integer> getTheOnes = findWords.mapToPair(new
  PairFunction<String, String, Integer>() {
        @Override
        public Tuple2<String, Integer> call(String thisString) {
          return new Tuple2<String, Integer>(thisString, 1);
        }
  });
      JavaPairRDD<String, Integer> finalCounts = getTheOnes.
  reduceByKey(new Function2<Integer, Integer, Integer>() {
        @Override
        public Integer call(Integer i1, Integer i2) {
          return i1 + i2;
        }
  });
      List<Tuple2<String, Integer>> thisOutput = finalCounts.collect();
      for (Tuple2<?,?> tuple : thisOutput) {
        System.out.println(tuple._1() + ": " + tuple._2());
      }
      ctx.stop();
    }
  }

{% endhighlight  %}

与Scala版本的MapReduce代码相比，Java版的需要写更多的代码，使用Java Spark API需要更关注更多:
* 切分单词
* 给每个单词count技术赋值1
* 给每个独立的单词计算出现次数
* 输出结果

#### 使用maven构建项目

在整本书中我都是用Eclipse创建和构建工程，Maven是一个构建工具（我认为`sbt`也从Maven中活去了很多灵感）。Maven和Ant是Java的主要构建工具，
如果你没有安装Maven，你可以从[http:// maven.apache.org](http:// maven.apache.org)下载。

对每个项目而言，你需要一个Maven构建文件，叫做pmo.xml.

{% highlight xml %}
  <project>
    <groupId>com.mlbook</groupId>
    <artifactId>javamrexample</artifactId>
    <modelVersion>4.0.0</modelVersion>
    <name>Java MR Example</name>
    <packaging>jar</packaging>
    <version>1.0</version>
    <repositories>
      <repository>
        <id>Akka repository</id>
        <url>http://repo.akka.io/releases</url>
      </repository>
    </repositories>
    <dependencies>
      <dependency>
        <groupId>org.apache.spark</groupId>
        <artifactId>spark-core_2.10</artifactId>
        <version>1.0.0</version>
      </dependency>
    </dependencies>
</project>
{% endhighlight  %}

从这个文件可以看到项目的基本结构，并且配置了从哪个仓库下载依赖。对Spark项目而言，你需要在dependencies中指名Spark API的依赖。

#### 用Maven打包

你可以从命令行中执行Maven打包命令：
{% highlight bash %}
mvn package
{% endhighlight  %}

Maven构建工具会下载依赖，创建类文件，然后将依赖的类打包进jar文件。构建好后，一个`target`目录会被自动创建，里面包含了打好包的jar文件:

{% highlight bash %}
  Jason-Bells-MacBook-Pro:JavaMRExample Jason$ cd target/
  Jason-Bells-MacBook-Pro:target Jason$ ls -l
  total 24
  drwxr-xr-x  10 Jason  staff   340  9 Jul 18:19 classes
  -rw-r--r--   1 Jason  staff  8679  9 Jul 18:19 javamrexample-1.0.jar
  drwxr-xr-x   3 Jason  staff   102  9 Jul 18:04 maven-archiver
  Jason-Bells-MacBook-Pro:target Jason$
{% endhighlight  %}

与Scala的例子类似，你需要使用`spark-submit`提交Spark作业：
{% highlight bash %}
jason@cloudatics:~$ /usr/local/spark/bin/spark-submit --class
  "JavaMRExample" \
  --master local[4] javamrexample-1.0.jar
{% endhighlight  %}

Spark会执行jar文件，你可以在终端中看到MapReduce的输出：

{% highlight bash %}
 14/07/09 20:37:08 INFO DAGScheduler: Stage 0 (collect at JavaMRExample.
  java:44) finished in 0.784 s
  14/07/09 20:37:08 INFO SparkContext: Job finished: collect at
  JavaMRExample.java:44, took 2.47317507 s
  young: 29
  mattered: 1
  intimately: 1
  journeys.: 1
  Let: 7
  House: 1
  (Socialism),: 1
  instance,: 1
  superannuated.: 1
  proportions,: 1
  Contributed: 1
  secure: 4
  incoherent.: 1
  everyone.: 1
  gowns: 2
  well-informed: 1
{% endhighlight  %}

### Spark编程总结

至此，你已经学会了2种快速构建Spark作业的方法，如前所述，使用Java还是Scala取决于你的喜好。在生产环境中，你肯定不想用一个你不是100%
熟悉的语言编写的代码。

有了Spark的基本信息和构建Spark作业的方法，你可以继续学习一些Spark上可以用的库了。

## Spark SQL

Hadoop社区中最常被问到的一个问题就是"我可以运行SQL-like查询么?"。有些人在处理数据时，非常希望使用SQL,原因很简单，
SQL语言简洁优雅容易懂。Hadoop生态中的Pig脚本就以非常接近英文的方式表达Mapreudce作业了，纯SQL的诱惑实在太大，
所以他们常常问是否存在这样的SQL。

SparkSQL就是这样的工具--Spark框架下的SQL-like查询工具。它就是纯的SQL工具，所以你可以用它在Spark上进行scala查询，甚至是HiveSQL查询。
数据可以是像Apahce Hive这样的外部数据库或者讲数据加载到内存作为RDD进行查询。

{% highlight bash %}
NOTE:
SparkSQL的SQL解析器对大多数人来说都非常有用，但是并没有像期待的那样，像一个数据库系统那样高级。如果你需要像数据库系统那样的灵活性，
建议使用HiveSQL。在本节的后面，将主要介绍SparkSQL的解析器。
{% endhighlight  %}

### 基本概念

创建好了SparkContext后，你可以很轻松的创建SparkSQL实例，并将它关联到当前上下文。这个操作可以在Scala shell或者单独的java，scala，python 
写的Spark作业中完成。如果你还记得之前编写Spark作业的方式，编程将会很简单。

一个包含SparkSQL库的基本代码如下：


{% highlight scala %}
 import org.apache.spark.SparkContext
  import org.apache.spark.SparkContext._
   import org.apache.spark.SparkConf
    object SparkSQLExample {
      def main(args: Array[String]) {
        val configuration = new SparkConf().setAppName("SparkSQL Example")
        val sc = new SparkContext(configuration)
        val sql = new org.apache.spark.sql.SQLContext(sc)
        // program continues.
  } }
{% endhighlight  %}
你需要在你的`sbt`构建文件中加入SparkSQL的依赖，我已经为上面的代码创建好了一个新的构建文件:
{% highlight bash %}
name := "SparkSQLExample"

  version := "1.0"
  
  scalaVersion := "2.10.4"
  
  libraryDependencies += "org.apache.spark" %% "spark-core" % "1.0.0"
  
  libraryDependencies += "org.apache.spark" %% "spark-sql" % "1.0.0"
  
  resolvers += "Akka Repository" at http://repo.akka.io/releases/

{% endhighlight  %}

别忘了每行文本之间要加入额外的空行,否则构建工具在构建时会报错。

#### 在RDD上使用SparkSQL

下面将会在RDD上使用SparkSQL构建一个真实的例子，将数据放在内存中将会大大加快查询的速度。同时，你将会看到一个
包含多个`.scala`文件的应用。

##### 生成数据

例子中使用了一个包含如下信息的`.csv`文件：
* 唯一的id
* 名字
* 姓
* 英国邮政编码
* 生日（格式为: 月/日/年）
* 纬度
* 经度

这些数据可以可以展现用户管理数据库中的某些特征了。你也可以自己产生数据或者使用`fakenamegenerator.com`服务为你
生成测试数据。如果你使用了`fakenamegenerator.com`的服务，请确保第一行没有列名，如果有，就删除掉他们。

一个数据的样本如下:
{% highlight bash %}

  72215385-fad0-45fd-b932-a3d4fa07fb6d,William,Winter,DG3
  7AL,1/4/1969,55.282416,-3.831666
  71efb06f-63a7-4312-abe2-1fc4c8bd52e5,Billy,Noble,DD6
  7FU,9/11/1969,55.597429,-3.170968
  eac7b8f6-2d71-49a7-8e4d-a780826ce893,Kayleigh,Atkins,DG8
  9ES,1/20/1932,54.73341,-4.407141
  337d498d-9bed-4663-b688-6ec2651bcd9d,Emma,Perry,IM3
  2GE,4/16/1935,54.173625,-4.480233
  c3b0cc54-1f2f-416f-9b91-17a0700a4dc1,Liam,Carr,EX32
  8AA,1/3/1991,50.682015,-3.119895
  ea6acc38-1b69-424f-b885-09b078f6eaf2,Alex,Dodd,PH2
  0QJ,6/24/1993,55.982172,-3.592573
  
{% endhighlight  %}

数据准备好了之后，就可以开始编码了。

#### Scala应用