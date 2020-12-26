# Part 31 - ASM Program 4 \[Moving Data Between Registers And Memory\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our fourth program we will demonstrate how we can move data between registers and memory.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF-dgqrt_Rfpw/article-inline_image-shrink_1000_1488/0/1520625191381?e=1614211200&amp;v=beta&amp;t=TT4e5i1Ae20Fb4E7BQQK4Ga3hMtlUKD0Fuv-M5Z9dsQ"/></div>

Specifically we will move the immediate value of 777 decimal into EAX. We then move that value stored in EAX into the constant value in memory which initially had the value of 10 decimal at runtime. Keep in mind we could have called the value anything however I called it constant as it was set up as a constant in the .data section.

You can clearly see it can be manipulated so it is NOT a constant. I chose constant deliberately as if it was in pure form the value would stay 10 decimal or 0xa hex.

This code is purely an academic exercise as variable data normally would be set up under the .bss section however I wanted to demonstrate that the above is possible to show the absolute flexibility of assembly language.

Keep in mind to assemble we type:

__as –32 -o moving\_data\_between\_registers\_and\_memory.o moving\_data\_between\_registers\_and\_memory.s__

To link the object file we type:

__ld -m elf\_i386 -o moving\_data\_between\_registers\_and\_memory moving\_data\_between\_registers\_and\_memory.o __

I look forward to seeing you all next week when we dive into debugging our fourth assembly program!