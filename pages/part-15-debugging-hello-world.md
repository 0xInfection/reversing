# Part 15 - Debugging Hello World

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code from last week.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHCoWLpKrStnA/article-inline_image-shrink_1000_1488/0/1520191246374?e=1614211200&amp;v=beta&amp;t=BP5WkWSTpfH5TcIZuXBPpUM5Ab9OGo-4WqRyGfdkLOE"/></div>

Let’s debug!&nbsp;Let’s fire up GDB which is the GNU Debugger to which we will break down the C++ binary and step through it line-by-line in ARM Assembly.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGZYAS71PhOrA/article-inline_image-shrink_1000_1488/0/1520232284963?e=1614211200&amp;v=beta&amp;t=U1SQd5BzTIvmWnXa3Sd2JyjepUFEl3hE-XrPeDXUHQw"/></div>

This is the ARM disassembly that we are seeing.&nbsp;No matter what language you program in, it ultimately will go down to this level.&nbsp;

This might be a bit scary to you if you did not take my prior course on ARM Assembly.&nbsp;If you need to do a refresher, please link back to that series.

You are probably asking yourself why we are not debugging with the original source code and seeing how it matches nicely to the assembly.&nbsp;The answer is when you are a professional Reverse Engineer, you do not get the luxury of seeing source code when you are reversing binaries.&nbsp;

This is a childishly simple example and we will continue through the series with very simple examples so that you can learn effective techniques.&nbsp;We are using a text-based debugger here so that you fully understand what is going on and to also get some training if you had to ever attach yourself to a running process inside a foreign machine you will know how to properly debug or hack.

I will focus SOLELY on this method rather than using a nice graphical debugger like IDA or the like so that you are able to manipulate at a very low-level.

We start with loading the link register into __r11 __and adding __4__ to the stack pointer and then adding it to __r11__.&nbsp;This is simply a routine which will allow the binary to preserve the link register and setting up space on the stack.

We notice memory address __0x10750__ being loaded from memory to the register __r1__.&nbsp;Let’s do a string examination and see what is located at that address.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHnETV_0INvVA/article-inline_image-shrink_1000_1488/0/1520233136878?e=1614211200&amp;v=beta&amp;t=tzr4mmZqWAg6ddbO7s36naU0EV9Q2uqkAhcD7i55ZXg"/></div>

Voila!&nbsp;We see our string. __“Hello World!”__ located at that memory address.&nbsp;

Let’s set a breakpoint at __main+16.__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHqVRmT-mgyAg/article-inline_image-shrink_1000_1488/0/1520202291983?e=1614211200&amp;v=beta&amp;t=p0w9sg_Fq0HSvqEM0i4pRYDfscvcCVXQ7mza3l8on2w"/></div>

Let’s take a look at our register values.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGSf1zMtjTwsg/article-inline_image-shrink_1000_1488/0/1520193660539?e=1614211200&amp;v=beta&amp;t=VJzC0kMuj08Y9ShtRL5S5qKqCwlzhMhdMoZRmInP9HA"/></div>

Let’s now take a look at what is inside the __r1__ register and then step through the binary.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHBFli6ZrFnyw/article-inline_image-shrink_1000_1488/0/1520235567544?e=1614211200&amp;v=beta&amp;t=lFukOryYGs2ZXhUAqTbfeoYrMmJ_LrewrtYFjV08SPI"/></div>

We see the __“Hello World!”__ string now residing inside of __r1__ which resides at memory address __0x10848__.&nbsp;Finally let’s continue through the binary.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQERpBfgmUg0hQ/article-inline_image-shrink_1000_1488/0/1520190662835?e=1614211200&amp;v=beta&amp;t=jBIGsHFYMFEexcg6LT2gFwsV5VDn1WqH-lwzbl-ew1Y"/></div>

Understanding assembly and step-by-step debugging allows you to have complete and ultimate control over any binary!&nbsp;More complex binaries can cause you hours, days or weeks to truly Reverse Engineer however the techniques are the same just more time consuming.

Reverse Engineering is the most sophisticated form of analysis in advanced Computer Engineering.&nbsp;There are many tools that a professional Reverse Engineer uses however each of those tools have a usage and purpose however this technique is the most sophisticated and comprehensive.

Next week we will dive into Hacking Hello World.