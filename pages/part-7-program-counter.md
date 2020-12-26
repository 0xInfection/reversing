# Part 7 – Program Counter

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

We will dive into the registers over the coming weeks to make sure you obtain a firm understand of their role and what they can do.

We begin with the PC or program counter. The program counter is responsible for directing the CPU to what instruction will be executed next. The PC literally holds the address of the instruction to be fetched next.

When coding you can refer to the PC as PC or R15 as register 15 is the program counter. You MUST treat it with care as you can set it wrong and crash the executable quite easily.

You can control the PC directly in code:

<pre spellcheck="false">mov r15, 0x00000000
</pre>

I would not suggest trying that as we are not in Thumb mode and that will cause a fault as you would be going to an OS area rather than designated program area.

Regarding our ARM processor, we follow the standard calling convention meaning params are passed by placing the param values into regs R0 – R3 before calling the subroutine and the subroutine returns a value by putting it in R0 before returning.

This is important to understand when we think about how execution flows when dealing with a stack operation and the link register which we will discuss in future tutorials.

When you are hacking or reversing a binary, controlling the PC is essential when you want to test for subroutine execution and learning about how the program flows in order to break it down and understand exactly what it is doing.

Next week we will dive into more information on the CPSR! Stay tuned!