# Part 34 – Hacking Double Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code.

<pre spellcheck="false">int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; double myNumber = 1337.77;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/927948278.jpg"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/854533091.jpg"/></div>

Let’s set a breakpoint at __main+24__ and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/490853933.jpg"/></div>

We see the __strd r2, \[r11, \#-12\]__ and we have to fully understand that this means we are storing the value at the offset of __-12__ from register __r11__ into __r2__.&nbsp;Let’s now examine what exactly resides there.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1012184437.jpg"/></div>

Voila!&nbsp;We see __1337.77__ at that offset location or specifically stored into __0x7efff230__ in memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1038709324.jpg"/></div>

Let’s step into twice which executes the __vldr d0, \[r11, \#-12\]__ as we understand that __1337.77__ will now be loaded into the double precision math coprocessor __d0 __register.&nbsp;Let’s now print the value at that location below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/270669655.jpg"/></div>

Let’s hack the __d0__ register!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1029172940.jpg"/></div>

Now let’s reexamine the value inside __d0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/760356558.jpg"/></div>

Let’s continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/534946050.jpg"/></div>

Successfully hacked!

Next week we will dive into the SizeOf Operator.