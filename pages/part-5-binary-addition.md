## Part 5 - Binary Addition

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Binary addition can occur in one of four different fashions:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1536919520880.jpg"/></div>

Keep in mind the (1) means a carry bit. It very simply means an overflow.

Lets take the following 4-bit nibble example:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1536919547320.jpg"/></div>

We see an obvious carry in the 3rd bit. If the 8th bit had a carry then this would generate a carry flag within the CPU.

Let’s examine an 8-bit number:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1536919574450.jpg"/></div>

If we had:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1536919592305.jpg"/></div>

Here we see a carry bit which would trigger the carry flag within the CPU to be 1 or true. We will discuss the carry flag in later tutorials. Please just keep in mind this example to reference as it is very important to understand.

Next week we will dive into binary subtraction! Stay tuned!