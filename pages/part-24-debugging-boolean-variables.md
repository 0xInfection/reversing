# Part 24 – Debugging Boolean Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFDvsepyGWEkA/article-inline_image-shrink_1000_1488/0/1520236715844?e=1614211200&amp;v=beta&amp;t=GbqOWOVILF8nqNE0nZhwtDtRasEHgYlBQsy1Rc9GOjc"/></div>

Let’s debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGcWtIrh1tf8A/article-inline_image-shrink_1000_1488/0/1520194325794?e=1614211200&amp;v=beta&amp;t=DgtDcYsZuLIjOMp8Mw9EOAJCOE4YjzLPQPCnIlGKXMo"/></div>

Let’s step 4 times and disassemble.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEkh7vJ2OzHtQ/article-inline_image-shrink_1000_1488/0/1520190876822?e=1614211200&amp;v=beta&amp;t=kCZemRGiNf3vxvo0NxrgcNxHgP5kRYRT1WcV1c16wjE"/></div>

Let’s examine what is now in __r3__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH0R28tjbUz9A/article-inline_image-shrink_1000_1488/0/1520171350771?e=1614211200&amp;v=beta&amp;t=9XTVRTO0XkfPXMtX3sq2XLtTjVOo3r7w065AWY84HVE"/></div>

As we can clearly see the value in __isHacked__ is __0__ or __false__ which makes sense based on our c++ source code.

I know these lessons may seem trivial however Reverse Engineering is all about breaking things down in their most basic components.&nbsp;Reverse Engineering is about patience and logical flow.&nbsp;It is critical that you take the time and work through all of these examples with a Raspberry Pi device so that you can have a proper appreciation for how the process actually works.

Next week we will dive into Hacking Boolean Variables.