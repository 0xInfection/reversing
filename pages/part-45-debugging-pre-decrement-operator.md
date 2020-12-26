# Part 45 – Debugging Pre-Decrement Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = --myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

We remember when we compile we get 15.

Let's debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/756947067.jpg"/></div>

Let's break.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/154002148.jpg"/></div>

As we can see __r3 __holds 15. Keep in mind hacking this value may not be the final place it may be stored. Remember this for next week and re-examine the debug code above to see if you can figure it out.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1036215822.jpg"/></div>

As we can see __r1__ holds 15 as well. Keep in mind the above statement.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/735633383.jpg"/></div>

As we continue we see our __cout __function echoing 15 for both areas as expected.

Next week we will dive into the Hacking Pre-Decrement Operator.