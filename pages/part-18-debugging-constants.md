## Part 18 – Debugging Constants

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review last week’s code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520147783406.jpg"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520194203208.jpg"/></div>

As we can see the value in the memory address __0x10730 __is equal to __2017__.&nbsp;Let’s continue and watch the value print to the standard output (terminal) as it did last week when we ran it.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520152068447.jpg"/></div>

We can see very clearly that we move the value from memory into __r1 __and then we branch to our __cout__ function to print to the terminal.&nbsp;At this stage you should feel a little more comfortable with understanding what the assembly is doing above.

Next week we will dive into Hacking Constants.