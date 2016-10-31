Title: Notes for Leetcode
Date: 2016-10-20
Category: posts
Tags: algorithm
Slug: notes-for-leetcode.md
Author: Andy

## 1.Binary Number Representation 
    :::java
    x = 0b1111; // which is equals to `x = 15`; and is useful when use the number for masking.
    
## 2.Rotate Function
### Original Question
Given an array of integers $A$ and let $n$ to be its length.

Assume $B_k$ to be an array obtained by rotating the array $A$ $k$ positions clock-wise, we define a "rotation function" $F$ on $A$ as follow:
$$
F(k) = 0 * B_k[0] + 1 * B_k[1] + \cdots + (n-1) * B_k[n-1].
$$
Calculate the maximum value of $F(0), F(1), \cdots, F(n-1)$.
Example:

    A = [4, 3, 2, 6]
    F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
    F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
    F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
    F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of $F(0), F(1), F(2), F(3)$ is $F(3) = 26$.

### 思路([来源](https://discuss.leetcode.com/topic/58616/java-solution-o-n-with-non-mathametical-explaination/8))
定义新的函数 $D(n)$为 $B_k[0]=A[n]$时$F(n)$ 的值，求 $F(n)$ 的最大值等价于求 $D(n)$ 的最大值，从而有：
$$
   D(n) = D(n-1) - A.length*A[n];
$$
即可得解：

    :::java
    public int maxRotateFunction(int[] A) {
        if (A.length <= 1) {
            return 0;
        }
        int max = Integer.MIN_VALUE;
        int sum = 0;
        int ai = 0;
        for (int i = 0; i < A.length; i++) {
            sum += A[i];
            ai += i * A[i];
        }
        max = ai;
        for (int i = A.length - 1; i > 0; i--) {
            ai += sum - A.length * A[i];
            max = Math.max(max, ai);
        }
        return max;
    } 



###References
[Solution to Convert a Number to Hexadecimal](https://discuss.leetcode.com/topic/65028/java-clean-code-with-explanations-and-running-time-2-solutions)

[Rotate Function](https://leetcode.com/problems/rotate-function/)

[Java Solution O(n) with non mathametical explaination](https://discuss.leetcode.com/topic/58616/java-solution-o-n-with-non-mathametical-explaination/8)
