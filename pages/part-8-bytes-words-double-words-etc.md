## Part 8 - Bytes, Words, Double Words, etc...

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Memory is measured in bytes. A byte is 8 bits. Two bytes are called a word and two words are called a double word which is four bytes (32-bit) and a quad word is eight bytes (64-bit).

A byte is 8 bits and is 2^8 power which is 256. The number of binary numbers 8 bits in size is one of 256 values starting at 0 and going to 255.

Every byte of memory in a computer has its own unique address. Let's review the disassembled instructions for a simple hello world application in Linux by setting a breakpoint on the main function. We will use the GDB debugger:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520519299095.jpg"/></div>

Don't worry if this does not make sense yet. The point of utilizing this example is to give you a sneak peek into our first program that we will examine in addition to learning about memory in a computer.

Below is an examination of the ESP register. Again, it is not critical that you understand what a register is or what ESP does. We simply want to see what a memory location looks like:

![](/imgs/1520519298916.jpg)&nbsp;

We see the memory location of 0xffffd040 which of course is in hexadecimal. We also see the value inside the ESP register which is 0xf7fac3dc which is also in hexadecimal.

It is important to understand that 0xffffd040 is 4 bytes and is a double word. As we learned in Part 6: Hexadecimal Number System, each hexadecimal digit is 4 bits long otherwise called a nibble. In 0xffffd040, lets look at the right most digit of 0. In this example, 0 (hexadecimal) is 4 bits long. If we look at 40 (in hexadecimal), we see that is a byte in length or 8 bits long. If we look at d040, we have two bytes or a word in length. Finally, ffffd040 is a double word or 4 bytes in length which is 32-bits long. The 0x at the beginning of the address just designates that is is a hexadecimal value.

A computer program is nothing more than machine instructions stored in memory. A 32-bit CPU fetches a double word from a memory address. A double word is 4 bytes in a row which is read from memory and loaded into the CPU. As soon as it finishes executing, the CPU fetches the next machine instruction in memory from the instruction pointer.

Those of you new to assembly have now had your first look. Don't get discouraged or frustrated if you do not know what is going on here. We will take our time and go through dozens of examples to break down each step in future lessons. What is important is that you take your time and examine what each lesson is discussing. Please always feel free to comment below with any questions.

In our next tutorial we will discuss the basics of x86 Architecture.