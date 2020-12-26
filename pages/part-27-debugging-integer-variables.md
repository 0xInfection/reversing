# Part 27 – Debugging Integer Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code.&nbsp;I again want to include the below information from last week’s lesson to emphasize what is going on regarding integers.

A 32-bit register can store 2^32 different values. The range of integer values that can be stored in 32 bits depends on the integer representation used. With the two most common representations, the range is 0 through 4,294,967,295 (2^32 − 1) for representation as an (unsigned) binary number, and −2,147,483,648 (−2^31) through 2,147,483,647 (2^31 − 1) for representation as two's complement.

Keep in mind with 32-bit memory addresses you can directly access a maximum of 4 GB of byte-addressable memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520217390524.jpg"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520233314454.jpg"/></div>

We see at __main+12 __the address at __0x10730 __loading data into __r3__.&nbsp;Let’s take a closer look.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520192010424.jpg"/></div>

When we examine the data inside __0x10730__ we clearly see the integer __777__ present.&nbsp;When we continue we see __777 __echoed back to the terminal which makes sense as we utilized the __cout__ function within c++.\#linux \#arm \#asm \#cplusplus \#reverseengineering

Next week we will dive into Hacking Integer Variables.