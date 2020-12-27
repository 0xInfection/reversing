## Part 10 - Stack Pointer

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The Stack is an abstract data type to which is a LIFO (Last In First Out).&nbsp;When we push a value onto the stack it goes into the Stack Pointer and when it is popped off of the stack it pops the value off of the stack and into a register of your choosing.

CODE TIME! Again, don’t be discouraged if you don’t understand everything in the code example here.&nbsp;It will become clear over the next few lessons.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149187367.jpg"/></div>

To compile:

<pre spellcheck="false">as -o sp_demo.o sp_demo.s

ld -o sp_demo sp_demo.o
</pre>

Once again lets load the binary into GDB to see what is happening.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520209893418.jpg"/></div>

Lets step into one time.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232603248.jpg"/></div>

We see __hex 30__ or __48 decimal__ moved into __r7__.&nbsp;Lets step into again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520238832288.jpg"/></div>

We see the value of the __sp__ change from __0x7efff3a0__ to __0xefff39c__.&nbsp;That is a movement backward __4 bytes__.&nbsp;Why the heck is the stack pointer going backward you may ask!

The answer revolves around the fact that the stack grows __DOWNWARD__.&nbsp;When we say the top of the stack you can imagine a series of plates being placed __BENEATH__ of each other.

Originally the __sp__ was at __0x7efff3a0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520218097215.jpg"/></div>

When we pushed __r7__ onto the stack, the new value of the __Stack Pointer__ is now __0x7efff39c__ so we can see the Stack truly grows __DOWNWARD__ in memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520239285552.jpg"/></div>

Now lets step into again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143279567.jpg"/></div>

We can see the value of __hex 10__ or __decimal 16__ moved into __r7__.&nbsp;Notice the __sp__ did not change.

Before we step into again, lets look at the value inside the __sp__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520216970660.jpg"/></div>

Lets step into again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520233070958.jpg"/></div>

We see the value in the stack was popped off the stack and put back into __r7__ therefore the value of __hex 30__ is back in __r7__ as well as the __sp__ is back at __0x73fff3a0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232081853.jpg"/></div>

Please take the time to type out the code, compile and link it and then step through the binary in GDB.&nbsp;Stack operations are critical to understanding Reverse Engineering and Malware Analysis as well as any debugging of any kind.

Next week we will dive into ARM Firmware Boot Procedures.