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

你也可以任意尝试
















