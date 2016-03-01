Title: Summary Concepts of Deep Learning
Date: 2016-03-01
Category: MachineLearning
Tags: machine learning, deep learning
Slug: summary-concepts-of-deep-learning
Status: draft

##机器学习
input->feature representation->learning algorithm
###监督学习
标注过的训练数据.

* 标注成本高
* 数据稀疏
###非监督学习
未标注的数据,让算法自己决定学到什么.

* 数据量大
###features
`特征的表示对机器学习性能有巨大的影响.`

* 人工特征筛选,处理,需要非常精细的调整和专业知识.
* 在很多任务中,很难知道哪些特征需要被抽取出来.例如,想要识别图像中的汽车,我们知道骑车都有轮子,所以我们可能会将轮子当做一个特征.但是实际上很难精确的描述什么是轮子.

## 神经网络
###Neurons
<p align="center">
<img src="/static/images/SingleNeuron.png" alt="SingleNeuron"  width="50%" />
</p>

神经网络的基本组成单元,叫神经元(neuron),途中的神经元是一个以$x_1,x_x,x_3$(和一个$+1$截距项(intercept term))为输入,以$h_{W,b}(x)=f(W^Tx)=f(\sum_{i=1}^{3}(W_ix_i+b)$为输出的计算单元.
其中$f:\mathbb{R}\mapsto\mathbb{R}$,被称为激活函数(activation function).常用的激活函数有:

* sigmoid function:$f(z) = \frac{1}{1+\exp(-z)}$

* tanh function:$f(z) = \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$

* rectified linear function: $f(z) = \max(0,x)$

这些函数的形状如下:
<p align="center">
<img src="/static/images/ActivationFunctions.png" alt="ActivationFunctions"  width="50%" />
</p>

###神经网络模型

<p align="center">
<img src="/static/images/Network331.png" alt="neualNetwork"  width="50%" />
</p>

####神经网络的问题

* 比较容易过拟合,参数难调.
* 训练速度比较慢,在层次比较少的情况下,并不比其他方法更优.
* 随着网络的深度增加,反向传播的梯度（从输出层到网络的最初几层）的幅度会急剧的见笑.这样,当使用梯度下降发的时候,最初的基层的权重变化非常缓慢,以至于他们不能够从样本中有效的学习,这种问题通常被称为`梯度的弥散(gradient diffusion)`.

## Deep Learning
<p align="center">
<img src="/static/images/deeplearningfeatures.png" alt="DeepLearningFeautures"  width="50%" />
</p>

###参考
[Deep Learning（深度学习）学习笔记整理系列](http://blog.csdn.net/zouxy09/article/details/8775518)

[Deep Learning](http://www.deeplearningbook.org/)

[Deep Learning Tutorial](http://ufldl.stanford.edu/tutorial/)

