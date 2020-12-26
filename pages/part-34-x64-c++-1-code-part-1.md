# Part 34 - x64 C++ 1 Code \[Part 1\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's review our code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQENfdV6CiAZXQ/article-inline_image-shrink_1000_1488/0/1561714810492?e=1614211200&amp;v=beta&amp;t=1yue3Fox8m_DwRL4qu3B77hLoQ8B2mPq3oshLiDvlQQ"/></div>

Compile:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFa4XFadZl3Gw/article-inline_image-shrink_1000_1488/0/1561714836259?e=1614211200&amp;v=beta&amp;t=T7unD1AqBWl3e562JZUeMrWPnCiplBEIRDeA51IlOi4"/></div>

Run:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHD9kEqc4jUOg/article-inline_image-shrink_1000_1488/0/1561714869555?e=1614211200&amp;v=beta&amp;t=4T6RbjonYPfcxZLb8wYd3mtmGiu-K7Sla9pl7OqbaF0"/></div>

For literally years I have been using GDB as the debugger of choice. The reason is that it is on every Linux based system which runs just about every IoT and Server in the world. In addition, there are versions for Windows.

I have struggled hard with this but have decided to introduce another terminal based debugger called Radare 2. The reason I like Radare 2 so much is that it is still terminal based yet more robust with its feature set. If you are running a Kali Linux VM like I am here you can simply the below.

Let's open up our binary for write mode and simply analyze the binary.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE7_zNXdtKMzQ/article-inline_image-shrink_1000_1488/0/1561716186925?e=1614211200&amp;v=beta&amp;t=Npp0wYxe4mN_YwTucM-wEPPssTvkwLA3sBKks7G8oAw"/></div>

Ok, there is a lot going on here. Let's break it down. First, we open up Radare 2 in write mode by typing '__r2 -w ./1__' and then use the '__aaa__' command to analyze the binary. We then use '__s sym.main__' to seek to the main routine of the binary which is our entry point. We then do a '__pdf__' command to disassemble the binary.

We see what we refer to as the prologue where we push __rbp__ the stack base pointer onto the stack. We then move __rsp__ into __rbp__ for safe keeping and then we reserve __0x10__ hex bytes or 16 decimal bytes on the stack to make room for our string.

If none of this makes sense please go back to the beginning of the tutorial series to review basic assembly and the registers as it is CRITICAL you understand this before we move forward.

We can clearly see the qword of '__Hello World\\n__' at memory address __0x2005__ and then we see our C++ library call for the output stream which is __cout __to display our string to the terminal.

Let's examine __0x2005__ to verify that our string is at that location:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGhSH5m8Z3rng/article-inline_image-shrink_1000_1488/0/1561715552920?e=1614211200&amp;v=beta&amp;t=NzULlXHuDnoVjM_9wP941OXQgusgcI6EPOyU4ZBeA60"/></div>

Next week we will hack the value and modify the binary. I highly encourage you all to install VirtualBox which is free and get the Kali Linux VirtualBox image and install Vim as well.

There are tutorials on all of this in my prior series. Stay tuned for the hack next week!