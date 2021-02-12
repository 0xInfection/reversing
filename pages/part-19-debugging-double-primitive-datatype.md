## Part 19 - Debugging Double Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to debug our very simple double primitive datatype.

To begin let's open up our binary in Radare2.

<pre spellcheck="false">radare2 ./0x06_asm64_double_primitive_datatype
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

When dealing with double floating-point numbers in ARM64 we have to understand that we want to locate where the&nbsp;_fmov_&nbsp;instruction occurs where we take a value from our&nbsp;_w0_&nbsp;register and move it into the floating point&nbsp;_d0_&nbsp;register. Here is where all the magic happens! This is just like our floating-point numbers that deal with _s0_.

Let us define a break point right below the&nbsp;_fmov_&nbsp;instruction. REMEMBER with ASLR your addresses will be different than this example.

<pre spellcheck="false">[0x556bf809b4]&gt; db 0x556bf809c4
[0x556bf809b4]&gt; dc
hit breakpoint at: 0x556bf809c4
[0x556bf809c4]&gt; dr w0
0x33333333
</pre>

We move our&nbsp;_w0_&nbsp;register into _d0_ so we HAVE to change these values in _d0_&nbsp;which is different from our float. We will explore this in the next lesson.

Lets continue to show our value.

<pre spellcheck="false">[0x556bf809c4]&gt; dc
10.1
(39979) Process exited with status=0x0
[0x7fa37da0fc]&gt;
</pre>

In our next lesson we will hack this value!