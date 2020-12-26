# Part 23 - Boot Sector Basics \[Part 6\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

We need to discuss memory at this point. Before we can discuss setting up a simple stack in our bootloader we must understand how memory is allocated in the bootsector.

1)__0x0 = Interrupt Vector Table __- This is where our interrupt table exists at the very base of memory. This is where all of our interrupt calls exist.

2)__0x400 = BIOS Data Area__ - This stores variables about the state of the bootable device.

3)__0x7c00 = Loaded Boot Sector__ - This has our machine code that will be loaded into RAM by the bootloader firmware (note: firmware is simply code that runs before an OS runs like what we are doing).

4)__0x7e00 = Free__ - This is your stack area that you can develop in.

5)__0x9fc00 = Extended BIOS Data Area__ - Holds data from disk track buffers and other connected devices as remember there is no file system as of yet.

6)__0xa0000 = Video Memory__ - BIOS maps your video memory here at boot.

7)__0xc0000 = BIOS__ - Where BIOS officially resides.

8)__0x100000 = Free__ - Additional space you can develop in.

This is critical that you understand how memory is laid out at boot. In our next lesson we will create a simple stack at __0x7e00__.