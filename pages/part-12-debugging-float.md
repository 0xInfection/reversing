## Part 12 - Debugging float

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1618059343816.jpg"/></div>

We see the format specifier in _\[0x0000033c\]._

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%f
</pre>

The float is at _\[0x00000340\]_.

<pre spellcheck="false">:&gt; pff @ [0x00000340]
0x00004000 = 9.32830524e-09
</pre>

Do not worry that the float is inaccurate as this machine is x64. What is important to see is the value _0x00004000_. You then ask yourself, hey, that is not _40.5_! What is the deal?

OK...

The Pico does not have its own math coprocessor so it handles floats and doubles using software. Therefore _0x00004000_ would be the representation of _40.5_ decimal.

So if the value was _40.4_, for example, it would be _0x00003333_. Conversely _40.6_ would be _0x00004ccc_.

Take a look at the following table which will help illustrate the point.

<pre spellcheck="false">0x3ff00000 = 1.000000
0x3ff00001 = 1.000001
0x3ff00002 = 1.000002
...
0x3ff0000f = 1.000015
0x3ff00010 = 1.000016
0x3ff00011 = 1.000017
etc...
</pre>

Ultimately the values in these 4 bytes (32-bits) will determine the value of the float.

In our next lesson we will hack the float and demonstrate this logic.