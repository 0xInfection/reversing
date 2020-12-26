# Part 30 - ASM Hacking 3 \[Moving Data Between Memory And Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s hack!&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520588657073.jpg"/></div>

Specifically we will move the value of inside the constant integer of 10 decimal into ECX like before.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520171419386.jpg"/></div>

We open GDB in quiet mode and break on \_start and run by following the commands above.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520145740732.jpg"/></div>

As we can see when we info registers the value of ECX is 0. Let’s do a si and another si.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520198737146.jpg"/></div>

As you can see the value of ECX is 10 decimal or 0xa hex as it was in the prior lesson now lets hack that value to something else.

Let’s __set $ecx = 1337 __and do an i r.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520588657130.jpg"/></div>

As you can clearly see we have hacked the value of ECX to 0x539 hex or 1337 decimal.

As I have stated throughout this series. Each of these lessons are very bite-sized examples so that you get the hard muscle memory on how to hack through a variety of situations so that you ultimately have a complete mastery of processor control.

I look forward to seeing you all next week when we dive into creating our fourth assembly program!