## Part 7 - Hacking char

Today we hack the simple char program.

Let's review our code.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; char x = 'x';
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; &nbsp; printf("%c\n", x);

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; return 0;
}
</pre>

Let's fire up our debugger.

<pre spellcheck="false">radare2 -w arm -b 16 0x03_char.elf
</pre>

Let's auto analyze.

<pre spellcheck="false">aaaa
</pre>

Let's seek to main.

<pre spellcheck="false">s main
</pre>

Let's go into visual mode by typing&nbsp;__V__&nbsp;and then&nbsp;__p__&nbsp;twice to get to a good debugger view.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616750858178.jpg"/></div>

In our last lesson we broke down each line. Here we are clearly interested in hacking the value of 0x78 and changing that to anything we want. Let's try 0x79. This simple hack will turn the char _'x'_ into _'y'_.

<pre spellcheck="false">:&gt; wa movs r1, 0x79 @ 0x00000328
Written 2 byte(s) (movs r1, 0x79) = wx 7921
</pre>

Let's verify the change.

<pre spellcheck="false">:&gt; pd 1 @ 0x00000328
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ; CODE XREF from main @ 0x338
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0x00000328&nbsp; &nbsp; &nbsp; 7921 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; movs r1, 0x79 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ; 'y' ; arg1
</pre>

In this case our debugger is even telling us it is in fact _'y'_ in addition to now we are moving the hex ascii value into 0x79 into _r1_.

Let's also hack the sleep time to 2000 ms or 2 seconds.

<pre spellcheck="false">:&gt; wa lsls r0, r0, 3 @ 0x00000332
Written 2 byte(s) (lsls r0, r0, 3) = wx c000
</pre>

Here we simply logical shift left 3 times therefore 250 x 2 = 500, 500 x 2 = 1000, 1000 x 2 = 2000.

Let's verify.

<pre spellcheck="false">:&gt; pd 1 @ 0x00000332
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0x00000332&nbsp; &nbsp; &nbsp; c000 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lsls r0, r0, 3
</pre>

All we have to do now is exit and convert our&nbsp;__.elf&nbsp;__to&nbsp;__.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x03_char.elf 0x03_char.uf2
</pre>

Plug in the Pico and make sure you hold down BOOTSEL or use the setup I provided in the part 2.

<pre spellcheck="false">cp 0x03_char.uf2 /Volumes/RPI-RP2
</pre>

Let's screen it!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

AHH yea!

<pre spellcheck="false">y
y
y
y
y
y
</pre>

We see 'y' printed out every 2 seconds!

In our next lesson we will discuss the int data type.