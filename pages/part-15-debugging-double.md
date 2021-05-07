## Part 15 - Debugging double

Let's review&nbsp;__0x06\_double.c__&nbsp;as follows.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; double x = 40.5;

&nbsp; &nbsp; printf("%f\n", x);&nbsp;

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1618860188501.jpg"/></div>

We see the format specifier in&nbsp;_\[0x0000033c\]._

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%f
</pre>

The double is at&nbsp;_\[0x00000340\]_.

<pre spellcheck="false">:&gt; pff @ [0x00000340]
0x00004000 = 9.32830524e-09
</pre>

Ok... Same deal as the float lesson so why did I waste time on choosing 40.5?

I wanted to show you definitive proof that the compiler will treat this the same as it is within the bounds of a float when the Pico SDK functionality does it's magic as there is NO co-processor.

Let's examine a MOD to our program.

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

When we compile and run this program we get the following.

<pre spellcheck="false">40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
</pre>

OK well... This looks different. Let us for the first time in this course look at a Dynamic Reverse Engineering analysis in GDB.

It is NOT critical here that you run this and set this all up in GDB as there are a great deal of steps in addition to another Pico needed in a configuration such as the following below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1618861896464.jpg"/></div>

The scope of this course is to understand Static Reverse Engineering however I wanted to depart and show you what GDB is showing us with this new binary.

It is NOT necessary to use Dynamic Reverse Engineering unless you are dealing with a situation where you have a packed binary that you have to dynamically load and write out the code. It does make things easier when you are using Dynamic Reverse Engineering however I want to show you that Static Reverse Engineering can get you everything you need without having to set up a remote process to actually run the binary on.

If you did find it necessary to try this you would need to first install the OpenOCD repo into the pico folder that we created at the beginning of this course. You can find details at the link below and go to __5.1 Installing OpenOCD__ in the datasheet.

https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf

You will then need to visit the page below and download the uf2 located at __Debugging using another Raspberry Pi Pico __and then flash the first Pico with the uf2.

https://www.raspberrypi.org/documentation/rp2040/getting-started/\#board-specifications

__TERMINAL 1__: You will then need to set up a first terminal to go into the openocd folder and run the following.

<pre spellcheck="false">src/openocd -f interface/picoprobe.cfg -f target/rp2040.cfg -s tcl
</pre>

__TERMINAL 2__: You will need to go into the build folder of your project and run the following.

<pre spellcheck="false">arm-none-eabi-gdb 0x06_double.elf
target extended-remote localhost:3333
load
monitor reset init
b main
c
</pre>

__TERMINAL 3__: You will need to run the screen emulator which will start with a blinking cursor.

<pre spellcheck="false">screen /dev/tty.usbmodem14101 115200
</pre>

Nonetheless with that brief explanation, lets' review this dynamically in GDB.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1618862002127.jpg"/></div>

We see two values at _0x10000340_ and _0x10000344_.

Let's delete all breakpoints and break right before the call to the printf wrapper.

<pre spellcheck="false">d
b *0x1000032e
c
</pre>

Let's examine the values at each of these locations.

<pre spellcheck="false">p/x *0x10000340
0x71c71c72

p/x *0x10000344
0x4044471c

</pre>

We know that the following output is what prints.

<pre spellcheck="false">40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
40.5555555560000000
</pre>

What is happening is that these values are now in R2 and R3 respectively.

<pre spellcheck="false">p/x $r2
0x71c71c72

p/x $r3
0x4044471c
</pre>

In ARM 32 Assembly the arguments to the functions are passed in r0-r3 and if you need more args they are put on the stack. In our case r0 has our format modifier.

<pre spellcheck="false">x/s $r0
0x10007070:	"%.16f\n"
</pre>

We see in r1 a value pointing to the stack.

<pre spellcheck="false">x/w $r1
0x0:	0x20041f00

p/x *0x20041f00
0xa
</pre>

This is another piece going into the printf wrapper in order to properly print the string to the STDOUT.

In our next lesson we will hack statically.