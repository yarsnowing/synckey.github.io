Title: iterm2 clone session
Date: 2015-05-20
Category: posts
Slug: iterm2-clone-session
Tags: iterm2,mac,sesssion
Author: Andy

    :::bash
    vim ~/.ssh/config
    
贴入如下内容:

    :::bash
    host *
    ControlMaster auto
    ControlPath ~/.ssh/master-%r@%h:%p
    
退出iterm2，重新登录即可。






###References
[Iterm2 auto login 自动登录脚本](http://www.dbathink.com/2012/10/iterm2-auto-automatic-login-log-on-script/)

[linux clone session](http://laughingchs.iteye.com/blog/1317703)

