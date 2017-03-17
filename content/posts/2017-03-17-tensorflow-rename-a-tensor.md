Title: Tensorflow 'rename' a Tensor
Date: 2017.03.17
Category: posts
Tags: machine learning, deep learning, tools.
Slug: tensorflow-rename-a-tensor
Author: Andy
Place: Beijing

Sometimes we want to rename a Tensor(or an Operation)in Tensorflow, there is no way to do that directly,because a tf.Operation (or tf.Tensor) is immutable once it has been created. The typical way to rename an op is therefore to use tf.identity(), which has almost no runtime cost:
   
    :::python
    with tf.name_scope("abc"):
        z = x + y
        z = tf.identity(z, name="z")

The tf.identity function returns a tensor with the same shape and contents as the input tensor or value.

#### References
[How to rename a variable which respects the name scope?](https://stackoverflow.com/questions/34399588/how-to-rename-a-variable-which-respects-the-name-scope/34399966#34399966)
