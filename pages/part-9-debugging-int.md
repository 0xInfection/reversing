## Part 9 - Debugging int

Today we are going to debug our very simple int program. Let's review the code.

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
</pre>

<pre spellcheck="false">}
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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1617350497179.jpg"/></div>

We start out by setting up our main return value.

<pre spellcheck="false">push {r4, lr}
</pre>

We call the standard I/O init.

<pre spellcheck="false">bl sym.stdio_init_all
</pre>

We then load our format modifier %d into&nbsp;_r4_.

<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>

We can prove it.

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%d
</pre>

We then load our int&nbsp;_'40'_&nbsp;into&nbsp;_r1 _which is _0x28_ hex.

<pre spellcheck="false">movs r1, 0x28
</pre>

We can prove it.

<pre spellcheck="false">:&gt; ? 0x28
int32 &nbsp; 40
uint32&nbsp; 40
hex &nbsp; &nbsp; 0x28
octal &nbsp; 050
unit&nbsp; &nbsp; 40
segment 0000:0028
string&nbsp; "("
fvalue: 40.0
float:&nbsp; 0.000000f
double: 0.000000
binary&nbsp; 0b00101000
ternary 0t1111
</pre>

We then move our format modifier into&nbsp;_r0_.

<pre spellcheck="false">movs r0, r4&nbsp;
</pre>

We then branch long to the printf wrapper and call it.

<pre spellcheck="false">bl sym.__wrap_printf

</pre>

We then move 250 decimal or 0xfa hex into&nbsp;_r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

We then move 250 decimal, which we know when logical shift left twice will be 1,000 decimal or 0xfa hex into&nbsp;_r0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

We then call the sleep\_ms function.

<pre spellcheck="false">bl sym.sleep_ms
</pre>

We then continue the while loop infinitely.

<pre spellcheck="false">b 0x328
</pre>

In our next lesson we will hack this very simple binary.