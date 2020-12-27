## Part 8 - CPSR

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The CPSR register stores information about the program and the results of a particular operation. Bits that are in the respective registers have pre-assigned conditions that are tested for an occurrence which are flags.

There are 32-bits that total this register. The highest 4 we are concerned with most which are:

Bit 31 – N = Negative Flag

Bit 30 – Z = Zero Flag

Bit 29 – C = Carry Flag (UNSIGNED OPERATIONS)

Bit 28 – V = Overflow flag (SIGNED OPERATIONS)

When the instruction completes the CPSR can get updated if it falls into one of the aforementioned scenarios. If one of the conditions occurs, a 1 goes into the respective bits.

There are two instructions that directly effect the CPSR flags which are CMP and CMN. CMP is compare such as:

<pre spellcheck="false">CMP R1, R0 @ notational subtraction where R1 – R0 and if the result is 0, bit 30 Z would be set to 1
</pre>

The most logical command that usually follows is BEQ = branch if equal, meaning the zero flag was set and branches to another label within the code.

Regarding CMP, if two operands are equal then the result is zero. CMN makes the same comparison but with the second operand negated for example:

<pre spellcheck="false">CMN R1, R0 @ R1 - (-R0) or R1 + R0
</pre>

When dealing with the SUB command, the result would NOT update the CPSR you would have to use the SUBS command to make any flag update respectively.

Next week we will dive into more information on the Link Register! Stay tuned!