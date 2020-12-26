# Part 10 - Debugging Character Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we hack the char from the last lesson.

Let's fire up radare2 in write mode.

<pre spellcheck="false">radare2 -w ./0x03_asm64_char_primitive_datatype
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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/128900619.jpg"/></div>

You can right click and&nbsp;__Open image in new tab&nbsp;__to get an expanded view.

Let's get back to the terminal view.

<pre spellcheck="false">q
</pre>

All we have to do is write assembly to 0x000009ec and specify a new char of our choosing.

<pre spellcheck="false">[0x000009e4]&gt; wa movz w0, 0x66 @ 0x000009ec
Written 4 byte(s) (movz w0, 0x66) = wx c00c8052
[0x000009e4]&gt;
</pre>

Let's quit and run the new binary from the terminal.

<pre spellcheck="false">[0x000009e4]&gt; q
kali@kali:~/Documents/0x03_asm64_char_primitive_datatype$ ./0x03_asm64_char_primitive_datatype
f
</pre>

<pre spellcheck="false"></pre>

As you can see we successfully and permanently hacked the binary! It is very trivial but when you take the last series of lessons together with each new successive lesson you build a real skill-set!

In our next lesson we will work with the boolean primitive datatype.

  