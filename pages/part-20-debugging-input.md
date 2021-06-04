## Part 20 - Debugging Input

Today we will debug our input function. Let's review our code.

Review&nbsp;__input.c__&nbsp;as follows.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include "pico/stdlib.h"

#define ZERO 0x30
#define NINE 0x39
#define PERIOD 0x2e
#define CAPITAL_A 0x41
#define LOWER_CASE_Z 0x7a
#define BACKSPACE 0x08
#define DEL 0x7f

void input_proc(char type, char* p_usb_char, char* p_usb_string, const int* p_USB_STRING_SIZE)
{
&nbsp; *p_usb_char = '\0';
&nbsp; *p_usb_char = getchar_timeout_us(0);
&nbsp; if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
&nbsp; {
&nbsp; &nbsp; if(p_usb_string[0] != '\0')
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; printf("\b");
&nbsp; &nbsp; &nbsp; printf(" ");
&nbsp; &nbsp; &nbsp; printf("\b");
&nbsp; &nbsp; &nbsp; p_usb_string[strlen(p_usb_string)-1] = '\0';
&nbsp; &nbsp; }
&nbsp; }
&nbsp; if(type == 'f')
&nbsp; {&nbsp;
&nbsp; &nbsp; char* period;
&nbsp; &nbsp; while((*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE) || *p_usb_char == PERIOD)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(*p_usb_char == PERIOD)
&nbsp; &nbsp; &nbsp; &nbsp; period = strchr(p_usb_string, '.');
&nbsp; &nbsp; &nbsp; if(period == NULL)&nbsp;
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; else
&nbsp; &nbsp; &nbsp; &nbsp; break;
&nbsp; &nbsp; }
&nbsp; }
&nbsp; else if(type == 'd')
&nbsp; {&nbsp;
&nbsp; &nbsp; while(*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; }
&nbsp; }
&nbsp; else if(type == 's')
&nbsp; {&nbsp;
&nbsp; &nbsp; while(*p_usb_char &gt;= CAPITAL_A &amp;&amp; *p_usb_char &lt;= LOWER_CASE_Z)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; }
&nbsp; }
}

void flush_input(char* p_usb_string)
{
&nbsp; p_usb_string[0] = '\0';
}
</pre>

Review our&nbsp;__print.c__&nbsp;as follows.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"
#include "input.h"

#define RETURN 0x0d

void print_proc(char* p_usb_char, char* p_usb_string)
{
&nbsp; if(*p_usb_char == RETURN)
&nbsp; {
&nbsp; &nbsp; if(p_usb_string[0] == '\0')
&nbsp; &nbsp; &nbsp; printf("\n");
&nbsp; &nbsp; else
&nbsp; &nbsp; &nbsp; printf("\n%s\n", p_usb_string);
&nbsp; &nbsp; flush_input(p_usb_string);
&nbsp; }
}
</pre>

Review our&nbsp;__main.c__&nbsp;as follows.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"
#include "print.h"
#include "input.h"

int main()
{
&nbsp; stdio_init_all();

&nbsp; const int USB_STRING_SIZE = 100;
&nbsp; char usb_char;
&nbsp; usb_char = '\0';
&nbsp; char usb_string[USB_STRING_SIZE];
&nbsp; usb_string[0] = '\0';
&nbsp;&nbsp;
&nbsp; while(1)
&nbsp; {&nbsp; &nbsp;
&nbsp; &nbsp; input_proc('f', &amp;usb_char, usb_string, &amp;USB_STRING_SIZE);
&nbsp; &nbsp; print_proc(&amp;usb_char, usb_string);
&nbsp; }

&nbsp; return 0;
}
</pre>

Let's fire up in our debugger.

<pre spellcheck="false">radare2 -w arm -b 16 main.elf
</pre>

Let's auto analyze.

<pre spellcheck="false">aaaa
</pre>

Let's seek to main.

<pre spellcheck="false">s main
</pre>

Let's go into visual mode by typing&nbsp;__V__&nbsp;and then&nbsp;__p__&nbsp;twice to get to a good debugger view.

We first review main.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622836839312.jpg"/></div>

We see our _stdio\_init\_all_ call which sets up IO and we see a _0x64_ into _r3_ which is our move of 100 decimal to set _USB\_STRING\_SIZE _and we set up our _usb\_char_ value and init to _0_ and finally _usb\_string_ and init to _0_. 

Lets look at our print\_proc function.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837104639.jpg"/></div>

We first check to see if our pointer to usb\_char or _p\_usb\_char_ is equal to the _RETURN_ key or _0xd_ and if so branch. 

We then iterate over _p\_usb\_string_ until we hit the null terminator and then call our _printf _function which as we can see here is a wrapper to the c printf function. 

We finally _flush\_input_.

Our input\_proc function is a bit more complex.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837449377.jpg"/></div>

Here we use the g_etchar\_timeout\_us_ function and handle the _BACKSPACE_ and _DELETE_ keys.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837675957.jpg"/></div>

We then call our _putchar _wrapper against_ 0_ and _9_ and check the _strlen_ and properly build our string with _strncat_.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837760991.jpg"/></div>

We then properly handle our _PERIOD_ logic to ensure only one _PERIOD _is entered as a floating point number can NOT handle 2 periods.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837842045.jpg"/></div>

We then then properly handle our loop.

Finally we have our flush\_input function.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837919869.jpg"/></div>

Here we simply flush the input buffer by setting _p\_usb\_string_ to a null char.

This was a larger debug session so please take your time and compare the assembly against the source so you can really grasp each paragraph as I cover it here.

In our next lesson we will hack input!