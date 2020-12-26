# Part 28 - x64 Assembly \[Part 2\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we continue our tutorial with a simple subtract example. Let's examine the source code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1043372078.jpg"/></div>

Let's compile and run the debugger:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/399633186.jpg"/></div>

Let's run and disassemble:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/993234925.jpg"/></div>

As we can see very we load __16__ or __0x10__ hex into __EAX__ and then subtract __5__ from it in the next instruction.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/158987666.jpg"/></div>

We step twice and then look at the resulting value in __RAX__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/828803848.jpg"/></div>

As we can see the result is 0xb hex or 11 decimal as expected. It is important that you try these simple examples to get a grasp of what happens when we start to debug C++ code in future tutorials.