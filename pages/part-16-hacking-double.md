## Part 16 - Hacking double

Let's review&nbsp;__0x06\_double\_MOD.c__&nbsp;as follows.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; double x = 40.55555555555555555555;

&nbsp; &nbsp; printf("%.16f\n", x)&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Let's fire up in our debugger.

<pre spellcheck="false">radare2 -w arm -b 16 0x06_double.elf
</pre>

Let's auto analyze.

<pre spellcheck="false">aaaa
</pre>

Let's seek to main.

<pre spellcheck="false">s main
</pre>

Let's go into visual mode by typing&nbsp;__V__&nbsp;and then&nbsp;__p__&nbsp;twice to get to a good debugger view.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1620377345934.jpg"/></div>

Our microcontroller is a little endian architecture as we have discussed before therefore if we are going to change our 40.5555555560000000 to 1.0 we need to put that value in reverse byte order therefore...

<pre spellcheck="false">0x3ff00000
</pre>

Needs to be...

<pre spellcheck="false">0x0000f03f
</pre>

Therefore we need to change the value at the following.

<pre spellcheck="false">wx 0x0000f03f @ 0x00000344
</pre>

All we have to do now is exit and convert our&nbsp;__.elf&nbsp;__to&nbsp;__.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x06_double.elf 0x06_double.uf2
</pre>

Plug in the Pico and make sure you hold down BOOTSEL or use the setup I provided in the part 2.

<pre spellcheck="false">cp 0x06_double.uf2 /Volumes/RPI-RP2
</pre>

Let's screen it!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

AHH yea!

<pre spellcheck="false">1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
</pre>

Now we should have a good understanding of the data types within C to look at some slightly larger concepts.

In our next lesson we will begin to discuss input.