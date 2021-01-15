## Part 14 - Hacking Boolean Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we hack the boolean from the last lesson.

Let's fire up radare2 in write mode.

<pre spellcheck="false">radare2 -w ./0x04_asm64_boolean_primitive_datatype
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

All we have to do is write assembly to _0x00000009bc_ and specify _0x0_.

<pre spellcheck="false">[0x000009b4]&gt; wa movz w0, 0x0 @ 0x00000009bc
Written 4 byte(s) (movz w0, 0x0) = wx 00008052
</pre>

<pre spellcheck="false">[0x000009b4]&gt;
</pre>

Let's quit and run the new binary from the terminal.

<pre spellcheck="false">[0x000009b4]&gt; q
kali@kali:~/Documents/0x04_asm64_boolean_primitive_datatype$ ./0x04_asm64_boolean_primitive_datatype
</pre>

<pre spellcheck="false">0
</pre>

As you can see we successfully and permanently hacked the binary! What was originally _true_ or _1_ is now _false _or _0_.

In our next lesson we will work with the integer primitive datatype.