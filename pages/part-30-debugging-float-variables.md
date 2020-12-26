# Part 30 – Debugging Float Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; float myNumber = 1337.1;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQE-W2lfO5Z_cA/article-inline_image-shrink_1000_1488/0/1521196070985?e=1614211200&amp;v=beta&amp;t=RWKXhZZGZHVCzAbQtV-bQK7Ea8Fy409f51OkQbHqysE"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQFmb2yUlPGMOA/article-inline_image-shrink_1000_1488/0/1521196099167?e=1614211200&amp;v=beta&amp;t=COWt7C0rXVbWEbqXg3AyIWNcPiITn23wXT0GjrKqFuo"/></div>

Let’s break on __main+20__ and continue to that point.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQFpDjN2vhgKeQ/article-inline_image-shrink_1000_1488/0/1521196123405?e=1614211200&amp;v=beta&amp;t=0I1-YcZ7owFNpbnG-6OLqxIwPj_9j6Gi94sGCGeIvPc"/></div>

Let’s examine what value is inside __r11-8__.&nbsp;We clearly see it is __1337.09998__ which approximates our value in our original c++ code.&nbsp;Keep in mind a float has roughly 7 decimal digits of precision and that is why we do not see __1337.1__ so please remember that as we go forward.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQEGcCsAFAAzag/article-inline_image-shrink_1000_1488/0/1521196151522?e=1614211200&amp;v=beta&amp;t=sMv2aIBltLU0qTQf2CzrEjvscSq_jCEQWERbXnBxj7I"/></div>

We can also see this value in high memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQEYJsBEkFRfmA/article-inline_image-shrink_1000_1488/0/1521196178255?e=1614211200&amp;v=beta&amp;t=T6DXcYhk-HziLrRj9FDcH_Dp5kmxQsmcDr4_A8ryW30"/></div>

Let’s break on __main+28__ and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQGMfcuxt_W1yg/article-inline_image-shrink_1000_1488/0/1521196203419?e=1614211200&amp;v=beta&amp;t=rx-5w_bCf6INOulvfw-g0oh1mQcj5qwXlQBfdc_slNY"/></div>

We see a strange new instruction.&nbsp;We see __vldr__ and the value within __r11, \#8__ being moved into__ s0__.&nbsp;So what is __s0__?&nbsp;We have a math co-processor which has a series of additional registers that work with decimal or floating-point numbers.&nbsp;Here we see an example of such to which the value of __1337.09998 __is being moved into __s0__.&nbsp;The __vldr__ instruction loads a constant value into every element of a single-precision or double-precision register such as__ s0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQGASJZmOCaRUQ/article-inline_image-shrink_1000_1488/0/1521196373197?e=1614211200&amp;v=beta&amp;t=S2c5siOgLZbi5XUqD9RZXhDtTnm_C59y-S4pti-PeIs"/></div>

We can only see these special registers if we do a info registers all command as we do below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQHOWgjk7hN3Tg/article-inline_image-shrink_1000_1488/0/1521196414932?e=1614211200&amp;v=beta&amp;t=iuvSh_U5jZVqNJzIF1lf7wmS3Op9ZJD6OZaRrzL9kFM"/></div>

Below we see the value now being moved into __s0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQFIXNMmWUZv2A/article-inline_image-shrink_1000_1488/0/1521196439893?e=1614211200&amp;v=beta&amp;t=8iQ2SdDL1hqmi28FhXsXGym1Vu6wOH7iTJGK2nsz2ug"/></div>

Next week we will dive into Hacking Float Variables.