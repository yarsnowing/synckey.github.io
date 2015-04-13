---
layout: post
title: test highlight
categories: [personal]
tags: [心情]
---


```python
    print ""
    for i in ["1","2"]:
        print map()
```
{% highlight c tabsize=10 linenumber linenos=10 %}
/* hello world demo */
#include <stdio.h>
int main(int argc, char **argv)
{
    printf("Hello, World!\n");
    return 0;
}
{% endhighlight %}

{% highlight python %}
# encoding=utf-8
import signal
import os

__author__ = 'jian.wang'

"""
    执行器
"""
import subprocess


class Executor(object):
    def __init__(self):
        pass

    def _createFiles(self, stdoufilename, stderrfilename):
        stdout = open(stdoufilename, "w")
        stderr = open(stderrfilename, "w")
        return (stdout, stderr)


    def exe(self, cmd_line, stdoutfilename, stderrfilename):
        """
        """
        stdout, stderr = self._createFiles(stdoutfilename, stderrfilename)
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)  # 避免子进程在退出后变成defunct
        p = subprocess.Popen(cmd_line, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr,
                             shell=True)
        return p


def main():
    e = Executor()
    print e.exe("sh test_subprocess.sh", "stdout.txt", "stderr.txt")


if __name__ == "__main__":
    main()
{% endhighlight %}

{% highlight java %}
/****
 CPU使用率其实就是你运行的程序占用的CPU资源，表示你的机器在某个时间点的运行程序的情况。
*/
public class CPUTest
{
    public static void main(String[] args)
    {
        long startTime = 0;// 开始时间
        int busyTime = 100000000;// 繁忙时间
        int idleTime = 1;// 空闲时间
        while (true)
        {
            startTime = System.currentTimeMillis();
            // CPU繁忙
            while (System.currentTimeMillis() - startTime <= busyTime)
                ;
            // CPU空闲
            try
            {
                Thread.sleep(idleTime);
            }
            catch (InterruptedException e)
            {
                e.printStackTrace();
            }
        }
    }
}
{% endhighlight %}

```python
def test_conf(request):
    request_data = __get_request_data(request)
    LOG.info("DRAGON_PROJECT_PREFIX_PATH : " + conf.DRAGON_PROJECT_PREFIX_PATH.get())
    LOG.info("DRAGON_WORKFLOW_PREFIX_PATH : " + conf.DRAGON_WORKFLOW_PREFIX_PATH.get())
    LOG.info("DRAGON_IMPORT_DRIVER_PATH : " + conf.DRAGON_IMPORT_DRIVER_PATH.get())
    LOG.info("DRAGON_INCREMENT_DRIVER_PATH : " + conf.DRAGON_INCREMENT_DRIVER_PATH.get())
    LOG.info("DRAGON_HIVE_DRIVER_PATH : " + conf.DRAGON_HIVE_DRIVER_PATH.get())
    LOG.info("DRAGON_STD_LOG_PATH : " + conf.DRAGON_STD_LOG_PATH.get())
    LOG.info("DRAGON_AZKABAN_SERVER_URL : " + conf.DRAGON_AZKABAN_SERVER_URL.get())
    LOG.info("DRAGON_AZKABAN_USERNAME : " + conf.DRAGON_AZKABAN_USERNAME.get())
    return render('index.mako', request,{})


def create_project(request):
    request_data = __get_request_data(request)

#    query_data["source_db"]="xxxxx"
#        importJob = ImportJob()
#        importJob.save(query_data)
#        importJob=ImportJob.objects.get(id=12)
#        importJob.get_property("source_db")
#        importJob.save()
#    create_project.create_project(request_data)

    return render('create_project.mako', request,{})
```
