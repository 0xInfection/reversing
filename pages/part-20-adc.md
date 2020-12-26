# Part 20 – ADC

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

ADC is the same as ADD except it adds a 1 if the carry flag is set. We need to pay particular attention to the CPSR or Status Register when we work with ADC.

Let’s look at an example to illustrate:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEaZCw2691u5A/article-inline_image-shrink_1000_1488/0/1520238027219?e=1614211200&amp;v=beta&amp;t=a96_9zHSyvjCrHt8mp40-3wW3ZvP4NbYwhGIpLdRfII"/></div>

We __add__ __100__ decimal into __r1__, __4,294,967,295__ into __r2__, __100__ decimal into __r3__ and __100__ decimal into __r4__. We then __add r1__ and __r2__ and place in __r0__ and then __add r3__ and __r4__ and place into __r5__.

We see __adds __which sets the flags in the CPSR. We have to once again remember when we debug in GDB, the value of the CPSR is in hex. In order to see what flags are set, we must convert the hex to binary. This will make sense as we start to debug and hack this example in the coming tutorials.

You can compile the above by:

<pre spellcheck="false">as -o adc.o adc.s
ld -o adc adc.o
</pre>

I want you to ask yourself what is going to happen when __r3(100 decimal)__ is added to __r4(100 decimal)__? What do you think the value of __r5__ will be with the above example of setting the flags with the adds result? Think about the first sentence in this tutorial and keep this in mind for the next tutorial.

Next week we will dive into Debugging ADC.