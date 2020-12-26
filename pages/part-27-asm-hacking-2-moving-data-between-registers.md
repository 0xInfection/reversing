# Part 27 - ASM Hacking 2 \[Moving Data Between Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s hack the second program below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFdz9-ngv5wcg/article-inline_image-shrink_1000_1488/0/1520583727180?e=1614211200&amp;v=beta&amp;t=yBmdvpclAOCqp7SQmDEpppITEV-8yShYKt1GXj1R3gI"/></div>

Lets fire up GDB and break on \_start, run the binary and disas:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH3yve7S4b2Pg/article-inline_image-shrink_1000_1488/0/1520066773312?e=1614211200&amp;v=beta&amp;t=q0R5Ubr7Dy03WbgGbrUUzx_eVjsX7kJfS0ZtXQwTaPU"/></div>

Now lets __si__ twice and __i r__:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFs3ZSHScwHNw/article-inline_image-shrink_1000_1488/0/1520143945686?e=1614211200&amp;v=beta&amp;t=_f_UJl1lbjgPBTFFx9X9wH67LUZ-nux5hUJqfOkHgZI"/></div>

As we can see the value of __0x16__ or __22__ decimal did move into EDX successfully. This is what we did in the last lesson however here we are going to hack that value to something else.

We can __set $edx = 0x19__ for example:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEv0kDU_NqAsA/article-inline_image-shrink_1000_1488/0/1520583727155?e=1614211200&amp;v=beta&amp;t=AWBd-Unz_iisRFh1s6T0fo-6V7no6SJHcyFz9hvd8G8"/></div>

As you can see we easily hacked the value of __EDX__ to __0x19__ or __25__ decimal.

Hopefully you see some very simple patterns now that we are diving into very simple assembly language programs. The key is to understand how to manipulate values and instructions so that you have complete control over the binary.

We are going to continue to move at a snails pace throughout the rest of this tutorial as my goal is to give everyone very small bite-size examples of how to understand x86 assembly.

I look forward to seeing you all next week when we dive into writing our third assembly program!