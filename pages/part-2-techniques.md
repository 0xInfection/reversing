## Part 2: Techniques

There are two basic techniques that you can employ when analyzing malware. The first being static analysis and the other being dynamic analysis.

Static analysis uses software tools to examine the executable without looking at the actual decompiled instructions in Assembly. We will not focus on this type of analysis as we are going to focus on actual disassembled binaries instead.

Dynamic analysis uses disassemblers and debuggers to analyze malware binaries. The most popular tool in the market today is called IDA which is a multi-platform, multi-processor disassembler and debugger. There are other disassembler/debugger tools as well on the market today such as Hopper Disassembler, OllyDbg and many more.

A disassembler will convert an executable binary written in Assembly, C, C++, etc into Assembly Language instructions that you can debug and manipulate.

Reverse engineering is much more than just malware analysis. At the end of our series, our capstone tutorial will utilize IDA as we will create a real-world scenario where you will be tasked by the CEO of ABC Biochemicals to secretly try to ethically hack his companies software that controls a bullet-proof door in a very sensitive Bio-Chemical lab in order to test how well the software works against real threats. The project will be very basic however it will ultimately showcase the power of Assembly Language and how one can use it to reverse engineer and ultimately provide solutions on how to better design the code to make it safer.

In our next lesson we will discuss various types of malware.