# Part 28 – Hacking Integer Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988583160.jpg"/></div>

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988510636.jpg"/></div>

Let’s take a look again inside the memory location of __0x10730__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988543593.jpg"/></div>

As we can clearly see the integer value of __777__ appears and when we continue it echoes out to the terminal the value of __777__ which corresponds with our c++ function __cout__.

Let’s hack the value inside of __0x10730__ and set the value to __666__ and then reexamine the value inside __0x10730__ and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988571825.jpg"/></div>

Success!&nbsp;As we can see we hacked the value to __666__ as we continue we see it echoed out to stdout.

Next week we will dive into Float Variables.