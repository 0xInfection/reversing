# Part 1 – The Meaning Of Life Part 2

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Welcome to the ARM Reverse Engineering tutorial. This is the third tutorial series that I have done focusing on Assembly Language and Reverse Engineering.

The first series was on x86 Assembly and the second was on ARM Assembly. This series will be an expansion series on ARM focusing on ARM Reverse Engineering so rather than create programs directly in Assembly alone and then Reverse Engineer the binary in Assembly we will work with Assembly and C together and Reverse Engineer in Assembly so that you will get a flavor for a real-world series of applications and what it looks like disassembled.

We will not be working with GUI tools such as IDA Pro as we will be working with GDB in CLI shell. We will not be working in a traditional lab environment where we are going to put a binary into a debugger rather we are going to SSH into the ARM device and actually attach to a running process (PID) and Reverse Engineer the process as it is running.

The first 13 weeks will be an exact review of the ARM Assembly series as it is critical that we re-examine these concepts so that we have a very firm grasp when it comes time to reverse our binaries.

I wanted to bring back the original quote below before we get started...

“So if I go to college and learn Java will I make a million dollars and have nice things?”

I felt it necessary to start out this tutorial series with such a statement. This is NOT an attack on Java as I have used Java in Android Development, Spring and JavaEE. In today’s Agile environment, rapid-development is reality. With the increased challenges in both the commercial market and the government sector, software development will continue to focus on more robust libraries that will do more with less. React, Python, Java, C\# and the like will continue to grow not shrink as the race for project completion augments with each passing second of time.

Like it or not, hardware is getting smaller and smaller and the trend is going from CISC to RISC. A CISC is your typical x86/x64 computer with a complex series of instructions. CISC computers will always exist however with the trend going toward cloud computing and the fact that RISC machines with a reduced instruction set are so enormously powerful today, they are the obvious choice for consumption.

How many cell phones do you think exist on earth today? Most of them are RISC machines. How many of you have a Smart TV or Amazon Echo or any number of devices considered part of the IOT or Internet Of Things? Each of these devices have one thing in common – they are RISC and all are primarily ARM based.

ARM is an advanced RISC machine. Compared to the very complex architecture of a CISC, most ARM systems today are what is referred to as a SoC or system on chip which is an integrated circuit which has all of the components of a computer and electronic system on a single chip. This includes RF functionality as well. These low-power embedded devices can run versions of Windows, Linux and many other advanced operating systems.

“Well who cares about ARM, you can call it anything you want, I know Java and that’s all I need to know cause when I program it works everywhere so I don’t have to worry about anything under the hood.”

I again just want you to reflect on the above statement for a brief moment. As every day continues to pass, more and more systems are becoming vulnerable to attack and compromise. Taking the time to understand what is going on under the hood can only help to curb this unfortunate reality.

This series will focus on ARM Reverse Engineering. We will work with a Raspberry Pi 3 which contains the Broadcom BCM2837 SoC with a 4x ARM Cortex-A53, 1.2GHz CPU and 1 GB LPDDR2 RAM. We will work with the Raspbian Jessie, Linux-based operating system. If you don’t own a Raspberry Pi 3, they are usually available for $35 on Amazon or any number of retailers. If you would like to learn more visit <a href="https://www.raspberrypi.org/" rel="nofollow noopener" target="_blank">https://www.raspberrypi.org</a>.

We will work solely in the terminal so no pretty pictures and graphics as we are keeping it to the hardcore bare-bones utilizing the GNU toolkit to compile and debug our code base.

__UNDER NO CONDITIONS ARE YOU TO EVER USE THIS EDUCATION TO CAUSE HARM TO ANY SYSTEM OF ANY KIND AS I AM NOT RESPONSIBLE! THIS IS FOR LEARNING PURPOSES ONLY!__

Next week we will dive into the binary number system and compare and contrast it with decimal and hexadecimal so we have a proper framework of understanding to move forward.