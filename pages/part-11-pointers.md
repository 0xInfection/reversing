## Part 11 - Pointers

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

x64 utilizes the flat memory model to which we have one large array of addresses that exist within the processor.&nbsp;

A pointer is nothing more than the address of a specific value in memory.&nbsp;Let’s take an example:

__mov rax, 0x10__

In this example we are moving __10__ hex into the __rax __register.

To get the value inside __rax__ at __0x10,__ you would use the following syntax:

__mov rbx, word ptr \[rax\]&nbsp;__

Let’s assume the value inside memory __0x10__ was __0x20__ therefore __rax __points to the value inside __0x10__ which when you dereference by __\[rax\]__ contains__ 0x20__.&nbsp;__0x20__ is the value inside of the register __rax__.

We are moving a word value pointed inside of __rax&nbsp;__ into __rbx__.

If we do:

__mov word ptr \[rax\], 0x66__

This will put the value of __0x66__ into the memory location at __0x10__.&nbsp;We know that the value inside __0x10 __memory location was __0x20__ so therefore the new value inside the memory at __0x10__ will be __0x66.__

This can get confusing however when we get into code over the coming months this will become more apparent.&nbsp;

Next week we will dive into load effective address! Stay tuned!