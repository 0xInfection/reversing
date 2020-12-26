# Part 28 - x64 Assembly \[Part 2\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we continue our tutorial with a simple subtract example. Let's examine the source code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH8rCvJISV5mg/article-inline_image-shrink_1000_1488/0/1551437589689?e=1614211200&amp;v=beta&amp;t=7f0OPo0sGhX0GNX_-jkWzYU1VzqHrr7oXY_84OD_Jk4"/></div>

Let's compile and run the debugger:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFOsjpu931lCA/article-inline_image-shrink_1000_1488/0/1551437628625?e=1614211200&amp;v=beta&amp;t=jIcde5vCIxkrXDbZdD--hxgCrGvy3pAttVfcRZoLGcw"/></div>

Let's run and disassemble:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE7bu1HtufvHA/article-inline_image-shrink_1000_1488/0/1551437662831?e=1614211200&amp;v=beta&amp;t=JPWyY6UWCbWI6ivguOLx7duCqqgJ-SI4eSMpovzAb6k"/></div>

As we can see very we load __16__ or __0x10__ hex into __EAX__ and then subtract __5__ from it in the next instruction.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGQ-N5eO6PM3A/article-inline_image-shrink_1000_1488/0/1551437723578?e=1614211200&amp;v=beta&amp;t=dbmnIl1oR0UGilI7MRD36iUh2IvX8Mw3sM3CEHwRLjs"/></div>

We step twice and then look at the resulting value in __RAX__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGBdnBh3BgNIw/article-inline_image-shrink_1000_1488/0/1551437759416?e=1614211200&amp;v=beta&amp;t=-jdHdiTz0b24GdcMxukEQNuOjJi5JCRi7XdKawjgk70"/></div>

As we can see the result is 0xb hex or 11 decimal as expected. It is important that you try these simple examples to get a grasp of what happens when we start to debug C++ code in future tutorials.