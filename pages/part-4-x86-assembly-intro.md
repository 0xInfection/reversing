## Part 4: x86 Assembly Intro

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Ladies and Gentlemen, boys and girls, children of all ages! We are about to embark on a journey that will change your life forever!

There is vast&nbsp;material to cover to get a good understanding of Assembly Language and why it is important to understand the basics.

The first question we must answer is what is x86 Assembly Language to which the answer is a family of backward-compatible Assembly Languages which provide compatibility back to the Intel 8000 series of microprocessors. x86 Assembly Languages are used to produce object code for the aforementioned series of processors. It uses mnemonics to represent the instructions that the CPU can execute.

Assembly Language for the x86 microprocessor works in conjunction with various operating systems. We will focus on Linux Assembly Language utilizing the Intel syntax in addition to learning how to program in C to which we will disassemble the source code an analyze the respective Assembly.

x86 Assembly Language has two choices of syntax. The AT&amp;T syntax was dominant in the Unix world since the OS was developed at AT&amp;T Bell Labs. In contrast, the Intel syntax was originally used for the documentation of the x86 platform and was dominant in the MS-DOS and Windows environments.

For our purposes, when we are ultimately disassembling or debugging software, whether it be in a Linux or Windows environment, we will see the Intel syntax in large measure. This is essential whether we are examining a Windows binary in PE format or a Linux binary in ELF format. More on that later in this tutorial.

The main differences between the two is in the AT&amp;T syntax, the source comes before the destination and in the Intel syntax, the destination comes before the source. We will discuss this in more detail later in the tutorial.

Before you run for the door and regret embarking on this journey, remember, some basic context helps to which we will develop throughout our quest. Many of these topics may be confusing at this point which is perfectly normal as we will develop them in time.

We will focus on Linux Assembly because Linux runs on a variety of hardware and is capable of running devices such as a cell phone, personal computer or a complex commercial server.

Linux is also open source and there are many versions. We will focus on Ubuntu in our demonstrations which can be freely obtained. In contrast, the Windows operating system is owned and controlled by one company, Microsoft, to which all updates, security patches and service patches come directly from them where Linux has millions of professionals providing the same absolutely free!

We will also focus on a 32-bit architecture as ultimately most malware will be written for such in order to infect as many systems as possible. 32-bit applications/malware will work on 64-bit systems so we want to understand the basics of the 32-bit world.

In our next lesson we discuss the binary number system. Grab your cup of coffee you are going to need it!