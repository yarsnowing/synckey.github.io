---
layout: post
title: iterm2 clone session功能
categories: [notes]
tags: [iterm2,mac,sesssion]
---

{% highlight bash %}
vim ~/.ssh/config
{% endhighlight %}
贴入如下内容:
{% highlight bash %}
host *
ControlMaster auto
ControlPath ~/.ssh/master-%r@%h:%p
{% endhighlight %}
退出iterm2，重新登录即可。






###References
[Iterm2 auto login 自动登录脚本](http://www.dbathink.com/2012/10/iterm2-auto-automatic-login-log-on-script/)

[linux clone session](http://laughingchs.iteye.com/blog/1317703)

