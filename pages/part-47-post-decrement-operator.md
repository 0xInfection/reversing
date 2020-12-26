# Part 47 – Post-Decrement Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = myNumber--;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

We see our very simple C++ code above to which we are doing nothing more than assigning a number into a variable to which we init another int variable and assign the original variable to which it is post-decremented. We then output each value to the terminal.

Let's debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQEYId8W-vF-fQ/article-inline_image-shrink_1000_1488/0/1532085310684?e=1614211200&amp;v=beta&amp;t=jmklFnNu31_R_KOjsRY6UBKv6BdlvY6hQRvOY9mWEEI"/></div>

It is clear that the value for the post-decrement operator gets loaded into __r1__ at __main+68 __so let's break at __main+72__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQFevnl8ABB7zw/article-inline_image-shrink_1000_1488/0/1532085326445?e=1614211200&amp;v=beta&amp;t=owEilGhGFI6Fj5OtWO0S6GNHaJ3_O2QOb_4MonVntHU"/></div>

We can clearly see that __r1 __does in fact hold the value of __15__ to which was decremented from our original value.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQH4rl574XICeQ/article-inline_image-shrink_1000_1488/0/1532085443370?e=1614211200&amp;v=beta&amp;t=V9oIz7Tmi89hFMRqSn412_pM-YZwsczv-7G8iGfQY_A"/></div>

Next week we will dive into Hacking Post-Decrement Operator.