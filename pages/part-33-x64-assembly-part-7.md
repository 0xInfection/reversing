# Part 33 - x64 Assembly \[Part 7\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we start our RE with the C++ language. The vast majority of malware is written in C++ and walking through simple code examples over the coming months and breaking them down in a debugger will give you a real hands-on approach to learning true RE.

We will use Kali Linux going forward with Radare 2. You can get VirtualBox and download the Kali Linux x64 Appliance to follow along.

Let's start with the C++ 1 code example:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1561023464535.jpg"/></div>

Here we simply create a main function and use the C++ output stream library to output the text "Hello World" with a new line at the end to the terminal. Let's compile and link:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1561023530059.jpg"/></div>

Let's run in the terminal:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1561023550876.jpg"/></div>

As we can see "Hello World" successfully echoed to the terminal.

Next week we will introduce Radare 2 and debug the code and examine what it looks like in x64 Assembly.