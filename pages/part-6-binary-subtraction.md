## Part 6 - Binary Subtraction

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Binary subtraction is nothing more than adding the negative value of the number to be subtracted. For example 8 + - 4, the starting point would be zero to which we move 8 points in the positive direction and then four points in the negative direction yielding a value of 4.

We represent a sign bit in binary to which bit 7 indicates the sign of number where 0 is positive and 1 is negative.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526862141.jpg"/></div>

The above would represent -2.

We utilize the concept of twos compliment which inverts each bit and then finally adding 1.

Lets example binary 2.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526884698.jpg"/></div>

Invert the bits.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526902723.jpg"/></div>

Add 1.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526921447.jpg"/></div>

Let’s examine a subtraction operation:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526940998.jpg"/></div>

So what is the (1) you may ask, that is the overflow bit. In future tutorials we will examine what we refer to as the overflow flag and carry flag.

Next week we will dive into word lengths! Stay tuned!