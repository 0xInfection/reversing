## Part 28 - ASM Program 3 \[Moving Data Between Memory And Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our third program we will demonstrate how we can move data between memory and registers.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520175192505.jpg"/></div>

Specifically we will move the value of inside the constant integer of 10 decimal into ECX.

Keep in mind to assemble we type:

__as –32 -o moving\_data\_between\_memory\_and\_registers.o moving\_data\_between\_memory\_and\_registers.s__

To link the object file we type:

__ld -m elf\_i386 -o moving\_data\_between\_memory\_and\_registers moving\_data\_between\_memory\_and\_registers.o __

I look forward to seeing you all next week when we dive into debugging our third assembly program!