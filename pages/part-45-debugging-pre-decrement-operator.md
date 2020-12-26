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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQFxNuZ90pIzIg/article-inline_image-shrink_1000_1488/0/1530270075261?e=1614211200&amp;v=beta&amp;t=QadDqJLhS4VRDb-k1HsVwGO-AMHgFBtuhqwzJqUkqxk"/></div>

Let's break.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQE71Ogx2J3drQ/article-inline_image-shrink_1000_1488/0/1530270088297?e=1614211200&amp;v=beta&amp;t=rkTmb-gh02ahmb2p-5KDqez8aq5eeAo9SOOTCP8Bqxk"/></div>

As we can see __r3 __holds 15. Keep in mind hacking this value may not be the final place it may be stored. Remember this for next week and re-examine the debug code above to see if you can figure it out.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQEE6qagW6MkAQ/article-inline_image-shrink_1000_1488/0/1530270183626?e=1614211200&amp;v=beta&amp;t=xHmRPxDWY5sNCoBLPS3YOtHDieqaCADgkfjZcclHZrQ"/></div>

As we can see __r1__ holds 15 as well. Keep in mind the above statement.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQHwmVqJHsycYw/article-inline_image-shrink_1000_1488/0/1530270209438?e=1614211200&amp;v=beta&amp;t=Yq-FsGfw_tFBl8Cb1jpv1nQo6hxgXnbX7arXkKJqxLs"/></div>

As we continue we see our __cout __function echoing 15 for both areas as expected.

Next week we will dive into the Hacking Pre-Decrement Operator.