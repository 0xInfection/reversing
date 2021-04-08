## Part 10 - Hacking int

Today we hack our simple int program. Let's review the code.

__0x04\_int.c__

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; int x = 40;&nbsp;

&nbsp; &nbsp; printf("%d\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Let's fire up in our debugger.

<pre spellcheck="false">radare2 -w arm -b 16 0x04_int.elf
</pre>

Let's auto analyze.

<pre spellcheck="false">aaaa
</pre>

Let's seek to main.

<pre spellcheck="false">s main
</pre>

Let's go into visual mode by typing&nbsp;__V__&nbsp;and then&nbsp;__p__&nbsp;twice to get to a good debugger view.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1617616216893.jpg"/></div>

We are going to first hack the int value which we know is _40_ decimal or _28_ hex.

<pre spellcheck="false">:&gt; wa movs r1, 0x30 @ 0x00000328
Written 2 byte(s) (movs r1, 0x30) = wx 3021
</pre>

Here we see _0x30_ is _48_ decimal.

<pre spellcheck="false">:&gt; ? 0x30
int32 &nbsp; 48
uint32&nbsp; 48
hex &nbsp; &nbsp; 0x30
octal &nbsp; 060
unit&nbsp; &nbsp; 48
segment 0000:0030
string&nbsp; "0"
fvalue: 48.0
float:&nbsp; 0.000000f
double: 0.000000
binary&nbsp; 0b00110000
ternary 0t1210
</pre>

We also see that _0xfa_ which we know is _250_ decimal is our 1/4 millisecond delay that when shifted left twice, multiplies, and becomes _1000_ decimal for 1 second delay.

<pre spellcheck="false">:&gt; ? 0xfa
int32 &nbsp; 250
uint32&nbsp; 250
hex &nbsp; &nbsp; 0xfa
octal &nbsp; 0372
unit&nbsp; &nbsp; 250
segment 0000:00fa
string&nbsp; "\xfa"
fvalue: 250.0
float:&nbsp; 0.000000f
double: 0.000000
binary&nbsp; 0b11111010
ternary 0t100021
</pre>

Let's hack that to _50_ decimal.

<pre spellcheck="false">:&gt; wa movs r0, 0x32 @ 0x00000330
Written 2 byte(s) (movs r0, 0x32) = wx 3220
</pre>

We can see that it is in fact _50_ decimal.

<pre spellcheck="false">:&gt; ? 0x32
int32 &nbsp; 50
uint32&nbsp; 50
hex &nbsp; &nbsp; 0x32
octal &nbsp; 062
unit&nbsp; &nbsp; 50
segment 0000:0032
string&nbsp; "2"
fvalue: 50.0
float:&nbsp; 0.000000f
double: 0.000000
binary&nbsp; 0b00110010
ternary 0t1212
</pre>

Let's also only shift it left once such that it will take _50_ decimal and turn it into _100_ when it shifts left only once.

<pre spellcheck="false">:&gt; wa lsls r0, r0, 1 @ 0x00000332
Written 2 byte(s) (lsls r0, r0, 1) = wx 4000
</pre>

All we have to do now is exit and convert our&nbsp;__.elf&nbsp;__to&nbsp;__.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x04_int.elf 0x04_int.uf2
</pre>

Plug in the Pico and make sure you hold down BOOTSEL or use the setup I provided in the part 2.

<pre spellcheck="false">cp 0x04_int.uf2 /Volumes/RPI-RP2
</pre>

Let's screen it!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

AHH yea!

<pre spellcheck="false">48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
</pre>

Here we see we hacked it to 48 decimal and it is printing every 100 milliseconds!

In our next lesson we will deal with floats and the unique way the Pico handles them as it does not have a co-processor.