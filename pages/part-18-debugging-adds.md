# Part 18 – Debugging ADDS

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/242596009.jpg"/></div>

We again __add__ __100__ decimal into __r1__, __4,294,967,295__ into __r2__. We then __add r1__ and __r2__ and place in __r0.__

Lets debug:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/341564800.jpg"/></div>

We again see __adds __which sets the flags in the CPSR. We have to remember when we debug in GDB, the value of the CPSR is in hex. In order to see what flags are set, we must convert the hex to binary. This will make sense as we start to debug and hack this example in the coming tutorials.

We need to remember that bits 31, 20, 29 and 28 in the CPSR indicate the following:

__bit 31 - N = Negative Flag__

__bit 30 - Z = Zero Flag__

__bit 29 - C = Carry Flag__

__bit 28 - V = Overflow Flag__

We see the __CPSR__ at __10 hex__. __10 hex__ in binary is __0001__.

Therefore if the value in binary was __0001__ of bit 31, 30, 29 and 28 (__NZCV__) that would mean:

__Negative Flag NOT Set__

__Zero Flag NOT SET__

__Carry Flag NOT SET__

__Overflow Flag Set __

There is nothing in code above which set the __Overflow Flag__ however in it’s natural state upon executing this binary it is set.

Lets step through the program:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="imgs/322298656.jpg"/></div>

We see __64 hex__ or __100 decimal __moved into __r1__ as expected. No change in the __CPSR__. Lets step some more.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="imgs/1015312689.jpg"/></div>

We see the addition that transpires above and notice the value in __r0 __is __99 decimal__ after __100 decimal__ and __4294967295 decimal__ were added together. How is that possible? The answer is simple, we overflowed the 32-bit register of __r0__ from this addition.

If we examine the __CPSR__ we now see __20000010 hex__ or __0010 0000 0000 0000 0000 0000 0001 0000 binary__. We only have to focus on the most significant bits which are __0010__:

The value in binary is __0010__ of bit 31, 30, 29 and 28 (__NZCV__) that would mean:

__Negative Flag NOT Set__

__Zero Flag NOT SET__

__Carry Flag SET__

__Overflow Flag NOT Set__

We see that the __Carry Flag__ was set and the __Overflow Flag __was NOT set. Why is that?

The __Carry Flag__ is a flag set when two __unsigned numbers__ were added and the result is larger than the register where it is saved. We are dealing with a 32-bit register. We are also dealing with unsigned numbers therefore the __CF__ is set and the __OF__ was not as the __OF__ flag deals with __signed numbers__.

Next week we will dive into Hacking ADDS.