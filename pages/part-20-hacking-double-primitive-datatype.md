## Part 20 - Hacking Double Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we hack the double from the last lesson.

Let's fire up radare2 in write mode.

<pre spellcheck="false">radare2 -w ./0x06_asm64_double_primitive_datatype
</pre>

Let's auto analyze.

<pre spellcheck="false">aaa
</pre>

Seek to main.

<pre spellcheck="false">s main
</pre>

View disassembly.

<pre spellcheck="false">v
</pre>

Let's get back to the terminal view.

<pre spellcheck="false">q
</pre>

All we have to do now is write the new value of d0 into the register where the fmov instruction is and quit.

<pre spellcheck="false">wa mov x0, 0x6666666666666666 @0x000009bc
q
</pre>

Then we run our new binary.

<pre spellcheck="false">kali@kali:~/Documents/0x06_double_primitive_datatype$ ./0x06_asm64_double_primitive_datatype
</pre>

<pre spellcheck="false">10.2
</pre>

I hope you enjoyed this series and have a good firm grasp on ARM64 RE!