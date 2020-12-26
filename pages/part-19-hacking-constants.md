# Part 19 – Hacking Constants

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our original code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520195148562.jpg"/></div>

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144504108.jpg"/></div>

As we can see the value in the memory address __0x10730 __is equal to __2017__.&nbsp;Let’s change that value in memory to __1981__.&nbsp;Let’s continue and watch the value turn to __1981__!&nbsp;Successful hack!

Let’s hack a second way!&nbsp;Re-start the program and set a breakpoint at main+28 and continue to the breakpoint.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520146785758.jpg"/></div>

Let's continue and we see the value in __r1__ is __2017__.&nbsp;Let’s change the value in __r1__ to __1981__.&nbsp;We continue and see the program successfully hacked to __1981__!&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148769675.jpg"/></div>

Next week we will dive into Character Variables.