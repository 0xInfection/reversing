<h1>Part 48 – Debugging Post-Decrement Operator</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>Let's once again review our code.</p><pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
    int myNumber = 16;
    int myNewNumber = myNumber--;

    std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

    return 0;
}
</pre><p>Let's review last week's debug.</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFp2Mxp62mXrQ/article-inline_image-shrink_1000_1488/0/1532690049930?e=1614211200&amp;v=beta&amp;t=3xBB4cevl7ZNN7dTopkNoNkkSog6H2HJ2hMfeOGmvqk"/></div><p>As we can see here the value in <strong>r1</strong> at <strong>main+68</strong> is <strong>15</strong>. Let's hack!</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGC6C5RsOJnLA/article-inline_image-shrink_1000_1488/0/1532690140517?e=1614211200&amp;v=beta&amp;t=VDasHoj8d-Rx6AND9IPFmspdHejexLq5nRMWE3RSe-w"/></div><p>Once again we have manipulated and changed program execution to our own bidding. With each of these bite-size lessons you continue to get a better grasp on the processor and how it interfaces with the binary.</p><p>I hope this series gives you a solid framework for understanding the ARM processor. This concludes the series. Thank you all for coming along on the journey!</p>