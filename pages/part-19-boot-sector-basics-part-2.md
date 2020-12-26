# Part 19 - Boot Sector Basics \[Part 2\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

For those of you that are familiar with assembly these next several weeks/months might seem like we are progressing very slowly however the aim is to help those with little understanding of hardware to get a better understanding of the very systems that power the cloud.

The vast majority of AWS and Azure as well as many other cloud services utilize x64 based operating systems. Understanding what happens when these systems boot is of significant value and that is why we are going to go thorough a very slow process looking at each piece of a boot sector when a machine loads.

Let's examine our source code. Follow along in Vim or Nano.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1545990601552.jpg"/></div>

Last week we learned the opcodes for line 1 and 2 to which we do not have to review. Today we add a byte of data into our code. Notice this is a hexadecimal number and will match our binary upon inspection. In future lessons we will see how it looks when we do decimal and other systems.

Let's compile. If you do not have NASM installed please ensure you type __sudo apt-get install nasm__.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1545990746117.jpg"/></div>

Let's look at our binary in a hex editor. I use GHex as I keep to the GNU tradition as we will in future lessons use the GNU debugger called GDB. These are all on your Linux systems as I am using Ubuntu for these tutorials.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1545990876404.jpg"/></div>

We saw last week that the __EB__ and __FE__ correspond to our __INC__ and __JMP__ instructions. If this is unclear please re-read last weeks lecture. We see the 3rd byte as __10__. Remember this is hexadecimal so the value in decimal would be __16__.

Next week we will keep adding to our code and progress in our OS development series.