# Part 26 - Boot Sector Basics \[Part 9\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we begin our actual x64 code basics. Over the next few weeks I will create very simple examples so we get a grasp of the x64 architecture. Let's start with a basic code block:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/129351532.jpg"/></div>

We begin by declaring the __.data__ section to which all of our global data is stores. If we had a string or some other form of hard coded data it would go in that block. In our example we will leave it empty.

The __.text__ section declares where the entry point of the program will begin in our case we use __\_start__ or you can use __main__.

We simply move the value of decimal 16 or hex 10 into the 64-bit RAX register. We will see in a moment that the processor will use only the lower EAX when we debug in GDB.

The last piece is just a simple exit routine which we move 60 into RAX and then syscall. It simply returns operation back to the OS.

Let's compile and link:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="imgs/857388359.jpg"/></div>

Let's debug in GDB:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="imgs/726641022.jpg"/></div>

Let's set the debugger for intel syntax and set a break on start:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1723192.jpg"/></div>

As we can see 16 decimal or hex 10 is about to be moved into EAX but as we can see it has not been completed until we step forward.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/347274070.jpg"/></div>

Now we can view our registers.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/474437505.jpg"/></div>

We can see that RAX holds decimal 16 or hex 10 successfully.

We will spend several weeks on these simple examples so you can get comfortable with how the processor operates and its internal workings.