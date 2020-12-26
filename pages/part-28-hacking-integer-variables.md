# Part 28 – Hacking Integer Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEqDEnhIDVgHg/article-inline_image-shrink_1000_1488/0/1519988583160?e=1614211200&amp;v=beta&amp;t=D5Vg-W493fr-w96qOE-SGOHVaOvcnk_E-Xa7DgVzYdU"/></div>

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEeOZrk5uOQHA/article-inline_image-shrink_1000_1488/0/1519988510636?e=1614211200&amp;v=beta&amp;t=kni_sgud6QEsSA9sB-nEJSG5HdksIR8wZ9iYRlZCS-4"/></div>

Let’s take a look again inside the memory location of __0x10730__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEuioQfSU2mSw/article-inline_image-shrink_1000_1488/0/1519988543593?e=1614211200&amp;v=beta&amp;t=dsEGR4HX5HegzRfb9WWn211841ueJt4wSfZZP4cmKuY"/></div>

As we can clearly see the integer value of __777__ appears and when we continue it echoes out to the terminal the value of __777__ which corresponds with our c++ function __cout__.

Let’s hack the value inside of __0x10730__ and set the value to __666__ and then reexamine the value inside __0x10730__ and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEaRCgllMKnBg/article-inline_image-shrink_1000_1488/0/1519988571825?e=1614211200&amp;v=beta&amp;t=ZC_i5ZenG05Gu26aqYlsHyKHZvNMsXx31QTXGyHQV4A"/></div>

Success!&nbsp;As we can see we hacked the value to __666__ as we continue we see it echoed out to stdout.

Next week we will dive into Float Variables.