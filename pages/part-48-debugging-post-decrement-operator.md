# Part 48 – Debugging Post-Decrement Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's once again review our code.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = myNumber--;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Let's review last week's debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFp2Mxp62mXrQ/article-inline_image-shrink_1000_1488/0/1532690049930?e=1614211200&amp;v=beta&amp;t=3xBB4cevl7ZNN7dTopkNoNkkSog6H2HJ2hMfeOGmvqk"/></div>

As we can see here the value in __r1__ at __main+68__ is __15__. Let's hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGC6C5RsOJnLA/article-inline_image-shrink_1000_1488/0/1532690140517?e=1614211200&amp;v=beta&amp;t=VDasHoj8d-Rx6AND9IPFmspdHejexLq5nRMWE3RSe-w"/></div>

Once again we have manipulated and changed program execution to our own bidding. With each of these bite-size lessons you continue to get a better grasp on the processor and how it interfaces with the binary.

I hope this series gives you a solid framework for understanding the ARM processor. This concludes the series. Thank you all for coming along on the journey!