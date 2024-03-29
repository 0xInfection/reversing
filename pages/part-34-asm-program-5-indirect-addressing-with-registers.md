## Part 34 - ASM Program 5 \[Indirect Addressing With Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our fifth program we will demonstrate how we can manipulate indirect addressing with registers.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520086819422.jpg"/></div>

We can place more than one value in memory as indicated above. In the past, our memory location contained one single value. In the above as you can see the value of constants contains 11 separate values.

This creates a sequential series of data values placed in memory. Each data value occupies one unit of memory which is an integer or 4 bytes.

We must use an index system to determine these values as what we have created above is an array.

We will utilize the indexed memory mode where the memory address is determined by a base address, an offset address to add to the base address and the size of the data element, in our case an integer of 4 bytes and an index to determine which data element to select.

Keep in mind an array starts with index 0. Therefore in the above code we see 1 moving into edi which is the 2nd index which ultimately goes into ebx.

We will dive deeper into this in the next lesson we debug however I want you to take some time to study the code above and get a good grasp of what is going on.

Keep in mind to assemble we type:

__as –32 -o indirect\_addressing\_with\_registers.o indirect\_addressing\_with\_registers.s__

To link the object file we type:

__ld -m elf\_i386 -o indirect\_addressing\_with\_registers indirect\_addressing\_with\_registers.o __

I look forward to seeing you all next week when we dive into debugging our fifth assembly program!