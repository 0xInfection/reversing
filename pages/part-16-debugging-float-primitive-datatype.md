## Part 16 - Debugging Float Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to debug our very simple float primitive datatype.

To begin let's open up our binary in Radare2.

<pre spellcheck="false">radare2 ./0x05_asm64_float_primitive_datatype
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

When dealing with floating point numbers in ARM64 we have to understand that we want to locate where the _fmov_ instruction occurs where we take a value from our _w0_ register and move it into the floating point _s0_ register. Here is where all the magic happens!

Let us define a break point right below the _fmov_ instruction. REMEMBER with ASLR your addresses will be different than this example.

<pre spellcheck="false">[0x557931c9b4]&gt; db 0x557931c9c8
[0x557931c9b4]&gt; dc
[0x557931c9b4]&gt; hit breakpoint at: 0x557931c9c8
[0x557931c9c8]&gt; ds
[0x557931c9c8]&gt; dr w0
0x4121999a
[0x557931c9c8]&gt;
</pre>

OK so we see this strange value which if you look at the code below, the _lsl_ which is logical shift left, is moving the byte order of which we are using the _movz_ and _movk_ instructions which _movz_ will move _0x999a_ into _w0_ and then the _movk_ will move _0x4121,_ _lsl 16_ into_ w0_ therefore putting 4121 at the higher order byte locations and the 999a at the lower order byte locations.

<pre spellcheck="false">movz w0, 0x999a
movk w0, 0x4121, lsl 16
fmov s0, w0
</pre>

We move our _w0_ register into _s0_ so we HAVE to change these values here before letting it get into _s0_ otherwise it will be significantly harder to hack in the next lesson.

Lets continue to show our value.

<pre spellcheck="false">[0x557931c9c8]&gt; dc
10.1
(237691) Process exited with status=0x0
[0x7fb948407c]&gt;
</pre>

In our next lesson we will hack this value!