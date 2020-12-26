# Part 29 - ASM Debugging 3 \[Moving Data Between Memory And Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s debug!&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520241537282.jpg"/></div>

Specifically we will move the value of inside the constant integer of 10 decimal into ECX.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520590508110.jpg"/></div>

We open GDB in quiet mode and break on \_start and run by following the commands above.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520193652626.jpg"/></div>

As we can see when we info registers the value of ECX is 0.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520590507589.jpg"/></div>

After we step into twice, we now see the value of ECX as 10 decimal of 0xa hex.

I look forward to seeing you all next week when we dive into hacking our third assembly program!