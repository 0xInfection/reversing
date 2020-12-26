# Part 41 - Hacking Variables!

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's take a look at some branching logic:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729104643.jpg"/></div>

As we can plainly see we init an int to 1 and if the variable is equal to 1 the first if statement prints a response to standard output.

Let's compile:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729192665.jpg"/></div>

Let's run:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729212374.jpg"/></div>

As we can logically see the first branch is taken. Let's take it into Radare and look around at the assembly:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729291450.jpg"/></div>

We can see the branching logic with the aqua colored arrows. At __0x0000114a__ we see our first branch being loaded into __rdi__. Take note at __0x00001148__ we see a __jne 0x1158__. At __0x00001158__ we see our second branch being loaded into __rdi__.

The __jne__ means jump if not equal. This means if what is being compared in __0x00001144__ is not equal to 1 (we see __1__ being compared to what is in __local\_4h__ which we know is pseudo code for what is actually in __rbp-0x4__. This should make sense as I went over this in detail last week if you are confused please revisit our last lesson.

To hack we simply make the __jne__ statement to __je__ which is jump if equal which we know the __cmp__ or comparison is equal so it will now branch to "__A is NOT 1!__".

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729757650.jpg"/></div>

When we exit Radare we can see we have hacked the binary successfully:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566729786175.jpg"/></div>

Stay tuned!