## Part 5 - Hacking "Hello World"

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

In the last lesson we spent a good deal of time really understanding what is going on inside our binary. This laid the groundwork for an easy hack.

Let's fire up radare2 in write mode.

<pre spellcheck="false">radare2 -w ./0x01_asm_64_helloworld
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

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1606475269047.jpg"/></div>

We see the memory addresses as they are on disk as we are not running the binary as we discussed in the last lesson.

We see that at __0xb48__ we very easily find our string.

Let's get back to the terminal view.

<pre spellcheck="false">q
</pre>

Let's verify the string.

<pre spellcheck="false">[0x000009e4]&gt; ps @0xb48
Hello World!
[0x000009e4]&gt;

</pre>

Let's hack the string.

<pre spellcheck="false">[0x000009e4]&gt; w Hacked World @0xb48
</pre>

Let's verify the hack.

<pre spellcheck="false">[0x000009e4]&gt; ps @0xb48
Hacked World
[0x000009e4]&gt;
</pre>

Let's quit radare2.

<pre spellcheck="false">q
</pre>

Now let's run our binary again!

<pre spellcheck="false">./0x01_asm_64_helloworld
Hacked World
</pre>

We see that we very easily hacked the binary. These lessons will help you understand how an attacker creates a workflow so you can learn how to anticipate and better reverse engineer.

In our next lesson we will work with simple I/O.