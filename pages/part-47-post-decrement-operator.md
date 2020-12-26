<h1>Part 47 – Post-Decrement Operator</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>Let's re-examine our code.</p><pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
    int myNumber = 16;
    int myNewNumber = myNumber--;

    std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

    return 0;
}
</pre><p>We see our very simple C++ code above to which we are doing nothing more than assigning a number into a variable to which we init another int variable and assign the original variable to which it is post-decremented. We then output each value to the terminal.</p><p>Let's debug.</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQEYId8W-vF-fQ/article-inline_image-shrink_1000_1488/0/1532085310684?e=1614211200&amp;v=beta&amp;t=jmklFnNu31_R_KOjsRY6UBKv6BdlvY6hQRvOY9mWEEI"/></div><p>It is clear that the value for the post-decrement operator gets loaded into <strong>r1</strong> at <strong>main+68 </strong>so let's break at <strong>main+72</strong>.</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQFevnl8ABB7zw/article-inline_image-shrink_1000_1488/0/1532085326445?e=1614211200&amp;v=beta&amp;t=owEilGhGFI6Fj5OtWO0S6GNHaJ3_O2QOb_4MonVntHU"/></div><p>We can clearly see that <strong>r1 </strong>does in fact hold the value of <strong>15</strong> to which was decremented from our original value.</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQH4rl574XICeQ/article-inline_image-shrink_1000_1488/0/1532085443370?e=1614211200&amp;v=beta&amp;t=V9oIz7Tmi89hFMRqSn412_pM-YZwsczv-7G8iGfQY_A"/></div><p>Next week we will dive into Hacking Post-Decrement Operator.</p>