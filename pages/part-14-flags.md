# Part 14: Flags

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The topic of flags are one of the most extremely complex and complicated concepts of assembly language and program flow control when reverse engineering. This information below will become much clearer as we enter into the final phase of our training when we reverse engineer C applications into assembly language.

What is important here is to take away the fact that flags help control, check and verify program execution and are a mechanism to determine whether each operation that is performed by the processor is successful or not.

Flags are critical to assembly language applications as they are a check to verify each programs functions successful execution.

We are dealing with 32-bit assembly to which a single 32-bit register which contains a group of status, control and system flags exist. This register is called the EFLAGS register as it contains 32 bits of information that are mapped to represent specific flags of information.

There are three kinds of flags which are status flags, control flags and system flags.

Status flags are as follows:

__CF__: Carry Flag

__PF__: Parity Flag

__AF__: Adjust Flag

__ZF__: Zero Flag

__SF__: Sign Flag

__OF__: Overflow Flag

The carry flag is set when a math operation on an unsigned integer value generates a carry or borrow for the most significant bit. This is an overflow condition for the register involved in the math operation. When this occurs, the remaining data in the register is not the correct answer to the math operation.

The parity flag is used to indicate corrupt data as a result of a math operation in a register. When checked, the parity flag is set if the total number of 1 bits in the result is even and is cleared if the total number of 1 bits in the result is odd. When the parity flag is checked, an application can determine whether the register has been corrupted since the operation.

The adjust flag is used in Binary Coded Decimal math operations and is set if a carry or borrow operation occurs from bit 3 of the register used for the calculation.

The zero flag is set if the result of an operation is zero.

The sign flag is set to the most significant bit of the result which is the sign bit and indicates whether the result is positive or negative.

The overflow flag is used in signed integer arithmetic when a positive value is too big or a negative value is too small to be represented in the register.

Control flags are utilized to control specific behavior in the processor. The DF flag which is the direction flag is used to control the way strings are handled bu the processor. When set, string instructions automatically decrement memory addresses to get the next byte in the string. When cleared, string instructions automatically increment memory addresses to get the next byte in the string.

System flags are used to control OS level operations which should NEVER be modified by any respective program or application.

__TF__: Trap Flag

__IF__: Interrupt Enable Flag

__IOPL__: I/O Privilege Level Flag

__NT__: Nested Task Flag

__RF__: Resume Flag

__VM__: Virtual-8086 Mode Flag

__AC__: Alignment Check Flag

__VIF__: Virtual Interrupt Flag

__VIP__: Virtual Interrupt Pending Flag

__ID__: Identification Flag

The trap flag is set to enable single-step mode and when in this mode the processor performs only one instruction code at a time, waiting for a signal to perform the next instruction. This is essential when debugging.

The interrupt enable flag controls how the processor responds to signals received from external sources.

The I/O privilege field indicates the input-output privilege level of the currently running task and defines access levels for the input-output address space which must be less than or equal to the access level required to access the respective address space. In the case where it is not less than or equal to the access level required, any request to access the address space will be denied.

The nested task flag controls whether the currently running task is linked to the previously executed task and is used for chaining interrupted and called tasks.

The resume flag controls how the processor responds to exceptions when in debugging mode.

The VM flag indicates that the processor is operating in virtual-8086 mode instead of protected or real mode.

The alignment check flag is used in conjunction with the AM bit in the CR0 control register to enable alignment checking of memory references.

The virtual interrupt flag replicates the IF flag when the processor is operating in virtual mode.

The virtual interrupt pending flag is used when the processor is operating in virtual mode to indicate that n interrupt is pending.

The ID flag indicates whether the processor supports the CPUID instruction.

In our next tutorial we will discuss the stack.