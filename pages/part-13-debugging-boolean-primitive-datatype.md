## Part 13 - Debugging Boolean Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to debug our very simple boolean primitive datatype.

To begin let's open up our binary in Radare2.

<pre spellcheck="false">radare2 ./0x04_asm64_boolean_primitive_datatype
</pre>

Let's take advantage of Radare2's auto analysis feature.

<pre spellcheck="false">aaa
</pre>

The next thing we want to do logically is fire up the program in debug mode so it maps the raw machine code from disk to a running process.

<pre spellcheck="false">ood
</pre>

Now that we have a running instance we can seek to the main entry point of the binary.

<pre spellcheck="false">s main
</pre>

Let us take an initial examination by doing the following.

<pre spellcheck="false">v
</pre>

We see in _0x55718999bc_ _movz w0, 0x1_or moving _0x1_ into _w0_ which is our bool true. REMEMBER your address will be different due to ASLR.

Let's set a breakpoint at _0x55718999bc_ and verify the contents.

<pre spellcheck="false">[0x55718999b4]&gt; db 0x55718999bc
[0x55718999b4]&gt; dc
</pre>

<pre spellcheck="false">hit breakpoint at: 0x55718999bc
</pre>

<pre spellcheck="false">[0x55718999bc]&gt; ds
[0x55718999bc]&gt; dr w0
0x00000001
[0x55718999bc]&gt;
</pre>

Very simply we broke right before the value _0x1_ was to be placed in _w0_ and then we stepped and saw that it was in fact _0x1_ inside of _w0_ after the step. This means that our program successfully put a _1 _or _true_ into the _w0_ register which matches what our source code created.

If we dc again we see it echoed to the stdout as expected.

<pre spellcheck="false">[0x55718999bc]&gt; dc
1
(96445) Process exited with status=0x0
</pre>

<pre spellcheck="false">[0x7fac4f903c]&gt;
</pre>

In our next lesson we will hack the boolean to make it 0.