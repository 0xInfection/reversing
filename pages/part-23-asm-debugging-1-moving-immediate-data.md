# Part 23 - ASM Debugging 1 \[Moving Immediate Data\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s begin by loading the binary into GDB.

To load into GDB type:

__gdb -q moving\_immediate\_dat__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520242394717.jpg"/></div>

Let’s first set a breakpoint on start by typing b \_start.

We can then run the program by typing __r__.

To then begin disassembly, we simply type __disas__.

We coded a __nop__ which means no operation or 0x90 from an OPCODE perspective for proper debugging purposes which the breakpoint properly hit. This is good practice when creating assembly programs.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520193761435.jpg"/></div>

The native syntax as I have stated many times before is AT&amp;T syntax which you see above. I painfully go back and forth deliberately so that you have comfort in each however going forward I will be sticking to the AT&amp;T syntax however wanted to show you a few examples of both. I will state again that if you ever want to see Intel syntax simply type set-disassembly-flavor intel and you will have what you are looking for.

We first use the command si which means step-into to advance to the next instruction. What we see here at __\_start+0__ is you are moving the hex value of __0x64__ into __EAX__. This is simply moving decimal __100__ or as the computer sees it, hex __0x64__ into __EAX__ which demonstrates moving an immediate value into a register.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144825193.jpg"/></div>

We step-into again and then use the command i r which keep in mind has a space between them to give us information on the state of the CPU registers.&nbsp;We can see EAX now has the value of 0x64 hex or 100 decimal.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520492698882.jpg"/></div>

After we step-into again and do a __disas__, we see that we have then moved the value of __0x50__ into the __buffer__ label as can refer back to the source code from last week to see.

When dealing with non-register data, we can use the print command above as we type __print /x buffer__ and it clearly shows us that the value inside buffer is __0x50__. The __/x__ designation means show us the value in hex.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520492696905.jpg"/></div>

Consequently you can review slide 2 of this tutorial above you see at __\_start+5__ the immediate value of __0x50__ loaded into the __buffer__ label or in this case the address of __buffer__ which is __0x8049090__ and we can examine it by using the examine instruction by typing __x/xb 0x8049090__ which shows us one hex byte at that location which yields __0x50.__

We will be doing this with every program example so that we can dive into the debugging process. If there are any questions, please leave them below in the comments.

I look forward to seeing you all next week when we dive into creating our first assembly hack!