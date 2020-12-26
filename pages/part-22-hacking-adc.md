# Part 22 – Hacking ADC

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

To recap again, ADC is the same as ADD except it adds a 1 if the carry flag is set. We need to pay particular attention to the CPSR or Status Register when we work with ADC.

Let’s again review our code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHymGPxTYW0Kg/article-inline_image-shrink_1000_1488/0/1520144168134?e=1614211200&amp;v=beta&amp;t=2L5ijpvvkJQGffEhz6H_7hRx4X5qWh7tXHD9z_g8q2c"/></div>

We __add__ __100__ decimal into __r1__, __4,294,967,295__ into __r2__, __100__ decimal into __r3__ and __100__ decimal into __r4__. We then __add r1__ and __r2__ and place in __r0__ and then __add r3__ and __r4__ and place into __r5__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGOSpal8OqelQ/article-inline_image-shrink_1000_1488/0/1520170920932?e=1614211200&amp;v=beta&amp;t=WmB_bSHnun78lCRPT-0fMnE9hx3BhzjI8CfnCA1Z-_I"/></div>

We run the program and step to where we move __4,294,967,295__ into __r2__. Let’s hack that value in __r2 __and change it to __100 decimal__.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGHJMoBmAoChw/article-inline_image-shrink_1000_1488/0/1520230872538?e=1614211200&amp;v=beta&amp;t=o4CrSOJYiB07IpdL5WtFVUw92PtWKA0sUYuh-rX2QFI"/></div>

Let’s step a few more times:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFIZqpM-6mBbg/article-inline_image-shrink_1000_1488/0/1520243287330?e=1614211200&amp;v=beta&amp;t=ys2i-xcTZCddfPqlaP8wlYzFtitUBYGIrXIwmuAcmcM"/></div>

Ok so now we add __100 decimal__ and __100 decimal__ together in __r3__ and __r4__ and we get __200__ __decimal__ in __r5__! Do you remember last week when we had __201__? Let’s examine the CPSR below.

We again need to remember that bits 31, 20, 29 and 28 in the CPSR indicate the following:

__bit 31 - N = Negative Flag__

__bit 30 - Z = Zero Flag__

__bit 29 - C = Carry Flag__

__bit 28 - V = Overflow Flag__

We see the __CPSR__ at __10 hex__. The most significant bits of __10 hex__ in binary is __0001__.

Therefore if the value in binary was __0001__ of bit 31, 30, 29 and 28 (__NZCV__) that would mean:

__Negative Flag NOT Set__

__Zero Flag NOT Set__

__Carry Flag NOT SET__

__Overflow Flag Set__

As we can clearly see the carry flag was NOT set. I hope you can digest and understand each of these very simple operations and how they have an effect on the CPSR. Please take the time and review last weeks lesson for comparison.

Next week we will dive into SUB.