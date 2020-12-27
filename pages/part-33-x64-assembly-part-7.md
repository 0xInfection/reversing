## Part 33 - x64 Assembly \[Part 7\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's again review our source code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853169947.jpg"/></div>

Let's compile...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853185424.jpg"/></div>

As we have seen before it produces our string.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853213341.jpg"/></div>

We debug and see the string being moved into __0x6000d8__ and then __RSI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853259407.jpg"/></div>

Just to verify we can see the string at the aforementioned address. NOW FOR A BIT OF FUN :)...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853296959.jpg"/></div>

Here we demonstrate we have the power to simply hack and redefine the string in memory. We are simply setting a char byte length and setting a new string.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853373225.jpg"/></div>

As we can see we have successfully altered the string in memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853413835.jpg"/></div>

We continue and run through the binary and see that our hack continues through __RSI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553853461475.jpg"/></div>

Finally we see when we run the binary we have successfully hacked it's operation. This is a very simple example however shows the power of truly understanding assembly at this level. GUI debugger tools will also provide this functionality however I like to use the command line tools so that they could be used on every environment.

The purpose of these tools is to UNDERSTAND how this is done and what to look for when you are professionally reversing in real-time. You need to understand how an attacker can alter memory and/or instructions. We need more professional RE's to help defend infrastructures throughout the world and hopefully these tutorials motivate you toward a career in such.