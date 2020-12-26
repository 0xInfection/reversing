# Part 22 – Hacking Character Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGQe7xNNQbcCQ/article-inline_image-shrink_1000_1488/0/1520232430320?e=1614211200&amp;v=beta&amp;t=Nx3fu9UlKRPpDGjvO24NrGxVvnXPIrplSvw2qLmWjr4"/></div>

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG66QjDKlM4ng/article-inline_image-shrink_1000_1488/0/1520194771044?e=1614211200&amp;v=beta&amp;t=-ixL3KbRpV_bCTTNxfQfZhqYoVaUfTnN17PxKBgd7-A"/></div>

We again see the direct value of __0x6e__ moved into __r3__ at __main+12__ which is our ‘__n__’.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH4dKt6Jvgy7w/article-inline_image-shrink_1000_1488/0/1520195499705?e=1614211200&amp;v=beta&amp;t=-XXwe8QGdne1pO-3zIhDwpvAuky7_EaSzcMFaSr0Krk"/></div>

After stepping into 4 times and verify the value in __r3__ which we clearly see as ‘__n__’.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGLWv-llvF9rw/article-inline_image-shrink_1000_1488/0/1520233196032?e=1614211200&amp;v=beta&amp;t=QHCdAM7qfifVptKnQrnp45Spt5X4HLWDQz6OPYWi1ac"/></div>

Let’s hack the value in __r3__ to a ‘__y__’ and then reexamine the value in __r3__.&nbsp;We can now clearly see it has been changed to ‘__y__’.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE57P7xw6ov5A/article-inline_image-shrink_1000_1488/0/1520232999022?e=1614211200&amp;v=beta&amp;t=QfS0OLMo_cOv7LRCwy3TC5uVy3hsmcZFRfSMISd7VHU"/></div>

As we continue we successfully see our hack worked!&nbsp;We see the value of ‘__y__’ printing to the standard output.

Next week we will dive into Boolean Variables.