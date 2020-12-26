# Part 18 – Debugging Constants

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review last week’s code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG7GwzcUpYgew/article-inline_image-shrink_1000_1488/0/1520147783406?e=1614211200&amp;v=beta&amp;t=SdLc466lePsPkmV8fT11NXa-vHMJ0PitAr2q3PKvoPE"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEotLfqXgmzew/article-inline_image-shrink_1000_1488/0/1520194203208?e=1614211200&amp;v=beta&amp;t=2QHIX7jKms8LDh5wz04mS8eT1jcZ6RWiOkK_B9ayD1M"/></div>

As we can see the value in the memory address __0x10730 __is equal to __2017__.&nbsp;Let’s continue and watch the value print to the standard output (terminal) as it did last week when we ran it.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFaGz5Mxy_rpQ/article-inline_image-shrink_1000_1488/0/1520152068447?e=1614211200&amp;v=beta&amp;t=CcadDgVskDFid-xLpb5PLjI4Qd6cTsmV7cUUsLYzeGo"/></div>

We can see very clearly that we move the value from memory into __r1 __and then we branch to our __cout__ function to print to the terminal.&nbsp;At this stage you should feel a little more comfortable with understanding what the assembly is doing above.

Next week we will dive into Hacking Constants.