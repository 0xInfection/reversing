# Part 31 - x64 Assembly \[Part 5\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's review our code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/941463313.jpg"/></div>

Compile...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/316538068.jpg"/></div>

Debug...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/809970521.jpg"/></div>

Let's evaluate what is inside the memory address of 0x6000d8.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/213749516.jpg"/></div>

As we can see "__Hello World__" with the return character will then be moved into our __RSI__ register.

Next week we will examine this a bit closer.