# Part 5 – Word Lengths

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The system on chip we are working with has a 32-bit ARM CPU. 32-bits is actually 4 bytes of information which make up a word.

If you remember my prior tutorial on x86 Assembly, a word was 16-bits. Every different architecture defines a word differently.

The most significant bit of a word for our ARM CPU is located at bit 31 therefore a carry is generated if an overflow occurs there.

The lowest address in our architecture starts at 0x00000000 and goes to 0xFFFFFFFF. The processor sees memory in word blocks therefore every 4 bytes. A memory address associated with the start of a word is referred to as a word boundary and is divisible by 4. For example here is our first word:

<pre spellcheck="false">0x00000000
0x00000004
0x00000008
0x0000000C
</pre>

So why is this important? There is the concept of fetching and executing to which the processor deals with instructions to which it must work in this fashion for proper execution.

Before we dive into coding assembly it is critical that you understand some basics of how the CPU operates. There will be a number of more lectures going over the framework so I appreciate everyone hanging in there!

Next week we will dive into registers! Stay tuned!