# Part 21 - Boot Sector Basics \[Part 4\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

We begin by looking at some simple additions to our code. What we will accomplish today is to create a simple operating system that does literally nothing but boot. We will use QEMU as an emulator as I am too lazy to set up VirtualBox or VMWare however you can easily port the .bin to an .iso if you chose and boot from either.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/743794334.jpg"/></div>

We are simply adding a padding algorithm on line 7 that simply examines how many bytes are left after we subtract 200h or 512 and then it pads the remaining bytes with zeros. At the end you will see what we refer to as the magic number which is __0xaa55__ as this is a signature that the cpu is looking for to identify a boot sector. Remember this code is at sector 0 when it boots as there is no file system so if it finds the successful signature it will attempt to boot it.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="imgs/118783045.jpg"/></div>

We build the binary with the code above. Now let's look at the code in the hex editor.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/130955021.jpg"/></div>

As you can see it pads out the remaining bytes up to 200h or 512 with 0's as we anticipated. Below is the remainder of the binary.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/227028509.jpg"/></div>

As you can see at the very end we have __55 AA__. We remember that our processor is little endian so when we code it it was __aa 55__ and which is in it's mapped format. When it goes into the cpu it reverses the byte order. This is critical that you understand this.

Next week we will simply do nothing more than launch our new operating system. Stay tuned.