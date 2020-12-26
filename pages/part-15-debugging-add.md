# Part 15 - Debugging ADD

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our ADD example below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520244359354.jpg"/></div>

Again we see that we move decimal __67__ into __r1__ and decimal __53__ into __r2__. We then __add r1 __and __r2__ and put the result into __r0__.

Let’s compile:

__as -o add.o add.s__

__ld -o add add.o__

Let’s bring into GDB to debug:

__gdb -q add__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520594706178.jpg"/></div>

We can see that when we b__ \_start__, break on start and __r__, run we see the disassembly. If you do an __i r__ we see the info registers where we notice our __cpsr__ is __0x10__.

As we step again and info registers:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520213487826.jpg"/></div>

We notice __0x43__ hex or __67__ decimal into __r1__. We also notice that the flags are unchanged (__cpsr 0x10__).

Let’s step again and info registers:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520594706126.jpg"/></div>

We can see __r0 __now holds __0x78__ hex or __120__ decimal. We successfully saw the add instruction in place and we again notice that the flags register (__cpsr__) remains unchanged by this operation.

Next week we will dive into Hacking ADD.

  