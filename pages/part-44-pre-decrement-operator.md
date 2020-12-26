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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/768150832.jpg"/></div>

As we compile and run we see 15 echoed out to the terminal.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1034526941.jpg"/></div>

The value of __myNumber __was __16 __and when it is assigned with the pre-decrement operator we see that the new value is __15__ as it is assigned into __myNewNumber__.

Next week we will dive into the Debuggin Pre-Decrement Operator.