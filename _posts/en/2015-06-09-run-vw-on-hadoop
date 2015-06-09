---
layout: post
title: Run Vowpal Wabbit on Hadoop
categories: [hadoop]
tags: [hadoop,vw]
---

###Prerequisites
* hadoop 2.2.0
* Centos 6.4

###Install boost

{% highlight bash %}
wget http://jaist.dl.sourceforge.net/project/boost/boost/1.58.0/boost_1_58_0.tar.gz 
tar xzf boost_1_58_0.tar.gz
cd boost_1_58_0
sudo ./bootstrap.sh
sudo ./bjam --layout=tagged install 
cd /etc/yum.repos.d
wget http://people.centos.org/tru/devtools/devtools.repo
sudo vim /etc/yum.repos.d/DevToolset.repo
#add the following contents:
[DevToolset-2]
name=RedHat DevToolset v2 $releasever - $basearch
baseurl=http://puias.princeton.edu/data/puias/DevToolset/$releasever/$basearch/
enabled=1
gpgcheck=0 
sudo yum install devtoolset-2-gcc-4.8.1 devtoolset-2-gcc-c++-4.8.1 

vim ~/.bashrc
#add the following line to the bottom of the file
PATH=/usr/local/bin:/opt/rh/devtoolset-2/root/usr/bin/:$PATH
#then run bash to activate the modification
bash 

sudo yum install devtoolset-2-binutils-devel.x86_64 devtoolset-2-binutils.x86_64 -y 
{% endhighlight %}



###Install vw

{% highlight bash %}
wget -O vowpal_wabbit.tar.gz   https://codeload.github.com/JohnLangford/vowpal_wabbit/tar.gz/7.10
tar xzf vowpal_wabbit.tar.gz
cd vowpal_wabbit-7.10
sudo ./autogen.sh
sudo ./configure
sudo make
sudo make install
#add the path of .so files to /etc/ld.so.conf
sudo vim /etc/ld.so.conf
#add this dir /usr/local/lib
sudo /sbin/ldconfig
cd vowpal_wabbit-7.10/cluster 
cp /usr/local/bin/vw . 
mkdir ./libs 
cp  ../vowpalwabbit/.libs/* ./libs/ 
cp /usr/local/lib/libboost_program_options-mt.so.1.58.0 ./libs/ 
#modify the content of runvw-yarn.sh,add the following two lines to the top to make the libs available for the mappers
pwd=$(cd $(dirname $0); pwd)
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pwd}/libs/
and mapscript-yarn.sh 
#modify the mapscript-yarn.sh accord to your own environment.Mainly the path of the streaming jar,and file the libs dir
-Dmapred.job.queue.name=xxxx
-file ./libs

{% endhighlight %}

###Run test job
{% highlight bash %}
hadoop fs -put ../java/src/test/resources/house.vw hdfs://xxxx.com:54310/user/xxx/test_data/
sh -x mapscript-yarn.sh hdfs://xxxx.com:54310/user/xxx/test_result/ hdfs://xxxx.com:54310/user/xxx/test_data/
{% endhighlight %}

Refrences:

[vowpal wabbit on hadoop](https://scalableml.wordpress.com/2013/09/09/vowpal-wabbit-on-hadoop/)

[Vowpal Tutorial](https://github.com/JohnLangford/vowpal_wabbit/wiki/Tutorial)
