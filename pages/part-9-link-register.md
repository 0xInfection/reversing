# Part 9 - Link Register

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The Link Register, R14, is used to hold the return address of a function call.

When a BL (branch with link) instruction performs a subroutine call, the link register is set to the subroutine return address.&nbsp;BL jumps to another location in the code and when complete allows a return&nbsp;to the point right after the BL code section.&nbsp;When the subroutine returns, the link register returns the address back to the program counter.

The link register does not require the writes and reads of the memory containing the stack which can save a considerable percentage of execution time with repeated calls of small subroutines.

When BL has executed, the return address which is the address of the next instruction to be executed, is loaded into the LR or R14.&nbsp;When the subroutine has finished, the LR is copied directly to the PC (Program Counter) or R15 and code execution continues where it was prior in the sequential code source.

CODE TIME! Don’t be discouraged if you don’t understand everything in the code example here.&nbsp;It will become clear over the next few lessons.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGPWFIFoeU5FQ/article-inline_image-shrink_1000_1488/0/1520232099195?e=1614211200&amp;v=beta&amp;t=Id7F9An5RopHYQjnoEzWNEt7PMXMTeqJVUGDq35matM"/></div>

To compile:

<pre spellcheck="false">as -o lr_demo.o lr_demo.s

ld -o lr_demo lr_demo.o
</pre>

The simple example I created here is pretty self-explanatory.&nbsp;We start and proceed to the __no\_return__ subroutine and proceed to the __my\_function__ subroutine then to the __wrap\_up__ subroutine and finally__ exit__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFRqZj9YmvYuQ/article-inline_image-shrink_1000_1488/0/1520190659000?e=1614211200&amp;v=beta&amp;t=1Z7wGnOAHP9LPGCUbIWdMoXg1n2guXqy379ChZV-jV0"/></div>

It is necessary that we jump into GDB which is our debugger to see exactly what happens with each step:

As you can see with every step inside the debugger it shows you exactly the progression from __no\_return __to __my\_function__ skipping __wrap\_up__ until the program counter gets the address from the link register.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHIvvLr67EmrA/article-inline_image-shrink_1000_1488/0/1520221355382?e=1614211200&amp;v=beta&amp;t=0X_ROhHivP864Y5ZGKFo7R_TTfkb19K421ftEeUx5Lc"/></div>

Here we see the progression from __wrap\_up__ to __exit__.

This is a fundamental operation when we see next week how the stack operates as the LR is an essential part of this process.

Next week we will dive into the Stack Pointer!&nbsp;Stay tuned!