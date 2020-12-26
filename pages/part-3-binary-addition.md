# Part 3 – Binary Addition

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Binary addition can occur in one of four different fashions:

<pre spellcheck="false">0 + 0 = 0
1 + 0 = 1
0 + 1 = 1
1 + 1 = 0 (1) [One Plus One Equals Zero, Carry One]
</pre>

Keep in mind the (1) means a carry bit. It very simply means an overflow.

Lets take the following 4-bit nibble example:

<pre spellcheck="false">  0111
+ 0100
= 1011
</pre>

We see an obvious carry in the 3rd bit. If the 8th bit had a carry then this would generate a carry flag within the CPU.

Let’s examine an 8-bit number:

<pre spellcheck="false">  01110000
+ 01010101
= 11000101
</pre>

If we had:

<pre spellcheck="false">     ﻿﻿11110000
+    11010101
= (1)11000101
</pre>

Here we see a carry bit which would trigger the carry flag within the CPU to be 1 or true. We will discuss the carry flag in later tutorials. Please just keep in mind this example to reference as it is very important to understand.

Next week we will dive into binary subtraction! Stay tuned!