## Part 10 - Debugging Character Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to debug our very simple character primitive datatype.

To begin let's open up our binary in Radare2.

<pre spellcheck="false">radare2 ./0x03_asm64_char_primitive_datatype
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

We can see that at _0x5576bff9ec_ we are moving _0x63_ or ascii _'c'_ into the _w0_ register. REMEMBER your address will be different due to ASLR.

Let's set a breakpoint at&nbsp;_0x5576bff9ec_&nbsp;and verify the contents.

<pre spellcheck="false">[0x5576bff9e4]&gt; db 0x5576bff9ec
[0x5576bff9e4]&gt; dc
hit breakpoint at: 0x5576bff9ec
[0x5576bff9ec]&gt; dr w0
0x00000001
[0x5576bff9ec]&gt; ds
[0x5576bff9ec]&gt; dr w0
0x00000063
[0x5576bff9ec]&gt;

</pre>

This is very simple but let's break it down. We set our breakpoint and continued. We looked inside the register w0 and saw that the value is 0x01.

We then stepped once and looked again to see that 0x63 was successfully moved into w0 as now we see it does in fact contain 0x63.

If we dc again we see it echoed to the stdout as expected.

<pre spellcheck="false">[0x5576bff9ec]&gt; dc
c
(10845) Process exited with status=0x0
[0x7f9727503c]&gt;
</pre>

In our next lesson we will hack the char to another value of our choice.