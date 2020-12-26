<h1>Part 29 – Float Variables</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>The next stage in our journey is that of Floating-Point variables. </p><p>A floating-point variable is different from an integer as it has a fractional value attached to which we designate with a period.</p><p>Let’s examine our code.</p><pre spellcheck="false">#include &lt;iostream&gt;

 

float main(void) {

            int myNumber = 1337.1;

 

            std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

 

            return 0;

}
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQFUrIpYaQmEtw/article-inline_image-shrink_1000_1488/0/1520592872663?e=1614211200&amp;v=beta&amp;t=E50SPLEYjPMv8QgqKMnF2Fo6VXtmokHZvjejA5_U6aE"/></div><p>To compile this we simply type:</p><p>g++ example6.cpp -o example6</p><p>./example6</p><p>SUCCESS! We see 1337.1 printed to the standard output or terminal!</p><p>Let’s break it down:</p><p>We assign the floating-point variable<strong> </strong>directly into the variable <strong>myNumber </strong>and then print it out to the terminal with the c++ <strong>cout</strong> function.</p><p>Thus far we have a good understanding of the ARM registers however next week we will introduce the registers within the math co-processor that work with floating-point variables. The registers you have worked with up to now only store whole numbers or integers and at the Assembly level, any fractional value must be manipulated through the math co-processor registers.</p><p>Next week we will dive into Debugging Float Variables.</p>