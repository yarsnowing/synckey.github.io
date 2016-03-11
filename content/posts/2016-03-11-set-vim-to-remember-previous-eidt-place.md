Title: 让VIM记录文件上次编辑的位置
Date: 2016-03-11
Category: vim
Tags: tools,vim,linux 
Slug: set-vim-to-remember-previous-eidt-place

在`~/.vimrc`中加入如下配置:

    :::bash
    autocmd BufReadPost *
    \ if line("'\"")>0&&line("'\"")<=line("$") |
    \ exe "normal g'\"" |
    \ endif
    
###参考
[让VIM记录文件上次编辑的位置](http://www.2cto.com/os/201311/255061.html)

