# Part 13: Control Registers

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Their are five control registers which are used to determine the operating mode of the CPU and the characteristics of the current executing task. Each control register is as follows:

__CR0__: System flag that control the operating mode and various states of the processor.

__CR1__: (Not Currently Implemented)

__CR2__: Memory page fault information.

__CR3__: Memory page directory information.

__CR4__: Flags that enable processor feathers and indicate feature capabilities of the processor.

The values in each of the control registers can’t be directly accessed however the data in the control register can be moved to one of the general-purpose registers and once the data is in a GP register, a program can examine the bit flags in the register to determine the operating status of the processor in conjunction with the current running task.

If a change is required to a control register flag value, the change can be made to the data in the GP register and the register moved to the CR. Low-level System Programmers usually modify the values in control registers. Normal application programs do not usually modify control register entries however they might query flag values to determine the capabilities of the host processor chip on which the program is currently running.

In our next tutorial we will continue our discussion of the IA-32 Architecture with the topic of Flags.