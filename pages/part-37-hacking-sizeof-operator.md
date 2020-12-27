## Part 37 – Hacking SizeOf Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumberSize = sizeof(myNumber);

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumberSize &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429032559.jpg"/></div>

Remember that we create a variable __myNumber = 16__ to which we create another variable __myNumberSize__ which holds the value of the size of __myNumber__.&nbsp;We see that when we execute our code it shows 4 therefore we see that the SizeOf operator indicates an integer is 4 bytes wide.

Let’s review last week’s code as we start with debugging and breaking on main.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429072643.jpg"/></div>

Let’s break on __main+20__ as we can see the value of __4__ being moved into __r3__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429109049.jpg"/></div>

Let’s examine what is going on at __main+16__ as we can see that we are storing into the value of __$r11-8__ that which exists in __r3__ which in our case is __16__.&nbsp;This makes sense as when we examine our original code the value of __myNumber__ was in fact __16__.&nbsp;We can see this here when we examine the value inside __$r11-8__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429200465.jpg"/></div>

As we can see above the value inside __$r11-12__ is__ 4__ as that represents the value that __SizeOf__ is returning as the integer __16 __is in fact 4 bytes wide.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429249458.jpg"/></div>

Finally when we continue execution we in fact see the value __4__ echoed to the terminal.

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429287002.jpg"/></div>

We run and break on __main+28__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429310244.jpg"/></div>

We see the value in __r3__ is __4__ which is expected.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429336631.jpg"/></div>

We break on __main+36__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429367083.jpg"/></div>

We see the value in __r1__ is __4__ which should make logical sense as the value was stored from __r3__ into __r11-12__ and then back to __r1__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429391206.jpg"/></div>

Let’s hack the value in __r1__!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429414806.jpg"/></div>

Success!&nbsp;We have hacked the machine!

Next week we will dive into the Pre-Increment Operator.