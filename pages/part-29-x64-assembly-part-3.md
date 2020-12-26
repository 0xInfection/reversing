# Part 29 - x64 Assembly \[Part 3\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we will code our simple, "hello world" program in x64 Assembly.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/892118136.jpg"/></div>

We simply create a string in the __.data __section and add a return character at the end of the statement. We then perform a simple write call which utilizes the OS's interrupt vector table to spit out our string in the standard output or terminal.

We will compile and run below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/464836329.jpg"/></div>

As we can see "__Hello World__!" has been echoed to the terminal. Next week we will debug this simple program in GDB.