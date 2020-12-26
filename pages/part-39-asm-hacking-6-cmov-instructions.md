# Part 39 - ASM Hacking 6 \[CMOV Instructions\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s bring the binary into gdb.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520490808741.jpg"/></div>

Let’s now run the binary. We see that the smallest value is 7 which is expected. Our final bit of instruction in this tutorial will teach you how to jump to any part of the execution that you so choose.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520241582923.jpg"/></div>

We __set $eip = 0x080480dd__ which is the exit routine. We see now that it bypasses all of the code from the nop instruction when we broke on \_start. You now can use this command to jump anywhere inside of any binary within the debugger.

I look forward to seeing you all next week when we wrap up our tutorial series.