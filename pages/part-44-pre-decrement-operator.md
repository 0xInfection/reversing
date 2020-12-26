# Part 44 – Pre-Decrement Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's take a look at our pre-decrement operator example. The pre-decrement operator decrements a given value before the action gets assigned.

Let's examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = --myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQETIq-NCg8NXw/article-inline_image-shrink_1000_1488/0/1529666614196?e=1614211200&amp;v=beta&amp;t=Dkimz2B50UjF7KAufF_0jtR-Luh9gV1TM95fqNQQQZg"/></div>

As we compile and run we see 15 echoed out to the terminal.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG3Dreh2ykF4g/article-inline_image-shrink_1000_1488/0/1529666685691?e=1614211200&amp;v=beta&amp;t=jjT-cdObaIBS0UJ3Y8Wtq3GeLXYAnvSv7QDUkVzISD0"/></div>

The value of __myNumber __was __16 __and when it is assigned with the pre-decrement operator we see that the new value is __15__ as it is assigned into __myNewNumber__.

Next week we will dive into the Debuggin Pre-Decrement Operator.