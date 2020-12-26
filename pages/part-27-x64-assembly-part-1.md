# Part 27 - x64 Assembly \[Part 1\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's continue with another example:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/36977460.jpg"/></div>

As we can see we are moving __0x10__ into __RAX__ and adding __0x05__ into __RAX__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/559099400.jpg"/></div>

We compile and let's disassemble.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/915864110.jpg"/></div>

As you can see as expected we see our code in debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/238886684.jpg"/></div>

We step twice and then...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/862842710.jpg"/></div>

We see __0x15 __or __21__ decimal moved into __RAX__. Take the time to carefully try these very simple examples as we go forward.