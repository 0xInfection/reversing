## Part 8 - Hacking Basic I/O

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we hack the input validation from our last lesson.

Let's fire up radare2 in write mode.

<pre spellcheck="false">radare2 -w ./0x02_asm_64_basicio
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

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607709949903.jpg"/></div>

Let's get back to the terminal view.

<pre spellcheck="false">q
</pre>

Let's look at the visual graph and begin with the first _b.ne_ which under the proper expected conditions it will only accept a valid integer between _0_ and _100_ as we demonstrated in the last lecture.

The _b.ne_ meaning _branch if not equal_. The assembly before it simply does not matter in this case as we know if we leave b.ne as is the input validation will be in tact.

We need to disable this input validation by changing that instruction to a _b.eq_ or _branch if equal_.

Let's look at that code block.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1607710722312.jpg"/></div>

We see that it if it is true, meaning validation is correct and we have an integer between 0 and 100 we will follow the true green line to the next function which is as follows:

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607710870812.jpg"/></div>

If we fail the validation we will be sent to the false condition to obtain new input:

<div class="slate-resizable-image-embed slate-image-embed--active slate-image-embed__resize-bleed"><img src="/imgs/1607710976917.jpg"/></div>

Let's q to a terminal prompt.

<pre spellcheck="false">qq
</pre>

Let's seek to the statement we want to hack.

<pre spellcheck="false">[0x000010a4]&gt; s 0x000010c4
</pre>

Let's now hack the branch as discussed.

<pre spellcheck="false">[0x000010c4]&gt; wa b.eq 0x1214
Written 4 byte(s) (b.eq 0x1214) = wx 800a0054
[0x000010c4]&gt;
</pre>

Let's quit.

<pre spellcheck="false">q
</pre>

Now when we run the binary it will simply ignore any input at all let alone input validation and simply arrive at the desired point.

<pre spellcheck="false">kali@kali:~/Documents/0x02_asm_64_basicio$ ./0x02_asm_64_basicio
Your are 0 years old, seems legit!
kali@kali:~/Documents/0x02_asm_64_basicio$
</pre>

Even though 0 is valid it is simply an unstable value that happened to be in one of the registers that the program expected to be properly assigned during a normal program flow. Here we were able to change the binary permanently to accomplish our hack.

These are VERY simple examples however when you combine these as you progress you will literally be able to Reverse Engineer anything.

In our next lesson we will discuss the char primitive data type.

  