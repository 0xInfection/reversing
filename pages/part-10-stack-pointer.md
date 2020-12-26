# Part 10 - Stack Pointer

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The Stack is an abstract data type to which is a LIFO (Last In First Out).&nbsp;When we push a value onto the stack it goes into the Stack Pointer and when it is popped off of the stack it pops the value off of the stack and into a register of your choosing.

CODE TIME! Again, don’t be discouraged if you don’t understand everything in the code example here.&nbsp;It will become clear over the next few lessons.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHF6NDjdFFkWg/article-inline_image-shrink_1000_1488/0/1520149187367?e=1614211200&amp;v=beta&amp;t=tmkcRd7PKv1Q4GDziax5f5jAXVbaeKRikhsg337Y5DY"/></div>

To compile:

<pre spellcheck="false">as -o sp_demo.o sp_demo.s

ld -o sp_demo sp_demo.o
</pre>

Once again lets load the binary into GDB to see what is happening.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHUcXsY1X1hdQ/article-inline_image-shrink_1000_1488/0/1520209893418?e=1614211200&amp;v=beta&amp;t=ZufIijqOCdAkWBS5AhLTHmPP5Or57oZcs1ae-NNlwOQ"/></div>

Lets step into one time.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEDXzNHL0qSJw/article-inline_image-shrink_1000_1488/0/1520232603248?e=1614211200&amp;v=beta&amp;t=zZ-Ow2aI61-eT6qZ7S2e1LAXbkM1BoHmKOdJawi92Ik"/></div>

We see __hex 30__ or __48 decimal__ moved into __r7__.&nbsp;Lets step into again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHAO3eI2pxvRg/article-inline_image-shrink_1000_1488/0/1520238832288?e=1614211200&amp;v=beta&amp;t=PtjUak60uUwP3Xx2lH-mD8Ua9akoQ9lgxxvTxBRL2ZA"/></div>

We see the value of the __sp__ change from __0x7efff3a0__ to __0xefff39c__.&nbsp;That is a movement backward __4 bytes__.&nbsp;Why the heck is the stack pointer going backward you may ask!

The answer revolves around the fact that the stack grows __DOWNWARD__.&nbsp;When we say the top of the stack you can imagine a series of plates being placed __BENEATH__ of each other.

Originally the __sp__ was at __0x7efff3a0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGk-AQVLwT47g/article-inline_image-shrink_1000_1488/0/1520218097215?e=1614211200&amp;v=beta&amp;t=cjzwF9bIQJ4y30gLhExwdZl_XjlKYo2UMotEuUIpO4c"/></div>

When we pushed __r7__ onto the stack, the new value of the __Stack Pointer__ is now __0x7efff39c__ so we can see the Stack truly grows __DOWNWARD__ in memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE9USjiBS22Dw/article-inline_image-shrink_1000_1488/0/1520239285552?e=1614211200&amp;v=beta&amp;t=2WxZjLaP11OGwI0r8RlSsmeDj3OE6bsKyF_siIBxYSs"/></div>

Now lets step into again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE-tIYlBxJojQ/article-inline_image-shrink_1000_1488/0/1520143279567?e=1614211200&amp;v=beta&amp;t=UuUIo2c8Cb629giyBGgjQwlYxaQ3zFp_-CE-bm0BxsU"/></div>

We can see the value of __hex 10__ or __decimal 16__ moved into __r7__.&nbsp;Notice the __sp__ did not change.

Before we step into again, lets look at the value inside the __sp__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEVMeFVwK6yUw/article-inline_image-shrink_1000_1488/0/1520216970660?e=1614211200&amp;v=beta&amp;t=GgjQDq2hKPxpnU6TBFcPhDRr5hq8YM67pVvQXYtEzC8"/></div>

Lets step into again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFxltd6ZKGHlA/article-inline_image-shrink_1000_1488/0/1520233070958?e=1614211200&amp;v=beta&amp;t=6_tUIfQUeauhHObA0oAvnCxf0H_JH94A00P9GMaTBuo"/></div>

We see the value in the stack was popped off the stack and put back into __r7__ therefore the value of __hex 30__ is back in __r7__ as well as the __sp__ is back at __0x73fff3a0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGFQkyMfVuY6A/article-inline_image-shrink_1000_1488/0/1520232081853?e=1614211200&amp;v=beta&amp;t=yeKZSWGTmOM_eE6GBJdnLagJ5x7piX8ndtk_DcIC7Js"/></div>

Please take the time to type out the code, compile and link it and then step through the binary in GDB.&nbsp;Stack operations are critical to understanding Reverse Engineering and Malware Analysis as well as any debugging of any kind.

Next week we will dive into ARM Firmware Boot Procedures.