## Part 12 - Load Effective Address

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

When a binary executes in RAM the OS will unmap the code into a data segment where it finds free space in memory.&nbsp;

Load Effective Address loads a given memory address as a pointer to any given variable.&nbsp;For example:

__lea rbx, my\_var__

This will load the address of __my\_var&nbsp;__ into __rbx__.&nbsp;

In C++, a pointer actually adds what the user would see as one if something was incremented however it is actually moving it 2 bytes forward under the hood assuming it is a word in length or 16 bits or 2 bytes.&nbsp;Same thing.

In Assembly every single byte is addressable.&nbsp;For example:

__lea rax, my\_var__

__inc rax__

__mov word ptr \[rax\], rbx__

Let’s say the value of __0x20__ is in __rbx__.&nbsp;This above instruction will place the value of __0x20__ into a non-word boundary which will result in an error.&nbsp;You would have to increment __rax__ by 2 to ensure that does not happen.

Next week we will dive into the data segment! Stay tuned!