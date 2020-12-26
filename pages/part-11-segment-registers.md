# Part 11: Segment Registers

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The segment registers are used specifically for referencing memory locations. There are three different methods of accessing system memory of which we will focus on the flat memory model which is relevant for our purposes.

There are six segment registers which are as follows:

__CS__: Code segment register stores the base location of the code section (.text section) which is used for data access.

__DS__: Data segment register stores the default location for variables (.data section) which is used for data access.

__ES__: Extra segment register which is used during string operations.

__SS__: Stack segment register stores the base location of the stack segment and is used when implicitly using the stack pointer or when explicitly using the base pointer.

__FS__: Extra segment register.

__GS__: Extra segment register.

Each segment register is 16-bits and contains the pointer to the start of the memory-specific segment. The CS register contains the pointer to the code segment in memory. The code segment is where the instruction codes are stored in memory. The processor retrieves instruction codes from memory based on the CS register value and an offset value contained in the instruction pointer (EIP) register. Keep in mind no program can explicitly load or change the CS register. The processor assigns its values as the program is assigned a memory space.

The DS, ES, FS and GS segment registers are all used to point to data segments. Each of the four separate data segments help the program separate data elements to ensure that they do no overlap. The program loads the data segment registers with the appropriate pointer value for the segments and then reference individual memory locations using an offset value.

The stack segment register (SS) is used to point to the stack segment. The stack contains data values passed to functions and procedures within the program.

Segment registers are considered part of the operating system and can neither read nor be changed directly in almost all cases. When working in the protected mode flat model (x86 architecture which is 32-bit), your program runs and receives a 4GB address space to which any 32-bit register can potentially address any of the four billion memory locations except for those protected areas defined by the operating system. Physical memory may be larger than 4GB however a 32-bit register can only express 4,294,967,296 different locations. If you have more than 4GB of memory in your computer, the OS must arrange a 4GB region within memory and your programs are limited to that new region. This task is completed by the segment registers and the OS keeps close control of this.

In our next tutorial we will continue our discussion of the IA-32 Architecture with the Instruction Pointer Register.