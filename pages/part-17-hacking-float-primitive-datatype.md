## Part 17 - Hacking Float Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we hack the float from the last lesson.

First update our radare2 source code.

<pre spellcheck="false">cd radare2
git pull
sys/user.sh
</pre>

If you did not follow the instructions earlier you have to build radare2 from source for this to work as they rarely update releases.

https://github.com/radareorg/radare2

If you do not have the repo, clone it and follow the instructions above.

Let's fire up radare2 in write mode.

<pre spellcheck="false">radare2 -w ./0x05_asm64_float_primitive_datatype
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

We need to hack two instructions here. Let's examine two very specific instructions.

<pre spellcheck="false">movz w0, 0x999a
movk w0, 0x4121, lsl 16
</pre>

Remember from last week that ultimately w0 is going to hold _0x4121999a_ as the _lsl_ moves the bites in reverse byte order.

Currently this will produce a float of _10.1_ as we have seen in the prior lessons. It is critical that you understand that in floating-point numbers there is a _mantissa_ which in our case is _10_ and an _exponent_ which is the _1_ to which they are separated by a_ ._ which ties them together.

Therefore to get _10.2_ we would need to write assembly and update these instructions.

<pre spellcheck="false">[0x000009b4]&gt; wa movz w0, 0x3333 @0x000009bc
[0x000009b4]&gt; wa movk w0, 0x4123, lsl 16 @0x000009c0
q

</pre>

Now run the binary!

<pre spellcheck="false">kali@kali:~/Documents/0x05_float_primitive_datatype$ ./0x05_float_primitive_datatype
10.2
</pre>

I want you to take a close look at some examples I have put together for you so that you can understand how different values result in different results. Keep in mind these results are in an active debug session so the addresses will be different so your ASLR will have different values.

<pre spellcheck="false">[0x555e6c29c4]&gt; dr w0 = 0x4122999a
0x4121999a -&gt;0x4122999a
[0x555e6c29c4]&gt; dc
hit breakpoint at: 0x555e6c29c8
[0x555e6c29c8]&gt; dc
10.1625
(238252) Process exited with status=0x0

[0x556215e9c4]&gt; dr w0 = 0x41235555
0x4121999a -&gt;0x41235555
[0x556215e9c4]&gt; dc
hit breakpoint at: 0x556215e9c8
[0x556215e9c8]&gt; dc
10.2083
(238258) Process exited with status=0x0

[0x558216c9c4]&gt; dr w0 = 0x4123599a
0x4121999a -&gt;0x4123599a
[0x558216c9c4]&gt; dc
hit breakpoint at: 0x558216c9c8
[0x558216c9c8]&gt; dc
10.2094
(238257) Process exited with status=0x0

[0x55868a79c4]&gt; dr w0 = 0x4123999a
0x4121999a -&gt;0x4123999a
[0x55868a79c4]&gt; dc
hit breakpoint at: 0x55868a79c8
[0x55868a79c8]&gt; dc
10.225
(238253) Process exited with status=0x0

[0x55826479c4]&gt; dr w0 = 0x41233333
0x4121999a -&gt;0x41233333
[0x55826479c4]&gt; dc
hit breakpoint at: 0x55826479c8
[0x55826479c8]&gt; dc
10.2
(238259) Process exited with status=0x0

[0x55716ab9c4]&gt; dr w0 = 0x4125999a
0x4121999a -&gt;0x4125999a
[0x55716ab9c4]&gt; dc
hit breakpoint at: 0x55716ab9c8
[0x55716ab9c8]&gt; dc
10.35
(238250) Process exited with status=0x0

[0x55880169c4]&gt; dr w0 = 0x412f999f
0x4121999a -&gt;0x412f999f
[0x55880169c4]&gt; dc
hit breakpoint at: 0x55880169c8
[0x55880169c8]&gt; dc
10.975
(238245) Process exited with status=0x0

[0x559130d9c4]&gt; dr w0 = 0x412ff99e
0x4121999a -&gt;0x412ff99e
[0x559130d9c4]&gt; dc
hit breakpoint at: 0x559130d9c8
[0x559130d9c8]&gt; dc
10.9984
(238246) Process exited with status=0x0

[0x557b1b39c4]&gt; dr w0 = 0x412fff9e
0x4121999a -&gt;0x412fff9e
[0x557b1b39c4]&gt; dc
hit breakpoint at: 0x557b1b39c8
[0x557b1b39c8]&gt; dc
10.9999
(238247) Process exited with status=0x0

[0x55931439c4]&gt; dr w0 = 0x412ffffe
0x4121999a -&gt;0x412ffffe
[0x55931439c4]&gt; dc
hit breakpoint at: 0x55931439c8
[0x55931439c8]&gt; dc
11
(238248) Process exited with status=0x0
</pre>

You can start to see patterns here. TAKE THE TIME AND ACTUALLY TRY THESE OUT so you have a better understand of how these values ultimately go into the s0 register!

Next lesson we will discuss doubles.