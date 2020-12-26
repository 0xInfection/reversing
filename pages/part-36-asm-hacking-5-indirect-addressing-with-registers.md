# Part 36 - ASM Hacking 5 \[Indirect Addressing With Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s reexamine the source once more.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520173944761.jpg"/></div>

Let’s once again load the binary into GDB and break on \_start.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520175535307.jpg"/></div>

As we look above we see the command print \*0x804909e. We see that it yields a value of 5 decimal. The binary at runtime puts the values inside the constants label to a respective memory address.

In this case we see that the pointer to 0x804909e or \*0x804909e holds 5 decimal as we have stated above. An integer holds 4 bytes of data. The next value in our array will be stored in 0x80490a2. This memory location will hold the value of 8.

If we were to continue to advance through the array we would move 4 bytes to the next value and so forth. Remember each memory location in x86 32-bit assembly holds 4 bytes of data.

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520450492026.jpg"/></div>

After we broke on \_start and ran, we examined the array like we did in our prior lesson. Here we hack the value at 0x80490a2 to 66 decimal instead of 8 decimal and we can see that we successfully changed one element of the array.

This lesson is very important to understand how arrays are ultimately stored in memory and how to manipulate and hack them. If you have any questions, please leave them in the comments below.

I look forward to seeing you all next week when we dive into programming our sixth assembly program!