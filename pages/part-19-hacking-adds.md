# Part 19 – Hacking ADDS

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s once again re-examine our code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520215587042.jpg"/></div>

We again __add__ __100__ decimal into __r1__, __4,294,967,295__ into __r2__. We then __add r1__ and __r2__ and place in __r0.__

Lets debug:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520594576879.jpg"/></div>

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

Lets take a look if we step again:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149286284.jpg"/></div>

We see __4294967295 decimal__ or __0xffffffff __in __r2__. We know if we step again we will cause the CPSR to change from 0001 to 0010 which means:

The value in binary is __0010__ of bit 31, 30, 29 and 28 (__NZCV__) that would mean:

__Negative Flag NOT Set__

__Zero Flag NOT SET__

__Carry Flag SET__

__Overflow Flag NOT Set__

This action sets the carry flag. However lets hack:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520147275008.jpg"/></div>

We hacked __r2__ and changed the value to __1 decimal __and__ 0x1 hex__. NOW we know before the__ CPSR __went to __0010__ last time however now that we hacked this, lets see what happens to the __CPSR__ when we step.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520211562604.jpg"/></div>

BAM! We hacked it and see__ r0 __is __101__ and therefore did NOT trigger the carry flag and kept the __CPSR__ at__ 0x10 hex __which means __0001 binary __which means:

Therefore if the value in binary was __0001__ of bit 31, 30, 29 and 28 (__NZCV__) that would mean:

__Negative Flag NOT Set__

__Zero Flag NOT SET__

__Carry Flag NOT SET__

__Overflow Flag Set __

It is so important that you understand this lesson in its entirety. If not, please review the last two weeks lessons.

Next week we will dive into ADC.

  