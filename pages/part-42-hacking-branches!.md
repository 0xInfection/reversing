# Part 42 - Hacking Branches!

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

We are at the end of the road. This is the final video in the x64 series. The final topic is that of pointers.

What are pointers? Let us start with an example.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567286671465.jpg"/></div>

A pointer is nothing more than a memory address. When we compile we will clearly see where lottery\_number lives in mapped memory (this is a running example unlike our unmapped Radare examples).

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567286745307.jpg"/></div>

Let's add a true pointer to the example:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567287725406.jpg"/></div>

We see the same value:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567287787090.jpg"/></div>

Let us experiment more:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567288396508.jpg"/></div>

We see the pointer address point to a new address:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567288456995.jpg"/></div>

Remember pointers are memory addresses of other variables. Let's look at it another way:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289354121.jpg"/></div>

Let us compile:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289368216.jpg"/></div>

We deference by doing the following:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289646596.jpg"/></div>

Then we compile:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289657671.jpg"/></div>

We can see the deference pointer is equal to 777.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290644015.jpg"/></div>

We can see the example with an array:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290665083.jpg"/></div>

Let's debug:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290786481.jpg"/></div>

Then we disassemble:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290800965.jpg"/></div>

Let's hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292294462.jpg"/></div>

Let's re-examine the binary:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292311387.jpg"/></div>

We can see we hacked the value of 3 with 6.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292376880.jpg"/></div>

We can see we have made the successful hack.

I hope over the years through the literal hundreds of x86, ARM and x64 tutorials you have a basic knowledge of how to do GOOD to protect critical infrastructures from malicious hands by understanding how the enemy works. Go and do GOOD work!

  