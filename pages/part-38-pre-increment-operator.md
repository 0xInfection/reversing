<h1>Part 38 – Pre-Increment Operator</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>The next stage in our journey is that of the pre-increment operator. </p><p>Let’s examine our code.</p><pre spellcheck="false">#include &lt;iostream&gt;

 

int main(void) {

            int myNumber = 16;

            int myNewNumber = ++myNumber;

 

            std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

 

            return 0;

}
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFl1kw-26V6pg/article-inline_image-shrink_1000_1488/0/1526036616866?e=1614211200&amp;v=beta&amp;t=G-kQS1i6E1fNS_tOfvkLzQ_LmoInMxvdKVb63si3Vaw"/></div><p>To compile this we simply type:</p><p>g++ example9.cpp -o example9</p><p>./example9</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE0hxqk9fJLyQ/article-inline_image-shrink_1000_1488/0/1526036640627?e=1614211200&amp;v=beta&amp;t=AOYJO94qJf8w-o9-ey2lS2OB5A4kboFsPTmz4YfzR4o"/></div><p>We see 17 printed to the screen.</p><p>Let’s break it down:</p><p>We create a variable <strong>myNumber = 16</strong> to which we create another variable <strong>myNewNumber</strong> which pre-increments the value of <strong>myNumber</strong>. We see that when we execute our code it shows 17.</p><p>When we pre-increment the value of the variable is incremented before assigning it to another variable. For example <strong>myNumber</strong> is <strong>16</strong> so it gets incremented before being assigned to <strong>myNewNumber</strong> so therefore we get <strong>17</strong>.</p><p>Next week we will dive into Debugging Pre-Increment Operator.</p>