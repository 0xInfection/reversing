# Part 21 – Debugging ADC

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

To recap, ADC is the same as ADD except it adds a 1 if the carry flag is set. We need to pay particular attention to the CPSR or Status Register when we work with ADC.

Let’s review our code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/809599778.jpg"/></div>

We __add__ __100__ decimal into __r1__, __4,294,967,295__ into __r2__, __100__ decimal into __r3__ and __100__ decimal into __r4__. We then __add r1__ and __r2__ and place in __r0__ and then __add r3__ and __r4__ and place into __r5__.

We see __adds __which sets the flags in the CPSR. We have to once again remember when we debug in GDB, the value of the CPSR is in hex. In order to see what flags are set, we must convert the hex to binary. This will make sense as we start to debug and hack this example in the coming tutorials.

Last week I raised a question where I wanted you to ask yourself what is going to happen when __r3(100 decimal)__ is added to __r4(100 decimal)__? What do you think the value of __r5__ will be with the above example of setting the flags with the adds result?

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/922369743.jpg"/></div>

Ok so we add __100 decimal__ and __100 decimal__ together in __r3__ and __r4__ and we get __201__ __decimal__ in __r5__! Is something broken? ADC is the same as ADD except it adds a 1 if the carry flag is set. Therefore we get the extra 1 in __r5__.

We again need to remember that bits 31, 20, 29 and 28 in the CPSR indicate the following:

__bit 31 - N = Negative Flag__

__bit 30 - Z = Zero Flag__

__bit 29 - C = Carry Flag__

__bit 28 - V = Overflow Flag__

We see the __CPSR__ at __20000010 hex__. The most significant bits of __20000010 hex__ in binary is __0010__.

Therefore if the value in binary was __0010__ of bit 31, 30, 29 and 28 (__NZCV__) that would mean:

__Negative Flag NOT Set__

__Zero Flag NOT Set__

__Carry Flag SET__

__Overflow Flag NOT Set__

As we can clearly see the carry flag was set. I hope you can digest and understand each of these very simple operations and how they have an effect on the CPSR.

Next week we will dive into Hacking ADC.