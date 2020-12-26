# Part 25 - ASM Program 2 \[Moving Data Between Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our second program we will demonstrate how we can move data between registers. Moving data from one register to another is the fastest way to move data. It is always advisable to keep data between registers as much as can be engineered for speed.

Specifically we will move the value in EDX into EAX. We will initialize this program with a simple immediate value of 22 decimal which will go into EDX and ultimately into EAX.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/726065964.jpg"/></div>

Keep in mind you can only move similar registers between each other. We know that EAX and EDX are 32-bit registers. We know that each of these registers can be accessed by their 16-bit values as ax and dx respectively. You can’t move a 32-bit value into a 16-bit value and vice-versa.

I look forward to seeing you all next week when we dive into debugging our second assembly program!