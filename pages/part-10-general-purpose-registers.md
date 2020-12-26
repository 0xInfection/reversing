# Part 10: General-purpose Registers

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The general-purpose registers are used to temporarily store data as it is processed on the processor. The registers have evolved dramatically over time and continue to do so. We will focus on 32-bit x86 architecture for our purposes.

Each new version of general-purpose registers is created to&nbsp;be backward compatible with previous processors. This means that code utilizing 8-bit registers on the 8080 chips will still function on today's 64-bit chipset.

General-purpose registers can be used to hold any type of data to which some have acquired specific use which are used in programs. Lets review the 8 general-purpose registers in an IA-32 architecture.

__EAX__: Main register used in arithmetic calculations. Also known as accumulator, as it holds results of arithmetic operations and function return values.

__EBX__: The Base Register. Pointer to data in the DS segment. Used to store the base address of the program.

__ECX__: The Counter register is often used to hold a value representing the number of times a process is to be repeated. Used for loop and string operations.

__EDX__: A general purpose register. Additionally used for I/O operations. In addition will extend EAX to 64-bits.

__ESI__: Source Index register. Pointer to data in the segment pointed to by the DS register. Used as an offset address in string and array operations. It holds the address from where to read data.

__EDI__: Destination Index register. Pointer to data (or destination) in the segment pointed to by the ES register. Used as an offset address in string and array operations. It holds the implied write address of all string operations.

__EBP__: Base Pointer. Pointer to data on the stack (in the SS segment). It points to the bottom of the current stack frame. It is used to reference local variables.

__ESP__: Stack Pointer (in the SS segment). It points to the top of the current stack frame. It is used to reference local variables.

Keep in mind each of the above registers are 32-bit in length or 4 bytes in length. Each of the lower 2 bytes of the EAX, EBX, ECX, and EDX registers can be referenced by AX and then subdivided by the names AH, BH, CH and DH for high bytes and AL, BL, CL and DL for the low bytes which are 1 byte each.

In addition, the ESI, EDI, EBP and ESP can be referenced by their 16-bit equivalent which is SI, DI, BP, SP.

This can be a bit confusing to someone who has not studied computer engineering however let me illustrate in the table below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/393089097.jpg"/></div>

EAX would have AX as its 16-bit segment and then you can further subdivide AX into AL for the low 8 bits and AH for the high 8 bits. The same holds true for EBX, ECX and EDX as well. EBX would have BX as its 16-bit segment and then you can further subdivide BX into BL for the low 8 bits and BH for the high 8 bits. ECX would have CX as its 16-bit segment and then you can further subdivide CX into CL for the low 8 bits and BH for the high 8 bits. EDX would have DX as its 16-bit segment and then you can further subdivide DX into DL for the low 8 bits and DH for the high 8 bits.

ESI, EDI, EBP and ESP can be broken down into its 16-bit segments as follows:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1065849384.jpg"/></div>

ESI would have SI as its 16-bit segment, EDI would have DI as its 16-bit segment, EBP would have BP as its 16-bit segment and ESP would have SP as its 16-bit segment.

In our next tutorial we will continue our discussion of the IA-32 Architecture with the Segment Registers.