# Part 21 – Debugging Character Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520147096734.jpg"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520229910793.jpg"/></div>

Woah!&nbsp;This is confusing.&nbsp;I don’t see any clear memory addresses being loaded into a register to manipulate the data.&nbsp;

Let’s keep in mind that we are dealing with a single byte character variable.&nbsp;

If you remember from last week each character translates down to an ASCII code in hex which the processor understands.&nbsp;The value of __n__ is __0x6e__ hex or __110__ decimal.&nbsp;You can review any ASCII table to see where we derived this value.

We do see __0x6e__ at __main+12__ which is the character ‘__n__’.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520209360741.jpg"/></div>

If we step into a few times we notice the value has been placed into __r3__.&nbsp;When we print the value in __r3__ we now see our ‘__n__’ character.

Let’s continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149197565.jpg"/></div>

We now see the ‘__n__’ printed to the standard output as expected.

It is important that you understand this process and understand that each character translates into an ASCII value to which the processor loads directly into a respective register.&nbsp;Our previous experience we have seen a string loaded directly into a memory location and this is not the case here.

Next week we will dive into Hacking Character Variables.