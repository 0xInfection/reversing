## Part 11 - ARM Firmware Boot Procedures

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s take a moment to talk about what happens when we first power on our Raspberry Pi device.

As soon as the Pi receives power, the graphics processor is the first thing to run as the processor is held in a reset state to which the GPU starts executing code. The ROM reads from the SD card and reads __bootcode.bin __to which gets loaded into memory in C2 cache and turns on the rest of the RAM to which __start.elf__ then loads.

The __start.elf __is an OS for the graphics processor and reads __config.txt __to which you can mod. The __kernel.img __then gets loaded into __0x8000__ in memory which is the Linux kernel.

Once loaded, __kernel.img __turns on the CPU and starts running at __0x8000 __in memory.

If we wanted, we could create our own __kernel.img__ to which we can hard code machine code into a file and replace the original image and then reboot. Keep in mind the ARM word size is 32 bit long which go from bit 0 to 31.

As stated, when __kernel.img__ is loaded the first byte, which is 8-bits, is loaded into address __0x8000__.

Lets open up a hex editor and write the following:

__FE FF FF EA__

Save the file as __kernel.img__ and reboot.

“Ok nothing happens, this sucks!”

Actually something did happen, you created your first bare-metal firmware! Time to break out the champagne!

When the Pi boots, the below code when it reached __kernel.img __loads the following:

__FE FF FF EA__

__@ address 0x8000, 0xfe gets loaded.__

__@ address 0x8001, 0xff gets loaded.__

__@ address 0x8002, 0xff gets loaded.__

__@ address 0x8003, 0xea gets loaded.__

“So what the hell is really going on?”

This set of commands simply executes an infinite loop.

Review the datasheet:

<a href="https://www.raspberrypi.org/wp-content/uploads/2012/02/BCM2835-ARM-Peripherals.pdf" rel="nofollow noopener" target="_blank">https://www.raspberrypi.org/wp-content/uploads/2012/02/BCM2835-ARM-Peripherals.pdf</a>

The above code has 3 parts to it:

1)Conditional – Set To Always

2)Op Code – Branch

3)Offset – How Far To Move Within The Current Location

__Condition – bits 31-28: 0xe or 1110__

__Op Code – bits 27-24: 0xa or 1010__

__Offset – bits 23-0 -2__

I know this may be a lot to wrap your mind around however it is critical that you take the time and read the datasheet linked above. Do not cut corners if you truly have the passion to understand the above. READ THE DATASHEET!

I will go through painstaking efforts to break everything down step-by-step however there are exercises like the above that I am asking you to review the datasheet above so you learn how to better understand where to look when you are stuck on a particular routine or set of machine code. This is one of those times I ask you to please read and research the datasheet above!

“I’m bored! Why the hell does this crap matter?”

Glad you asked! The single most dangerous malware on planet earth today is that of the root-kit variety. If you do not have a basic understanding of the above, you will never begin to even understand what a root-kit is as you progress in your understanding.

Anyone can simply replace the __kernel.img__ file with their own hacked version and you can have total control over the entire process from boot.

Next week we will dive into the Von Neumann Architecture.