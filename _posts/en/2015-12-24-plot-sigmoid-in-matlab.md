---
title: plot sigmoid in matlab
layout: post
categories: "ml"
tags: ["machine learning","technology","logistic regression"]
---

{% highlight matlab %}
a=2;
x=-10:0.1:10;
y=1./[1+exp(-a.*x)];
plot(x,y,'b');
grid on;
{%  endhighlight %}
<p align="center">
<img src="/static/images/sigmoid.svg" alt="sigmoid"  width="50%" />
</p>
