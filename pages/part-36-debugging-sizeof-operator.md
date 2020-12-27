## Part 36 – Debugging SizeOf Operator

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524823603695.jpg"/></div>

Remember that we create a variable __myNumber = 16__ to which we create another variable __myNumberSize__ which holds the value of the size of __myNumber__.&nbsp;We see that when we execute our code it shows 4 therefore we see that the SizeOf operator indicates an integer is 4 bytes wide.

Let’s debug and break on main.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524823663114.jpg"/></div>

Let’s break on __main+20__ as we can see the value of __4__ being moved into __r3__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524823735285.jpg"/></div>

Let’s examine what is going on at __main+16__ as we can see that we are storing into the value of __$r11-8__ that which exists in __r3__ which in our case is __16__.&nbsp;This makes sense as when we examine our original code the value of __myNumber__ was in fact __16__.&nbsp;We can see this here when we examine the value inside __$r11-8__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524823766343.jpg"/></div>

As we can see above the value inside __$r11-12__ is__ 4__ as that represents the value that __SizeOf__ is returning as the integer __16 __is in fact 4 bytes wide.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524823791885.jpg"/></div>

Finally when we continue execution we in fact see the value __4__ echoed to the terminal.

Next week we will dive into Hacking SizeOf Operator.