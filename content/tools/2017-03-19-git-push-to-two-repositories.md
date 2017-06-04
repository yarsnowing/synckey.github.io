Title: Git Push to Two Repositories at the Same Time
Date: 2017.06.04
Tags: tools,git
Slug: git-push-to-two-repositories
Author: Andy
Place: Beijing

Suppose I have 2 repositories,

>https://github.com/synckey/synckey.github.io.git
>https://git.coding.net/synckey/synckey.git

I want to push to them within one command.

    :::shell
    #if your project is cloned from this repository, 
    #you can simply ignore this first command
    git remote add origin https://git.coding.net/synckey/synckey.git
    git remote set-url --add https://git.coding.net/synckey/synckey.git


Then if you want to push to both of them, just rum `git push` as normal.

###References

[Markdown extensions](http://blog.csdn.net/fancivez/article/details/51544354)


