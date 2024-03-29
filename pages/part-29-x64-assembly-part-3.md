## Part 29 - x64 Assembly \[Part 3\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we continue our tutorial with a simple subtract example. Let's examine the source code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437589689.jpg"/></div>

Let's compile and run the debugger:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437628625.jpg"/></div>

Let's run and disassemble:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437662831.jpg"/></div>

As we can see very we load __16__ or __0x10__ hex into __EAX__ and then subtract __5__ from it in the next instruction.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437723578.jpg"/></div>

We step twice and then look at the resulting value in __RAX__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1551437759416.jpg"/></div>

As we can see the result is 0xb hex or 11 decimal as expected. It is important that you try these simple examples to get a grasp of what happens when we start to debug C++ code in future tutorials.