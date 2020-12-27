## Part 26 - ASM Debugging 2 \[Moving Data Between Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s debug the second program below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143823093.jpg"/></div>

Lets fire up GDB and break on \_start, run the binary and disas:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520559684472.jpg"/></div>

Now lets __si__ twice and __i r__:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520203219432.jpg"/></div>

As we can see the value of __0x16__ or __22__ decimal did move into EDX successfully. Now lets __si__ again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144473531.jpg"/></div>

As you can see we have successfully moved EDX into EAX.

I look forward to seeing you all next week when we dive into hacking our second assembly program!