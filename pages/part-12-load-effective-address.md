# Part 12 - Load Effective Address

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The data segment allocates memory on the heap in memory rather than the stack as they are not local variables they are known throughout the entire binary.&nbsp;

The sizes of data are as follows:

1)byte -&nbsp;We use the db notation which is obviously 1 byte or 8 bits.

2)word - We use dw and it is 2 bytes in length.

3)double word - We use dd to assign and they are 4 bytes long.

4)quad word - We use dq which is 8 bytes long.

5)xmm word - We use xmmword which is 16 bytes long.

6)ymm word - We use ymmword which is 32 bytes long.

There are SSE math registers which are separate from the CPU which hold the following:

1)real4 - This is a single or what you would think of as a floating point numbers as this is 4 bytes long.

2)real8 - This is a double floating point as this is 8 bytes long.

Finally there are arrays which can be single or multidimensional arrays where you can allocate against a db, dw, dd, dq, xmmword or ymmword.

We will see this in code when we get more advanced into the series however its critical that you understand the variables within a function are local and go to the stack as they do not last throughout the program.&nbsp;These variables which are part of the data segment are not local they are global and go to the heap.

The stack - local vars - grows down in memory so they start at a high memory address and grow down.&nbsp;The heap - global vars - grows from a lower memory address and grows up.&nbsp;

If you have questions please ask them in the comments as it is critical you get this concept down when we start to build our very basic operating system.

Next week we will dive into SHL! Stay tuned!