# Part 31 – Hacking Float Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 1337.1;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEZRad58-KHSw/article-inline_image-shrink_1000_1488/0/1521799049547?e=1614211200&amp;v=beta&amp;t=87pvQJDDfSo_RScfiDFHdEtVk3_eMoiY3fnJk6kcEYQ"/></div>

Let’s review last week’s tutorial.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQES3QRrE1zTFQ/article-inline_image-shrink_1000_1488/0/1521799097861?e=1614211200&amp;v=beta&amp;t=x96xvQAgyek-64icyPN5GBBwJV1JsYCcLoO4ImstJFU"/></div>

Let’s break on __main+20__ and continue to that point.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEa1tu_UEQ2Hg/article-inline_image-shrink_1000_1488/0/1521799125882?e=1614211200&amp;v=beta&amp;t=syEPLG5WYSLlyt0vSSC5knbrVBULQXiWqna8aHamLKI"/></div>

Let’s examine what value is inside __r11-8__.&nbsp;We clearly see it is __1337.09998__ which approximates our value in our original c++ code.&nbsp;Keep in mind a float has roughly 7 decimal digits of precision and that is why we do not see __1337.1__ so please remember that as we go forward.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEg5_6DOSJBuA/article-inline_image-shrink_1000_1488/0/1521799166328?e=1614211200&amp;v=beta&amp;t=SmxUOg6Gvqjd-NGcq0TtxRkIYcOZAmYv2V49JQ0CmVQ"/></div>

We can also see this value in high memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF3sRIMVARPXQ/article-inline_image-shrink_1000_1488/0/1521799204709?e=1614211200&amp;v=beta&amp;t=zyo6X677S8OdIXRd72GP_QfpOdCVBqI_hY5VGiZUFCg"/></div>

Let’s break on __main+28__ and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEWhvmXMw5DAw/article-inline_image-shrink_1000_1488/0/1521799242840?e=1614211200&amp;v=beta&amp;t=CJD_jAhFByXmtiWq7lH3io1HOL8k-9NKtf7mguCjtVM"/></div>

We see a strange new instruction.&nbsp;We see __vldr__ and the value within __r11, \#8__ being moved into__ s0__.&nbsp;So what is __s0__?&nbsp;We have a math co-processor which has a series of additional registers that work with decimal or floating-point numbers.&nbsp;Here we see an example of such to which the value of __1337.09998 __is being moved into __s0__.&nbsp;The __vldr__ instruction loads a constant value into every element of a single-precision or double-precision register such as__ s0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFsNZMexdd8yg/article-inline_image-shrink_1000_1488/0/1521799279756?e=1614211200&amp;v=beta&amp;t=RVWgvwyLICipNXQTCjgCQDXxD4BpveCvlF31ZXbyJNk"/></div>

We can only see these special registers if we do a info registers all command as we do below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGe7H7kTXHOTg/article-inline_image-shrink_1000_1488/0/1521799307421?e=1614211200&amp;v=beta&amp;t=Yew3wybf-AOjX3_r8wV-PECqioPdQTSdrS8K_AbbV8s"/></div>

Below we see the value now being moved into __s0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGxpvOHpzuhWQ/article-inline_image-shrink_1000_1488/0/1521799331767?e=1614211200&amp;v=beta&amp;t=C63jbySwMwNn1t_bElv2MYP1fLlOlLl4OWWy29vMqAI"/></div>

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF5koEdhSnLvg/article-inline_image-shrink_1000_1488/0/1521799362535?e=1614211200&amp;v=beta&amp;t=fsreQ6HTH-jy2IiyBi9a6CsCsawzSv9kysTpJTxLJeg"/></div>

Let’s now look at the registers and see what has transpired.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEPBsCYZygZpA/article-inline_image-shrink_1000_1488/0/1521799386349?e=1614211200&amp;v=beta&amp;t=QXhSEItu85cn3zzcFZMlwvgoo7a8Zs_PgZBnxyR4-7o"/></div>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF3fuShD-SosQ/article-inline_image-shrink_1000_1488/0/1521799407513?e=1614211200&amp;v=beta&amp;t=Ulx1HQbN7_6780oKJwAyKChjAoxQGD853RN2IbbpB98"/></div>

As you can see we have hacked the value (less the precision issue of the float variable accurate up to 6 decimal places)!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGDSlHn23_aEQ/article-inline_image-shrink_1000_1488/0/1521799441419?e=1614211200&amp;v=beta&amp;t=wkUxDMKbDvQfnDSLVZzDfrFQ6G5MzDYs6Pd1Vx7D-Ww"/></div>

Finally as we continue we see our hacked value echoed back out to the terminal when the c++ __cout __function executes.

Next week we will dive into Double Variables.