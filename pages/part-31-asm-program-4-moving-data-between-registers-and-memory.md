## Part 31 - ASM Program 4 \[Moving Data Between Registers And Memory\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our fourth program we will demonstrate how we can move data between registers and memory.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520625191381.jpg"/></div>

Specifically we will move the immediate value of 777 decimal into EAX. We then move that value stored in EAX into the constant value in memory which initially had the value of 10 decimal at runtime. Keep in mind we could have called the value anything however I called it constant as it was set up as a constant in the .data section.

You can clearly see it can be manipulated so it is NOT a constant. I chose constant deliberately as if it was in pure form the value would stay 10 decimal or 0xa hex.

This code is purely an academic exercise as variable data normally would be set up under the .bss section however I wanted to demonstrate that the above is possible to show the absolute flexibility of assembly language.

Keep in mind to assemble we type:

__as –32 -o moving\_data\_between\_registers\_and\_memory.o moving\_data\_between\_registers\_and\_memory.s__

To link the object file we type:

__ld -m elf\_i386 -o moving\_data\_between\_registers\_and\_memory moving\_data\_between\_registers\_and\_memory.o __

I look forward to seeing you all next week when we dive into debugging our fourth assembly program!