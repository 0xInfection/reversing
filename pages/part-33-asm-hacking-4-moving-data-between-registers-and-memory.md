## Part 33 - ASM Hacking 4 \[Moving Data Between Registers And Memory\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine the source code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520234729924.jpg"/></div>

We again can see above that we will move the immediate value of 777 decimal into EAX. We then move that value stored in EAX into the constant value in memory which initially had the value of 10 decimal at runtime. Keep in mind we could have called the value anything however I called it constant as it was set up as a constant in the .data section.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520242560352.jpg"/></div>

As you can see above we go into GDB and clearly see that the value of constant has been replaced with 777 decimal where in the code it was clearly set at 10 decimal in line 6 of the code at the beginning of this tutorial.

We can clearly see that in line 16 of the code the value of 777 decimal was successfully moved into EAX and into the memory value of constant.

Now lets hack this thing!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520174080965.jpg"/></div>

We took the very steps as we did last time with the debugging lesson. Here we hack the value of constant to which we hack the value from 777 to 666.

I look forward to seeing you all next week when we dive into creating our fifth assembly program!