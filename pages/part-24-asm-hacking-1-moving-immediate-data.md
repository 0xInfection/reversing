# Part 24 - ASM Hacking 1 \[Moving Immediate Data\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s begin by loading the binary into GDB.

To load into GDB type:

__gdb -q moving\_immediate\_data__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGmxUkcxGlQFg/article-inline_image-shrink_1000_1488/0/1520534645555?e=1614211200&amp;v=beta&amp;t=gbsmxaezbk1B_4xKcmhpV97wT732t2DC3c7xjgFd9ck"/></div>

Let’s first set a breakpoint on start by typing __b \_start__.

We can then run the program by typing __r__.

To then begin disassembly, we simply type __disas__.

We coded a __nop__ which means no operation or __0x90__ from an OPCODE perspective for proper debugging purposes which the breakpoint properly hit. This is good practice when creating assembly programs.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGZBzT7jIhTSw/article-inline_image-shrink_1000_1488/0/1520241969888?e=1614211200&amp;v=beta&amp;t=g1r1dORRYM8-7n-Q_V5pd-7kjr4EHfJKKGWp5sckDXc"/></div>

Lets have some fun! At this point lets __si__ once and do an __i r__ to see that__ 0x64__ has in fact been moved into __EAX__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG2mmq0T4sx3Q/article-inline_image-shrink_1000_1488/0/1520148350561?e=1614211200&amp;v=beta&amp;t=UePLiVw5TluwehUCLzeJKsRurClCyRq_0DlKIiqF_40"/></div>

We can see __EAX__ has the value of __0x64__ or __100__ decimal. Lets HACK that value now by setting __EAX__ to say something like __0x66__ by typing __set $eax = 0x66__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGXO_j1-YdTug/article-inline_image-shrink_1000_1488/0/1520194300522?e=1614211200&amp;v=beta&amp;t=O3X7YMmK2us1RC1qwDdhLtnkWhziQ5JH0iLQKdj6lAY"/></div>

BAM! There we go! You can see the ULTIMATE power of assembly here! We just hacked the value from __0x64__ to __0x66__ or __100__ to __102__ decimal. This is a trivial example however you can clearly see when you learn to master these concepts you develop a greater power over the computer. With each program that we create, we will have a very simple lesson like this where we will hijack at least one portion of the code so we can not only see how the program is created and debugged but how we can manipulate it to whatever we want.

I look forward to seeing you all next week when we dive into creating our second assembly program!