# Part 3 - "Hello World"

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to debug our first program utilizing our dev build of Radare2.

If this is your first time working with Assembly I would encourage you check out this series as it may better prepare you for the upcoming lessons.

<iframe allowfullscreen="true" class="center lazy-loaded" frameborder="0" height="294" src="https://www.linkedin.com/embeds/publishingEmbed.html?articleId=7574498398602237511" title="mytechnotalent/Reverse-Engineering-Tutorial" width="744"></iframe>

To begin let's open up our binary in Radare2.

<pre spellcheck="false">radare2 ./0x01_asm_64_helloworld
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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/767397257.jpg"/></div>

You can right click and __Open image in new tab __to get an expanded view.

Remember there is a difference between an executable on disk and what resides when it is mapped. When it is on disk it is referred to as unmapped. We will look at that at the end of the lesson. For now we are looking at a mapped version as you see it is an offset of the mapped code we will examine later.

Do you notice that as your mapped memory values are different than mine? That is because of ALSR.

Address Space Layout Randomization (ASLR) is a security technique used in operating systems, first implemented in 2001. The current versions of all major operating systems (iOS, Android, Windows, macOS, and Linux) feature ASLR protection.

ASLR is primarily used to protect against buffer overflow attacks. In a buffer overflow, attackers feed a function as much junk data as it can handle, followed by a malicious payload.

We notice in my mapped memory that at address _0x55629cab48_ we see our string_ "Hello World!"_. You will have a different offset as we discussed but will find the same result.

Let us get back to a console window by doing the following.

<pre spellcheck="false">q
</pre>

Let's verify our initial analysis.

<pre spellcheck="false">[0x55629ca9e4]&gt; ps @0x55629cab48
Hello World!
[0x55629ca9e4]&gt;
</pre>

We can see that it is in fact true that at the mapped memory address of _0x55629cab48_ we see the string _"Hello World!"_.

Let's also look at the hex view so we can see and better understand what is going on at the machine code level.

<pre spellcheck="false">px @0x55629cab48
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/563534516.jpg"/></div>

We see our "Hello World!" string and we can again see that it exists starting at the mapped memory address of 0x55629cab48.

We see that our machine code instructions are 16 bytes long or 64-bits long as we can see the first column start at _48_ and end with _00_.

It is VERY important we understand a few key things. First is the fact that a single hex digit is 4-bits wide or a nibble or a half of a byte. In our case _4_ is a half of a byte and _8_ is the other half of the byte. Together they form a byte and in our case a valid ascii char code.

Let's visit the online ascii table.

<iframe allowfullscreen="true" class="center lazy-load" data-delayed-url="https://www.linkedin.com/embeds/publishingEmbed.html?articleId=7387163987651632632" frameborder="0" height="104" src="about:blank" title="ASCII Table and Description" width="744"></iframe>

Second, we need to understand what the machine code translates to. Let's look up what _48_ is in hex. We see that it is a capital 'H'. That maps perfectly as you see in the right hand column of the image above we see a 0 and below it the letter H.

Obviously _65_ hex is ___'e'___ and so on and so forth. You can extrapolate the rest for yourself now that you have a basic understanding of what you are looking at.

Let's now define a breakpoint on main and execute this binary to verify in fact that when we continue on from main it will print _"Hello World"_ to the stdout.

<pre spellcheck="false">[0x55629ca9e4]&gt; db 0x55629ca9e4
[0x55629ca9e4]&gt;
</pre>

Let us continue and verify our hypothesis. First we continue and break on main.

<pre spellcheck="false">[0x55629ca9e4]&gt; dc
hit breakpoint at: 0x55629ca9e4
[0x55629ca9e4]&gt;
</pre>

Now we step again and since there are no other breakpoints we will conclude the execution and verify our result in stdout.

<pre spellcheck="false">[0x55629ca9e4]&gt; dc
Hello World!
(59575) Process exited with status=0x0
[0x7fb146cb8c]&gt;
</pre>

Let's exit Radare2.

<pre spellcheck="false">q
y
y
</pre>

Let us rerun Radare2 again and this time not run the binary and simply look at the unmapped binary that is on disk.

<pre spellcheck="false">radare2 ./0x01_asm_64_helloworld
</pre>

Let's auto analyze.

<pre spellcheck="false">aaa
</pre>

Let's seek to main.

<pre spellcheck="false">s main
</pre>

Then view.

<pre spellcheck="false">v
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/75880496.jpg"/></div>

You can right click and __Open image in new tab __to get an expanded view.

Notice that we have _"Hello World!"_ this time at the unmapped memory address of _0xb48_. You notice that when you ran the binary the executable had an offset to this value but the LSB were _48_ hex.

I hope this lesson helps you to understand the basics of 64-bit ARM assembly and how to reverse it properly.

In our next lesson we will hack the value.