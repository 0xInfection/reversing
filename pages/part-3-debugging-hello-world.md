## Part 3 - Debugging Hello World

Today we will dive into debugging our very simple, "Hello world!", program.

Let's review our code.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{	
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp;   printf("Hello world!\n");

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
    
  return 0;
}
</pre>

Please make sure you build Radare2 from source. Before each lesson PLEASE complete the following.

<pre spellcheck="false">git pull
radare2 sys/install.sh
</pre>

You can check that the version is up to date.

<pre spellcheck="false">radare2 -v

</pre>

In my case, as it will be different for you.

<pre spellcheck="false">radare2 5.2.0-git 25988 @ darwin-x86-64 git.5.1.1
commit: 510ddab0e523bed173b3954e5f61abf395812f7d build: 2021-03-21__05:40:51
</pre>

Now back to our project repo. Let's fire up our debugger.

<pre spellcheck="false">radare2 -w arm -b 16 0x02_hello_world.elf
</pre>

Let's auto analyze.

<pre spellcheck="false">aaaa
</pre>

Let's seek to main.

<pre spellcheck="false">s main
</pre>

Let's go into visual mode by typing __V__ and then __p__ twice to get to a good debugger view.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616343654275.jpg"/></div>

Let's break this very simple program down.

<pre spellcheck="false">push {r4, lr}
</pre>

We are simply setting up our function arguments where we pushing the value of _r4_ and _lr_ (link register) to the stack.

We then bl (branch long) to the _sym.stdio\_init\_all_ function which init's standard input and output.

<pre spellcheck="false">bl sym.stdio_init_all
</pre>

We then load the value at the location _0x00000338_ into the _r4_ register. This is where the, __"Hello world!"__ string lives.

<pre spellcheck="false">ldr r4, [0x00000338]
</pre>

To prove this we can do the following by pressing : inside of the current Visual mode and then typing the following.

<pre spellcheck="false">:&gt; psz @ [0x00000338]
Hello world!
:&gt; psz @ 0x00004cf8
Hello world!
</pre>

As you can clearly see the value inside of _0x00000338 _is the value at _0x0004cf8_.

We then move and set the flags (that is the _s_ in _movs_) the contents of _r4_ into _r0_.

<pre spellcheck="false">movs r0, r4
</pre>

We then branch long to the puts wrapper. The debugger converted our _printf _function in our code to this wrapper function.

<pre spellcheck="false">bl sym.__wrap_puts
</pre>

We then _movs _250 decimal, 0xfa hex, which is 1/4 our 1000 millisecond sleep into _r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

We then logically shift left, 2, and set the flags. This of course multiplies our 250 value by 2 and then again by 2 which takes 250 decimal to 1000 decimal which is our millisecond delay and places that 1000 decimal value into _r0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

If you are not familiar with ARM 32 Assembly instructions, please reference this great table provided by Keil.

https://developer.arm.com/documentation/ddi0210/c/Introduction/Instruction-set-summary/ARM-instruction-summary?lang=en

We then branch long to our _sleep\_ms_ function.

<pre spellcheck="false">bl sym.sleep_ms
</pre>

We then branch unconditional back to _0x328_ which is our while loop.

<pre spellcheck="false">b 0x328
</pre>

You can also see the graph view by pressing __V__ again in the current window.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1616345144033.jpg"/></div>

This is a great way to trace through more elaborate code. I wanted to show you all this as you can use this going forward as you do larger analysis.

In our next lesson we will hack our simple program and convert it back to a __.uf2__ and re-flash to the Pico.