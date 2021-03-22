## Part 4 - Hacking Hello World

In the last lesson we reviewed how to properly debug our very simple binary in __Radare2__. Today we are going to hack that static __.elf __binary and convert it to the __.uf2__ format and flash to our Pico and see the magic happen.

Let's review our very simple program once more.

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

Let's load up our binary.

<pre spellcheck="false">radare2 -w arm -b 16 0x02_hello_world.elf
</pre>

Let's auto analyze.

<pre spellcheck="false">aaaa
</pre>

Let's seek to main.

<pre spellcheck="false">s main
</pre>

Let's use Visual mode and press p twice to get our our favorite debugger view.

<pre spellcheck="false">V
</pre>

Let's review the simple ARM32 Assembly.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616443718242.jpg"/></div>

I would hack this binary in two ways. As we discussed in the last lesson we see the contents inside the memory location _0x00000338_ holding the value of our string. Let's press the colon : and press enter.

<pre spellcheck="false">:&gt; psz @ [0x00000338]
Hello world!
</pre>

Let's review our strings. I want you to pay attention to the, "Hello world!" as you will see two addresses. The one on the left is the physical address and the one directly to the right is the virtual address. We will be concerned with the virtual address. To better understand let's do the following.

<pre spellcheck="false">:&gt; iz~ | less
</pre>

As you can see our string is at the top.

<pre spellcheck="false">[Strings]
nth paddr&nbsp; &nbsp; &nbsp; vaddr&nbsp; &nbsp; &nbsp; len size section type&nbsp; &nbsp; string
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――
0&nbsp; &nbsp;0x00014cf8 0x00004cf8 12&nbsp; 13&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Hello world!
1&nbsp; &nbsp;0x00014d08 0x00004d08 26&nbsp; 27&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;No spinlocks are available
2&nbsp; &nbsp;0x00014d24 0x00004d24 33&nbsp; 34&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Hardware alarm %d already claimed
3&nbsp; &nbsp;0x00014d48 0x00004d48 15&nbsp; 16&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;\n*** PANIC ***\n
4&nbsp; &nbsp;0x00014d5c 0x00004d5c 11&nbsp; 12&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Hard assert
5&nbsp; &nbsp;0x00014d68 0x00004d68 7&nbsp; &nbsp;8&nbsp; &nbsp; .rodata ascii&nbsp; &nbsp;Release
6&nbsp; &nbsp;0x00014d70 0x00004d70 5&nbsp; &nbsp;6&nbsp; &nbsp; .rodata ascii&nbsp; &nbsp;1.0.0
7&nbsp; &nbsp;0x00014d78 0x00004d78 4&nbsp; &nbsp;5&nbsp; &nbsp; .rodata ascii&nbsp; &nbsp;pico
8&nbsp; &nbsp;0x00014d80 0x00004d80 16&nbsp; 17&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;0x02_hello_world
9&nbsp; &nbsp;0x00014d94 0x00004d94 11&nbsp; 12&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Mar 21 2021
10&nbsp; 0x00014db2 0x00004db2 4&nbsp; &nbsp;5&nbsp; &nbsp; .rodata ascii&nbsp; &nbsp;uBhM
11&nbsp; 0x00014dbc 0x00004dbc 10&nbsp; 11&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;UART stdin
12&nbsp; 0x00014dc8 0x00004dc8 11&nbsp; 12&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;UART stdout
13&nbsp; 0x00014dd4 0x00004dd4 19&nbsp; 20&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;UART stdin / stdout
14&nbsp; 0x00014dfc 0x00004dfc 18&nbsp; 19&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;USB stdin / stdout
15&nbsp; 0x00014e1c 0x00004e1c 12&nbsp; 13&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Raspberry Pi
16&nbsp; 0x00014e2c 0x00004e2c 4&nbsp; &nbsp;5&nbsp; &nbsp; .rodata ascii&nbsp; &nbsp;Pico
17&nbsp; 0x00014e34 0x00004e34 12&nbsp; 13&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;000000000000
18&nbsp; 0x00014e44 0x00004e44 9&nbsp; &nbsp;10&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Board CDC
19&nbsp; 0x00014ec4 0x00004ec4 19&nbsp; 20&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Unhandled IRQ 0x%x\n
20&nbsp; 0x00014ed8 0x00004ed8 39&nbsp; 40&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Isochronous wMaxPacketSize %d too large
21&nbsp; 0x00014f00 0x00004f00 30&nbsp; 31&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;ep %d %s was already available
22&nbsp; 0x00014f20 0x00004f20 40&nbsp; 41&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Can't continue xfer on inactive ep %d %s
23&nbsp; 0x00014f4c 0x00004f4c 35&nbsp; 36&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Transferred more data than expected
0&nbsp; &nbsp;0x00020135 0x10000135 5&nbsp; &nbsp;6&nbsp; &nbsp; .data&nbsp; &nbsp;ascii&nbsp; &nbsp;V\n`\eh
1&nbsp; &nbsp;0x0002018b 0x1000018b 5&nbsp; &nbsp;6&nbsp; &nbsp; .data&nbsp; &nbsp;ascii&nbsp; &nbsp;&amp;CF\eh
2&nbsp; &nbsp;0x000201a0 0x100001a0 4&nbsp; &nbsp;5&nbsp; &nbsp; .data&nbsp; &nbsp;ascii&nbsp; &nbsp;CF\ey
3&nbsp; &nbsp;0x000201a8 0x100001a8 4&nbsp; &nbsp;5&nbsp; &nbsp; .data&nbsp; &nbsp;ascii&nbsp; &nbsp;CF\eh
4&nbsp; &nbsp;0x000201d0 0x100001d0 4&nbsp; &nbsp;5&nbsp; &nbsp; .data&nbsp; &nbsp;ascii&nbsp; &nbsp;\thAq
5&nbsp; &nbsp;0x0002028d 0x1000028d 5&nbsp; &nbsp;6&nbsp; &nbsp; .data&nbsp; &nbsp;ascii&nbsp; &nbsp;GpF\t8
6&nbsp; &nbsp;0x00020805 0x10000805 5&nbsp; &nbsp;11&nbsp; &nbsp;.data&nbsp; &nbsp;utf16le \a \b \b
7&nbsp; &nbsp;0x00020905 0x10000905 5&nbsp; &nbsp;11&nbsp; &nbsp;.data&nbsp; &nbsp;utf16le \b \t \t
8&nbsp; &nbsp;0x00020a05 0x10000a05 5&nbsp; &nbsp;11&nbsp; &nbsp;.data&nbsp; &nbsp;utf16le \t \n \n
9&nbsp; &nbsp;0x00020b05 0x10000b05 5&nbsp; &nbsp;11&nbsp; &nbsp;.data&nbsp; &nbsp;utf16le \n \v \v
(END)
</pre>

You can see the value of _0x00004cf8_ holds our string to prove it we can do the following.

<pre spellcheck="false">:&gt; psz @ 0x00004cf8
Hello world!
</pre>

Let's hack this.

<pre spellcheck="false">:&gt; w Hacked World! @ [0x00000338]
</pre>

Let's now verify the value is changed.

<pre spellcheck="false">:&gt; psz @ 0x00004cf8
Hacked World!
</pre>

The other thing I would like to hack is the sleep\_ms which is currently set at 1000. Remember it is showing 250 decimal or 0xfa hex and we logical shift left twice as we discuss in the last lesson. The first logical shift left will multiply by 2 bringing us to 500 and the 2nd logical shift left will multiply by 2 brining us to 1000.

<pre spellcheck="false">lsls r0, r0, 2&nbsp;
</pre>

Let's hack this by changing the 2 to a 1. This will make the delay 500 ms or a half a second.

<pre spellcheck="false">:&gt; wa lsls r0, r0, 1 @ 0x00000330
Written 2 byte(s) (lsls r0, r0, 1) = wx 4000
</pre>

Let's verify.

<pre spellcheck="false">:&gt; pd 1 @ 0x00000330
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0x00000330&nbsp; &nbsp; &nbsp; 4000 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lsls r0, r0, 1
</pre>

We can clearly see it changed.

All we have to do now is exit and convert our __.elf __to __.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x02_hello_world.elf 0x02_hello_world.uf2
</pre>

Plug in the Pico and make sure you hold down BOOTSEL or use the setup I provided in the last lesson.

<pre spellcheck="false">cp 0x02_hello_world.uf2 /Volumes/RPI-RP2
</pre>

Let's screen it!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

AHH yea!

<pre spellcheck="false">Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
</pre>

Every half a second!

Next lesson we will discuss variables.