## Part 37 - ASM Program 6 \[CMOV Instructions\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our sixth program we will demonstrate how we can work with CMOV instructions.

Before we dive into some code lets talk about CMOV is. CMOV can prevent the processor from utilizing the JMP instructions and speeds up the respective binary.

There are unsigned CMOV instructions such as:

CMOVA or CMOVNBE = Above \[Carry Flag or Zero Flag = 0\]

CMOVAE or CMOVNB = Above Or Equal \[Carry Flag = 0\]

CMOVNC = Not Carry \[Carry Flag = 0\]

CMOVB or CMOVNAE = Below \[Carry Flag = 1\]

CMOVC = Carry \[Carry Flag = 1\]

CMOVBE or CMOVNA = Below Or Equal \[Carry Flag or Zero Flag = 1\]

CMOVE or CMOVZ = Equal \[Zero Flag = 1\]

CMOVNE or CMOVNZ = Not Equal \[Zero Flag = 0\]

CMOVP or CMOVPE = Parity \[Parity Flag = 1\]

CMOVNP or CMOVPO = Not Parity \[Parity Flag =0\]

There are also signed CMOV instructions such as:

CMOVGE or CMOVNL = Greater Or Equal \[Sign Flag xor Overflow Flag = 0\]

CMOVL or CMOVNGE = Less \[Sign Flag xor Overflow Flag = 1\]

CMOVLE or CMOVNG = Less Or Equal \[Sign Flag xor Overflow Flag or ZF = 1\]

CMOVO = Overflow \[Overflow Flag = 1\]

CMOVNO = Not Overflow \[Overflow Flag = 0\]

CMOVS = Sign NEGATIVE \[Sign Flag = 1\]

CMOVNS = Not Sign POSITIVE \[Sign Flag = 0\]

Keep in mind to review the relationships between the unsigned and signed operations. The unsigned instructions utilize the CF, ZF and PF to determine the difference between the two operands where the signed instructions utilize the SF and OF to indicate the condition of the comparison between the operands.

If you need a refresher on the flag please review Part 14 on Flags in this series.

The CMOV instructions rely on a mathematical instruction that sets the EFLAGS register to operate and therefore saves the programmer to use JMP statements after the compare statement. Lets examine some source code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520240921769.jpg"/></div>

Ok lets begin with lines 21 and 22. This is nothing new that we have experienced as we are simply moving the array into ebx.

On line 24 we see the find\_smallest\_value function to where we are cycling through the array and using the CMOVB to find the lowest value ultimately.

We see __cmp %ebx, %eax__ to which cmp subtracts the first operand from the second and sets the EFLAGS register appropriately. At this point the cmovb is used to replace the value in ebx with the value in eax if the value is smaller than what was originally in the ebx register.

After we exit the loop we see three sets of sys\_writes to first display our message, second to display our converted integer to ascii value and then finally a period and line feed.

Keep in mind to assemble we type:

__as –32 -o cmov\_instructions.o cmov\_instructions.s__

To link the object file we type:

__ld -m elf\_i386 -o cmov\_instructions cmov\_instructions.o __

I look forward to seeing you all next week when we dive into debugging our sixth assembly program!