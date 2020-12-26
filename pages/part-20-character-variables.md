<h1>Part 20 – Character Variables</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>The next stage in our journey is that of character variables. Unlike the strings we have dealt with thus far, a character only takes up one byte of data.</p><p>Keep in mind, when we deal with any character data, we deal with literally two hex digits which are the ASCII code that represents an actual character that we see on our respective terminals.</p><p>Remember that each hex digit is 4 bits in length. Therefore two hex digits are 8 bits in length or a byte long. </p><p>To recap, each character translates down to an ASCII code in hex which the processor understands. The value of <strong>n</strong> is <strong>0x6e</strong> hex or <strong>110</strong> decimal. You can review any ASCII table to see where we derived this value. This will come in handy in the next lesson.</p><p>We start with our third program in C++ which is our “Character Variable” program. Let’s dive in and break each line down step-by-step and see how this language works. We will call this example3.cpp and save it to our device.</p><pre spellcheck="false">#include &lt;iostream&gt;

 

int main(void) {

            char yes_no = ‘n’;

 

            std::cout &lt;&lt; yes_no &lt;&lt; std::endl;

 

            return 0;

}
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE9R8gHDJRDdg/article-inline_image-shrink_1000_1488/0/1520190636660?e=1614211200&amp;v=beta&amp;t=gnFIEDb1DHCjINYriZplt0m2q5jJRB6EWxQx1ubwCFQ"/></div><p>To compile this we simply type:</p><p>g++ example3.cpp -o example3</p><p>We simply then type:</p><p>./example3</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHkPA8-n4l81g/article-inline_image-shrink_1000_1488/0/1520211586776?e=1614211200&amp;v=beta&amp;t=sq5xYie1yPkJq4cdMzUGnPfN4_Lx5I6wmCkyJuaThRI"/></div><p>SUCCESS! We see “<strong>n</strong>” printed to the standard output or terminal!</p><p>Let’s break it down:</p><p>We utilize the <strong>char </strong>keyword to indicate a character variable to which we assign it the value of <strong>n</strong>.</p><p>We then utilize the <strong>cout </strong>function to print it to the standard output or terminal and add a new line with the <strong>endl</strong> function.</p><p>That’s it! Very simple.</p><p>Next week we will dive into Debugging Character Variables.</p>