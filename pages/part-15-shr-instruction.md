# Part 15 - SHR Instruction

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The ROL command stands for rotate left.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/87931927.jpg"/></div>

In our simple x64 example on an Ubuntu Linux machine above we see we __mov 1__ into __al __and rotate left by 1 bit.

The binary representation is __00000001b__.&nbsp;If we __ROL__ 1 bit the value simply becomes __00000010b__ as demonstrated below.

We first compile and link by:

__nasm -f elf64 -o test.o test.asm__

__ld -o test test.o__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/354440389.jpg"/></div>

We can see here in the debugger that __al __starts with __1__ and when we rotate left it goes to __10b__.

You can ROL with additional bits as well.&nbsp;The logic would remain the same as the bits will rotate left just as we demonstrated above.

Next week we will dive into ROR! Stay tuned!