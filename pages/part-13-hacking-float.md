## Part 13 - Hacking float

Let's review our example.&nbsp;__0x05\_float.c__&nbsp;as follows.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; float x = 40.5;

&nbsp; &nbsp; printf("%f\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Let's fire up in our debugger.

<pre spellcheck="false">radare2 -w arm -b 16 0x05_float.elf
</pre>

Let's auto analyze.

<pre spellcheck="false">aaaa
</pre>

Let's seek to main.

<pre spellcheck="false">s main
</pre>

Let's go into visual mode by typing&nbsp;__V__&nbsp;and then&nbsp;__p__&nbsp;twice to get to a good debugger view.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1618389543453.jpg"/></div>

The float is at&nbsp;_\[0x00000340\]_.

<pre spellcheck="false">:&gt; pff @ [0x00000340]
0x00004000 = 9.32830524e-09
</pre>

As we discussed in the last lesson, do not worry that the float is inaccurate as this machine is x64. What is important to see is the value&nbsp;_0x00004000_.

In our last lesson we also explained the way the Pico handles floats. Let's review some basics.

<pre spellcheck="false">0x3ff00000 = 1.000000
0x3ff00001 = 1.000001
0x3ff00002 = 1.000002
...
0x3ff0000f = 1.000015
0x3ff00010 = 1.000016
0x3ff00011 = 1.000017
etc...
</pre>

Let's hack to 1.000000 as follows.

Our microcontroller is a little endian architecture therefore if we are going to change our 40.5 to 1.0 we need to put that value in reverse byte order therefore...

<pre spellcheck="false">0x3ff00000
</pre>

Needs to be...

<pre spellcheck="false">0x0000f03f
</pre>

Therefore we need to change the value at

<pre spellcheck="false">wx 0x0000f03f @ 0x00000340
</pre>

All we have to do now is exit and convert our&nbsp;__.elf&nbsp;__to&nbsp;__.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x05_float.elf 0x05_float.uf2
</pre>

Plug in the Pico and make sure you hold down BOOTSEL or use the setup I provided in the part 2.

<pre spellcheck="false">cp 0x05_float.uf2 /Volumes/RPI-RP2
</pre>

Let's screen it!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

AHH yea!

<pre spellcheck="false">1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
</pre>

Here we have hacked the value to 1.000000 and we let the 1 second sleep to persist.

In our next lesson we will discuss the double data type.