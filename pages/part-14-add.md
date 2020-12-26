# Part 14 - ADD

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In ARM Assembly, we have three instructions that handle addition, the first being ADD, the second ADC (Add With Carry) and the final ADDS (Set Flag). This week we will focus on ADD.

Let’s look at an example to illustrate:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/107763072.jpg"/></div>

Here we see that we move decimal __67__ into __r1__ and decimal __53__ into __r2__. We then __add r1 __and __r2__ and put the result into __r0__.

"So what the heck is all that and why should I care?"

This series is going to be unlike any other in it's class.&nbsp;The goal is to take small pieces of code and see exactly what it does.&nbsp;If you are going to understand how to reverse a binary or malware of any kind, it is critical that you understand the basics.&nbsp;Learning ARM Assembly basics will help you when reversing an iPhone or Android. This tutorial series is going to work to take extremely small bites of code and talk about:

1)__The Code__:&nbsp;(Here) we speak briefly about what the code does.

2)__The Debug__:&nbsp;We break down the binary in the GDB Debugger and step though each instruction and see what specifically it does to program flow, register values and flags.

3)__The Hack__:&nbsp;We hack a piece of the code to make it do whatever WE want!

This approach will allow you to spend just a few minutes each week to get a good grasp on what is going on behind the scenes.

Next week we will dive into Debugging ADD.