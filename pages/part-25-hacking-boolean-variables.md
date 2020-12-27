## Part 25 – Hacking Boolean Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520191957701.jpg"/></div>

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520210981189.jpg"/></div>

Let’s break at main, run and disas in addition to step into four times.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520146846926.jpg"/></div>

We see that __0__ or __FALSE__ is moved into __r3__ at main+12.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520218746699.jpg"/></div>

Very simply we set __r3__ to __1__ or __TRUE__ and continue execution to which we notice that the Boolean variable __isHacked__ is now __TRUE__.

It’s that simple folks!&nbsp;These elementary examples will help build your mental library of examples of how to approach everything in code and understanding how to take control of code execution no matter what!

Next week we will dive into Integer Variables.