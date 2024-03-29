## Part 25 - Boot Sector Basics \[Part 8\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we will put all the pieces together. We will create our custom OS that does nothing but boot-up, set a video mode and then only accept numeric digits in the console. This is the final tutorial in this mini-series of Boot Sector Basics.

Let's examine our code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1549024795636.jpg"/></div>

The first thing we do is move to the programable area of the boot sector code at address 0x7c00. We then set the stack base and identify the area for our stack and set the base pointer into the stack pointer.

We then call our video mode function where we set a 640x200 greyscale console. We then call our get character input function that will only allow digits 0 to 9 as you can see 0x30 is the hex ascii value for 0 and 0x39 is the hex ascii value of 9. If the user types anything else in the console literally nothing will enter into the console. This is the absolute control you have in Assembly.

Lets compile and run:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1549025055903.jpg"/></div>

We then see the qemu console:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1549025085922.jpg"/></div>

As you can see I am only able to type numeric digits in our OS. Try it for yourself. Write the code and compile and run in the qemu editor. If you do not have qemu installed I show you in detail how to install it in the last two tutorials.

Take the time to really review what I am doing here as it is critical to understand that this is how your computer boots before going into 32 then 64-bit mode.

Next week we will simply discuss the high-level concept of how your computer bridges a 64-bit OS.