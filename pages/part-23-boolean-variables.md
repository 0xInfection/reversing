<h1>Part 23 – Boolean Variables</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>The next stage in our journey is that of Boolean variables. The name goes back to the great George Boole to which all modern computer science has derived. </p><p>At the lowest level a value is either 0 or 1, false or true, + &lt; 5 volts or +5 volts, etc.</p><p>Let’s examine our code.</p><pre spellcheck="false">#include &lt;iostream&gt;

 

int main(void) {

            bool isHacked = false;

 

            std::cout &lt;&lt; isHacked &lt;&lt; std::endl;

 

            return 0;

}
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFdIMgcYlHsxQ/article-inline_image-shrink_1000_1488/0/1520192758105?e=1614211200&amp;v=beta&amp;t=Cw-cpnI_gSKwLaA95D2XTtJrEYf9CZIdqpPJ6qF5c-g"/></div><p>To compile this we simply type:</p><pre spellcheck="false">g++ example4.cpp -o example4

./example4
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHKj1-JGT0Ctw/article-inline_image-shrink_1000_1488/0/1520196655358?e=1614211200&amp;v=beta&amp;t=7Cyap7-vGZe6WZFHJ8AXdNMG7e6k1EbWpzEYlKIWKHw"/></div><p>SUCCESS! We see <strong>0</strong> printed to the standard output or terminal!</p><p>Let’s break it down:</p><p>We create a boolean variable called <strong>isHacked </strong>to which we assign a value of <strong>false</strong> or <strong>0</strong>. When we run the binary we clearly see the value <strong>0</strong> that successfully was echoed to the standard output.</p><p>Next week we will dive into Debugging Boolean Variables.</p>