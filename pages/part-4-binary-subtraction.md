# Part 4 – Binary Subtraction

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Binary subtraction is nothing more than adding the negative value of the number to be subtracted. For example 8 + - 4, the starting point would be zero to which we move 8 points in the positive direction and then four points in the negative direction yielding a value of 4.

We represent a sign bit in binary to which bit 7 indicates the sign of number where 0 is positive and 1 is negative.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG30nevMsazhw/article-inline_image-shrink_1000_1488/0/1520215170654?e=1614211200&amp;v=beta&amp;t=oVIR51Ky-1MADecPdYCHvfWVl081djccZg5Z1P-B7AY"/></div>

The above would represent -2.

We utilize the concept of twos compliment which inverts each bit and then finally adding 1.

Lets&nbsp;examine binary 2.

__00000010__

Invert the bits.

__11111101__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF9y2SxkAS99A/article-inline_image-shrink_1000_1488/0/1520247605526?e=1614211200&amp;v=beta&amp;t=XP6ySCspvMwulc0loNSMaaXBT_DlGer1YpK2F3NxRl4"/></div>

Let’s examine a subtraction operation:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH-w6UWv5kACQ/article-inline_image-shrink_1000_1488/0/1520212177447?e=1614211200&amp;v=beta&amp;t=B-NrbMB0ARfVf7vNYrEEYNEd63DWI82YE2Jm4LdgAEI"/></div>

So what is the (1) you may ask, that is the overflow bit. In future tutorials we will examine what we refer to as the overflow flag and carry flag.

Next week we will dive into word lengths! Stay tuned!