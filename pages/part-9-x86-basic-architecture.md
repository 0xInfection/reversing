# Part 9: x86 Basic Architecture

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

A computer application is simply a table of machine instructions stored in memory to which the binary numbers which make up the program are unique only in the way the CPU deals with them.

The basic architecture is made up of a CPU, memory and I/O devices which are input/output devices which are all connected by a system bus as detailed below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF3eMuHKlz-GA/article-inline_image-shrink_1000_1488/0/1520249055678?e=1614211200&amp;v=beta&amp;t=s9E08qhObFSKcPCiAdvn2FqVKynwUa--2Q7LMULRLjI"/></div>

The CPU consists of 4 parts which are:

1)Control Unit - Retrieves and decodes instructions from the CPU and then storing and retrieving them to and from memory.

2)Execution Unit - Where the execution of fetching and retrieving instructions occurs.

3)Registers - Internal CPU memory locations used a temporary data storage.

4)Flags - Indicate events when execution occurs.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG_83vM3joGHw/article-inline_image-shrink_1000_1488/0/1520178351635?e=1614211200&amp;v=beta&amp;t=gf3dM8IXHTtDXRReTffZTcapRrItVMOpaEkrorcAwtc"/></div>

We will discuss 32-bit x86 so therefore a 32-bit CPU first fetches a double word (4 bytes or 32-bits in length) from a specific address in memory and is read from memory and loaded into the CPU. At this point the CPU looks at the binary pattern of bits within the double word and begins executing the procedure that the fetched machine instruction directs it to do.

Upon completion of executing an instruction, the CPU goes to memory and fetches the next machine instruction in sequence. The CPU has a register, which we will discuss registers in a future tutorial, called the EIP or instruction pointer that contains the address of the next instruction to be fetched from memory and then executed.

We can immediately see that if we controlled flow of EIP, we can alter the program to do things it was NOT intended to do. This is a popular technique upon which malware operates.

The entire fetch and execute process is tied to the system clock which is an oscillator that emits square-wave pulses at precise intervals.

In our next tutorial we will dive deeper into the IA-32 Architecture with a discussion of the General-purpose Registers.