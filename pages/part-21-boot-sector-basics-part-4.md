# Part 21 - Boot Sector Basics \[Part 4\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

We begin by looking at some simple additions to our code. What we will accomplish today is to create a simple operating system that does literally nothing but boot. We will use QEMU as an emulator as I am too lazy to set up VirtualBox or VMWare however you can easily port the .bin to an .iso if you chose and boot from either.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFKueFbAlgWJg/article-inline_image-shrink_1000_1488/0/1547203117260?e=1614211200&amp;v=beta&amp;t=8PWHO-WDVtVgLC9kT5b_yxnsq5nTG5s95iAQNkvicnM"/></div>

We are simply adding a padding algorithm on line 7 that simply examines how many bytes are left after we subtract 200h or 512 and then it pads the remaining bytes with zeros. At the end you will see what we refer to as the magic number which is __0xaa55__ as this is a signature that the cpu is looking for to identify a boot sector. Remember this code is at sector 0 when it boots as there is no file system so if it finds the successful signature it will attempt to boot it.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEL43xp4DVVtg/article-inline_image-shrink_1000_1488/0/1547203262774?e=1614211200&amp;v=beta&amp;t=oLsJf3_CU0zKIBCqYZXderlrdZeFPRyI1HYdbzpvsSQ"/></div>

We build the binary with the code above. Now let's look at the code in the hex editor.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQErn1vFqsRp3g/article-inline_image-shrink_1000_1488/0/1547203298648?e=1614211200&amp;v=beta&amp;t=Y78O1LwzNDCW5rRsIeywgK9Y-Fxcb49laWQBplI8t5g"/></div>

As you can see it pads out the remaining bytes up to 200h or 512 with 0's as we anticipated. Below is the remainder of the binary.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGGcbn_T4vZyA/article-inline_image-shrink_1000_1488/0/1547203339833?e=1614211200&amp;v=beta&amp;t=7YTLtPcW3Ytq14eQg69yspd5zaN47z1_Qjo9Nwgfb8E"/></div>

As you can see at the very end we have __55 AA__. We remember that our processor is little endian so when we code it it was __aa 55__ and which is in it's mapped format. When it goes into the cpu it reverses the byte order. This is critical that you understand this.

Next week we will simply do nothing more than launch our new operating system. Stay tuned.