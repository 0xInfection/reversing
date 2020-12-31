## Part 7 - Debugging Basic I/O

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to debug our very basic input validation program from last lecture.

To begin let's open up our binary in Radare2.

<pre spellcheck="false">radare2 ./0x02_asm_64_basicio
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

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607682836896.jpg"/></div>

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607683092302.jpg"/></div>

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607683246880.jpg"/></div>

A couple things to note we see at _0x5566be00cc_ the output of _"Enter Age: "_ and at _0x5566be017c_ a call to _istream_ which is going to capture the values from _stdin_ to which we identify a failure condition at 0x5566be01d0 where we find _"Dude be real!"_ and we see the results of a proper input validation starting at _0x5566be0218 _where we say _"You are "_ and then we see a call to the output stream at _0x5566be0238_ and then the continuation of the validation string at _0x5566be0244_ where we say _" years old, seems legit!"_.

The next step is to look at the binary with a visual graph.

<pre spellcheck="false">q
VV
ppppp
</pre>

We see the following:

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607685699956.jpg"/></div>

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607685723107.jpg"/></div>

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607685740119.jpg"/></div>

This is our zoomed out visual graph. We can see how the program moves from function to function. You will notice there are a series of tags such as \[ol\] or \[ok\] and you can literally type the following:

<pre spellcheck="false">p
ol
</pre>

Now we are inside that function:

<div class="slate-resizable-image-embed slate-image-embed__resize-bleed"><img src="/imgs/1607686001944.jpg"/></div>

Then to go back to main.

<pre spellcheck="false">qq
s main
VV
</pre>

This will take us to an expanded graph that we can also use our arrow keys to look around.

Let's set a breakpoint at _0x5566be00c4_ where we _bne 0x5566be0214_ which is where we see the success route of our binary.

<pre spellcheck="false">[0x5566be0194]&gt; db 0x5566be00c4
[0x5566be0194]&gt; dc
hit breakpoint at: 0x5566be00c4
Enter Age: 33
hit breakpoint at: 0x5566be00c4
[0x5566be0194]&gt; dc
Your are 33 years old, seems legit!
(2215) Process exited with status=0x0
</pre>

As you can see we cycled the loop and entered in a correct validation and was able to get our success return.

In our next lesson we will hack the validation.