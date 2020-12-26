# Part 17 - ADDS

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

ADDS is the same as ADD except it sets the flags accordingly in the CPSR.

Let’s look at an example to illustrate:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/537393655.jpg"/></div>

We __add__ __100__ decimal into __r1__, __4,294,967,295__ into __r2__. We then __add r1__ and __r2__ and place in __r0.__

We see __adds __which sets the flags in the CPSR. We have to remember when we debug in GDB, the value of the CPSR is in hex. In order to see what flags are set, we must convert the hex to binary. This will make sense as we start to debug and hack this example in the coming tutorials.

You can compile the above by:

<pre spellcheck="false">as -o adc.o adc.s
ld -o adc adc.o
</pre>

We need to remember that bits 31, 20, 29 and 28 in the CPSR indicate the following:

__bit 31 - N = Negative Flag__

__bit 30 - Z = Zero Flag__

__bit 29 - C = Carry Flag__

__bit 28 - V = Overflow Flag__

Therefore if the value in binary was __0110__ of bit 31, 30, 29 and 28 (__NZCV__) that would mean:

__Negative Flag NOT Set__

__Zero Flag SET__

__Carry Flag SET__

__Overflow Flag NOT Set __

It is critical that you compile, debug and hack each exercise in order to understand what is going on here.

Next week we will dive into Debugging ADDS.