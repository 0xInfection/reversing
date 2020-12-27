## Part 32 - x64 Assembly \[Part 6\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's review our code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248751760.jpg"/></div>

Compile...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248766003.jpg"/></div>

Debug...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248783477.jpg"/></div>

Let's evaluate what is inside the memory address of 0x6000d8.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248844375.jpg"/></div>

As we can see "__Hello World__" with the return character will then be moved into our __RSI__ register.

Next week we will examine this a bit closer.