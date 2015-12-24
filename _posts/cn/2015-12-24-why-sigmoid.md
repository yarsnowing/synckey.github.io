---
title: $sigmoid$ 怎么来的
layout: post
categories: "ml"
tags: ["machine learning","technology","logistic regression"]
---
逻辑回归是机器学习中用的最广泛的算法之一，其中一个重要的函数是 $sigmoid$ 函数，$sigmoid$ 函数的输出可以认为是预测的概率。但是，为什么是
$sigmoid$ ,为什么在二分类中使用它？

###1.逻辑回归的建模
在二分类中，我们假设 $y \in \lbrace0,1\rbrace$,在给定 $x$ 的情况下，很自然就想到使用 $Bernoulli$ 分布对 $y$ 的条件分布进行建模。$Bernoulli$
分布可以认为是二项分布的特殊情况(二项分布的$n=1$情况)，其结果只能取$0$或1(可以设想单次抛硬币的结果)。假设实验成功的概率为$p$,则$Bernoulli$的
概率密度函数和数学期望为:

$$
\begin{eqnarray*}
    f(x) &=& p^x(1-p)^{1-x}\\
    E(y) &=& p
\end{eqnarray*}
$$

###2.指数族分布($The$ $exponential$ $family$ $distribution$)

我们称如果一个分布可以被写成如下形式，就称其服从指数族分布($The$ $exponential$ $family$ $distribution$):

$$
p(y;\eta)=h(x)exp\{\eta^{T}T(x)-a(\eta)\}
$$

选定了$T,a,b$就定义了一个参数为$\eta$的分布族，我们改变$\eta$，就可以在该分布族内得到不同的分布。很多常见的分布$Bernoulli,Gaussian,
Bimomial,Poisson$等，均属于指数族分布。

假设 $y\sim Bernoulli(p),y\in\lbrace {0,1}\rbrace$,则有 $ p(y=1) = p,p(y=0)=1-p $,$Bernoulli$的概率密度函数可以改写为:

$$
\begin{eqnarray*}
p(y) &=& p^y(1-p)^{1-y} \\
     &=& exp\{log[p^y(1-p)^{1-y}] \} \\
     &=& exp\{ ylog(p) + (1-y)log(1-p) \} \\
     &=& exp\{[log(\frac{p}{1-p})]y + log(1-p)\}
\end{eqnarray*}
$$

令 $\eta=log(\frac{p}{1-p})$, 则我们得到 $p,\eta $之间的关系，即:

$$
    p=\frac{1}{1+e^{-\eta}}
$$

这就是我们的*$sigmoid$*函数!同时 $p(y)=exp\lbrace \eta y - log(1+e^{\eta}) \rbrace$ ,我们有:

$$
\begin{eqnarray*}
T(y)        &=& y \\
a(\eta)     &=& log(1+e^{\eta}) \\
b(y)        &=& 1
\end{eqnarray*}
$$

符合指数族分布的定义。

###广义线性模型(Generalized Linear Models)
假设

###References
[Andrew Ng Machine Learning ](http://open.163.com/special/opencourse/machinelearning.html)

[Michael I. Jordan The exponential family: Basics](http://www.cs.berkeley.edu/~jordan/courses/260-spring10/other-readings/chapter8.pdf)