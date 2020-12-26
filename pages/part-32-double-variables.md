<h1>Part 32 – Double Variables</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>The next stage in our journey is that of double-precision floating-point variables. </p><p>A double-precision floating-point variable is different from a floating-point variable as it is 64-bits wide and 15-17 significant digits of precision.</p><p>Let’s examine our code.</p><pre spellcheck="false">#include &lt;iostream&gt;

 

int main(void) {

            double myNumber = 1337.77;

 

            std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

 

            return 0;

}
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFKHNGJcnqsQQ/article-inline_image-shrink_1000_1488/0/1522403579256?e=1614211200&amp;v=beta&amp;t=AW9v9itxF-gMk0LBEpdgkBzB5QoQ_JmajBIl1tE-gGE"/></div><p>To compile this we simply type:</p><p>g++ example7.cpp -o example7</p><p>./example7</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGBnyYx8huVDw/article-inline_image-shrink_1000_1488/0/1522403604790?e=1614211200&amp;v=beta&amp;t=dylo5aOmpzs2p2yUkRRL8u4G07SlIJBi5056a7P7XBs"/></div><p>SUCCESS! We see 1337.77 printed to the standard output or terminal!</p><p>Let’s break it down:</p><p>We assign the floating-point variable<strong> </strong>directly into the variable <strong>myNumber </strong>and then print it out to the terminal with the c++ <strong>cout</strong> function.</p><p>Next week we will dive into Debugging Double Variables.</p>