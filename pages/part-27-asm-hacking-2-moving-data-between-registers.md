## Part 27 - ASM Hacking 2 \[Moving Data Between Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s hack the second program below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520583727180.jpg"/></div>

Lets fire up GDB and break on \_start, run the binary and disas:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520066773312.jpg"/></div>

Now lets __si__ twice and __i r__:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143945686.jpg"/></div>

As we can see the value of __0x16__ or __22__ decimal did move into EDX successfully. This is what we did in the last lesson however here we are going to hack that value to something else.

We can __set $edx = 0x19__ for example:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520583727155.jpg"/></div>

As you can see we easily hacked the value of __EDX__ to __0x19__ or __25__ decimal.

Hopefully you see some very simple patterns now that we are diving into very simple assembly language programs. The key is to understand how to manipulate values and instructions so that you have complete control over the binary.

We are going to continue to move at a snails pace throughout the rest of this tutorial as my goal is to give everyone very small bite-size examples of how to understand x86 assembly.

I look forward to seeing you all next week when we dive into writing our third assembly program!