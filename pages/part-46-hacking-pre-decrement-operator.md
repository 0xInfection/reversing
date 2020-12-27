## Part 46 – Hacking Pre-Decrement Operator

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875391750.jpg"/></div>

Let's break.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875474311.jpg"/></div>

Let's review what is inside __r3 __and hack it.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875492398.jpg"/></div>

Now as we continue we see it did not successfully hack why is that?

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875528881.jpg"/></div>

We re-run the binary and break and see the value here at __r1 __hold __15__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875553276.jpg"/></div>

When we continue we see 15 which we don't want.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875636786.jpg"/></div>

Now we break again and print the value.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875661356.jpg"/></div>

This time we set __r1__ and we can see we have successfully hacked!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875673374.jpg"/></div>

This is your first experience with really breaking down the registers and seeing where things are stored and how it can affect outcome. Take time and run this yourself so you really have a firm handle on this.

Next week we will dive into the Post-Decrement Operator.