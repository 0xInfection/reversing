# Part 42 – Debugging Post-Increment Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

We create a variable __myNumber = 16__ to which we create another variable __myNewNumber__ which post-increments the value of __myNumber__.&nbsp;We see that when we execute our code it shows __16__ as the value of __myNewNumber__ and __17__ as the value of __myNumber__ as __myNewNumber__ does not get incremented as only __myNumber__ get incremented as it is a post operator.

When we post-increment the value of the variable is incremented after assigning it to another variable.&nbsp;For example __myNumber__ is __16__ so it gets incremented after being assigned to __myNewNumber__ so therefore we get __17__.

Let's debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFmaWzQRvrFTw/article-inline_image-shrink_1000_1488/0/1528458112325?e=1614211200&amp;v=beta&amp;t=r2hxg9B8WWQKywdrzvuZpmJuNpf6KnnK5WKq8NsRiQ0"/></div>

Let's break on __\*main+28 __and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH3l-5lgllJ0g/article-inline_image-shrink_1000_1488/0/1528458131421?e=1614211200&amp;v=beta&amp;t=ZZMsTq9vtKenyWmtO1dUA0Z4wzYeKGz3vJTs_iSOGYw"/></div>

As we can see the value in __r3 __is 16 and the value in __r2 __is 17. We can see that as they are loaded from memory into the registers in __\*main+12__ directly by the __mov__ instruction and __\*main+24__ we add 1 into __r3__ and then put that value into __r2__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHn2yUOd579ug/article-inline_image-shrink_1000_1488/0/1528458142344?e=1614211200&amp;v=beta&amp;t=bHS8Hh0Jv2MwokxhtSabc4AzoSi2rvxwejJxKmox6TQ"/></div>

As we continue we can see the __cout __c++ function called which echos out the values to the terminal (standard output) as expected.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQESA6aDc_cw5w/article-inline_image-shrink_1000_1488/0/1528458154804?e=1614211200&amp;v=beta&amp;t=T7apGoUur4voWNz_WCJMDled6BZ7BLdzb_jfY6Fi244"/></div>

Next week we will dive into Hacking Post-Increment Operator.