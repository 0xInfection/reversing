# Part 16 - Hacking Hello World

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code from two weeks ago.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGNauUKkkfcsA/article-inline_image-shrink_1000_1488/0/1520191330889?e=1614211200&amp;v=beta&amp;t=fpTWNkGztvxgeDkO0-9PQOyo6jYfTPWO0byFNmN73Ds"/></div>

Let’s debug once again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHhlX_oNWoJIA/article-inline_image-shrink_1000_1488/0/1520233045514?e=1614211200&amp;v=beta&amp;t=JEyS8T873usIeyXMEokhgphAUmnHpPvwgwXdyb3mKvI"/></div>

Let’s once again examine the contents of the string at memory address __0x10750__ and continue through the execution of the program.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH5BjGLMZLjng/article-inline_image-shrink_1000_1488/0/1520200292099?e=1614211200&amp;v=beta&amp;t=wv5zorS0UzW4rZ0keha0AECo1VGbbRnk74JSjQa7L3U"/></div>

As you can see it holds the “__Hello World!__” string and when we continue through it echo’s back to the terminal as such.

Let’s hack!&nbsp;Let’s now overwrite the value inside of the memory address with the string, “__Hacked World!__” and continue execution.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEKZs_5pJdi_Q/article-inline_image-shrink_1000_1488/0/1520148428152?e=1614211200&amp;v=beta&amp;t=5v-3cbDBQ9AHZI2zXKCnrq2GyZmE4TccI8xRAD1_UYg"/></div>

Woohoo!&nbsp;Our first hack!&nbsp;As you can see as you understand Assembly you have ABSOLUTE control over the entire binary no matter what language it is written in.&nbsp;In this very simple example we were able to hack the value inside the memory address of __0x10750__ to which when executed it echoed, “__Hacked World!__” to the terminal or standard output.

Let’s again run the binary and do a disassembly.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEj7blx8L57Bg/article-inline_image-shrink_1000_1488/0/1520230658310?e=1614211200&amp;v=beta&amp;t=ecewuvor-jYWRiIjhcA8MaF2hHlGNsZ-06PKFyJ947Q"/></div>

Let’s now do the same procedure however lets __si__ 3x and examine the string inside of __r1__.&nbsp;We see that it contains, “__Hello World!__” as it has been successfully __ldr __(load from memory into the register) at __main+12__.

Let’s now set r1 to “__Hacked World!__” and continue execution.&nbsp;As you can see we now hacked it coming out of the register rather than in memory.&nbsp;You can clearly begin to see there are a number of ways to hack anything and here is a simple example of two such ways.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQECLU9XPGgLNQ/article-inline_image-shrink_1000_1488/0/1520231520333?e=1614211200&amp;v=beta&amp;t=qrcGe1s0ry-cGZRb7mRNQdoPv69SS-ZYxIJ1LNXMV0o"/></div>

Reverse Engineering is all about understanding how a program executes and hijacking execution flow and changing values to suit our purpose!&nbsp;Today you took your first step into this amazing journey!

Next week we will dive into constants.