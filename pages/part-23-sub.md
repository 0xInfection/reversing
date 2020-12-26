# Part 23 – SUB

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Subtraction in ARM has four instructions which are SUB, SBC, RSB and RSC. We will start today with SUB.

Please keep in mind when you add the S suffix on the end of each such as SUBS, SBCS, RSBS, RSCS, it will affect the flags. We have spent enough time on flags in the prior lessons so that you should have a firm grasp on this now.

Let’s examine an example of SUB:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFLxtHOvvWnMg/article-inline_image-shrink_1000_1488/0/1520194165815?e=1614211200&amp;v=beta&amp;t=Zr15fm_tpPonaAtyILc2jeZvmcPlCDIfQarevVlMPIs"/></div>

To compile:

<pre spellcheck="false">as -o sub.o sub.s
ld -o sub sub.o
</pre>

We simply take __67 decimal__ and move into __r1__ and __53 decimal__ and move into __r2__ and subtract r1 – r2 and put the result in __r0__.

Next week we will dive into SUB debugging.