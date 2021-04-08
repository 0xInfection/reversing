## Part 6 - Debugging char

Today we debug the char program. Let's review the code.

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616704139039.jpg"/></div>

We start out by setting up our main return value.

<pre spellcheck="false">push {r4, lr}
</pre>

We call the standard I/O init.

<pre spellcheck="false">bl sym.stdio_init_all
</pre>

We then load our format modifier %c into _r4_.

<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>

We can prove it.

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%c
</pre>

We then load our char _'x'_ into _r1_.

<pre spellcheck="false">movs r1, 0x78
</pre>

https://www.asciitable.com

You can check with above site that 0x78 hex is _'x'_.

We then move our format modifier into _r0_.

<pre spellcheck="false">movs r0, r4&nbsp;
</pre>

We then branch long to the printf wrapper and call it.

<pre spellcheck="false">bl sym.__wrap_printf

</pre>

We then move 250 decimal or 0xfa hex into _r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

We then move 250 decimal, which we know when logical shift left twice will be 1,000 decimal or 0xfa hex into _r0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

We then call the sleep\_ms function.

<pre spellcheck="false">bl sym.sleep_ms
</pre>

We then continue the while loop infinitely.

<pre spellcheck="false">b 0x328
</pre>

In our next lesson we will hack the char data type.