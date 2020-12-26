# Part 33 – Debugging Double Variables

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008391034.jpg"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008417137.jpg"/></div>

Let’s set a breakpoint at __main+24__ and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008442868.jpg"/></div>

We see the __strd r2, \[r11, \#-12\]__ and we have to fully understand that this means we are storing the value at the offset of __-12__ from register __r11__ into __r2__.&nbsp;Let’s now examine what exactly resides there.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008470513.jpg"/></div>

Voila!&nbsp;We see __1337.77__ at that offset location or specifically stored into __0x7efff230__ in memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008491495.jpg"/></div>

Let’s step into twice which executes the __vldr d0, \[r11, \#-12\]__ as we understand that __1337.77__ will now be loaded into the double precision math co-processor __d0 __register.&nbsp;Let’s now print the value at that location below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008515533.jpg"/></div>

Finally let’s continue and watch the value echo to the terminal.&nbsp;This completes our __cout__ c++ function.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008538297.jpg"/></div>

Next week we will dive into Hacking Double Variables.