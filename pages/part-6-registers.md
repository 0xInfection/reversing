<h1>Part 6 – Registers</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>Our ARM microprocessor has internal storage which make any operation must faster as there is no external memory access needed. There are two modes, User and Thumb. We will be focusing on User Mode as we are ultimately focused on developing for a system on chip within a Linux OS rather than bare-metal programming which would be better suited on a microcontroller device.</p><p>In User Mode we have 16 registers and a CPSR register to which have a word length each which is 32-bits each or 8 bytes each.</p><p>Registers R0 to R12 are multi-purpose registers to which R13 – R15 have a unique purpose as well as the CPSR. Lets take a look at a simple table to illustrate.</p><pre spellcheck="false">R0 GPR (General-Purpose Register)
R1 GPR (General-Purpose Register)
R2 GPR (General-Purpose Register)
R3 GPR (General-Purpose Register)
R4 GPR (General-Purpose Register)
R5 GPR (General-Purpose Register)
R6 GPR (General-Purpose Register)
R7 GPR (General-Purpose Register)
R8 GPR (General-Purpose Register)
R9 GPR (General-Purpose Register)
R10 GPR (General-Purpose Register)
R11 GPR (General-Purpose Register)
R12 GPR (General-Purpose Register)
R13 Stack Pointer
R14 Link Register
R15 Program Counter
CPSR Current Program Status Register
</pre><p>It is critical that we understand registers in a very detailed way. At this point we understand R0 – R12 are general purpose and will be used to manipulate data as we build our programs and additionally when you are hacking apart or reverse engineering binaries from a hex dump on a cell phone or other ARM device, no matter what high-level language it is written in, it must ultimately come down to assembly which you need to understand registers and how they work to grasp and understand of any such aforementioned operation.</p><p>The chip we are working with is known as a load and store machine. This means we load a register with the contents of a register or memory location and we can store a register with the contents of a memory or register location. For example:</p><pre spellcheck="false">ldr, r4, [r10] @ 
    load r4 with the contents of r10, if r10 had the decimal value of 
    say 22, 22 would go to r4

str, r9, [r4] @ 
    store r9 contents into location in r4, if r9 had 0x02 hex, 
    0x02 would be stored into location r4
</pre><p>The @ simply indicates to the compiler that what follows it on a given line is a comment and to be ignored.</p><p>The next few weeks we will take our time and look at each of the special purpose registers so you have a great understanding of what they do.</p><p>Next week we will dive into more information on the program counter! Stay tuned!</p>