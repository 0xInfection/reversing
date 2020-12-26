<h1>Part 35 – SizeOf Operator</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>The next stage in our journey is that of the SizeOf operator. </p><p>Let’s examine our code.</p><pre spellcheck="false">#include &lt;iostream&gt;

 

int main(void) {

            int myNumber = 16;

            int myNumberSize = sizeof(myNumber);

 

            std::cout &lt;&lt; myNumberSize &lt;&lt; std::endl;

 

            return 0;

}
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEQQajd0uaKRg/article-inline_image-shrink_1000_1488/0/1524218995477?e=1614211200&amp;v=beta&amp;t=l9lfzFdYyYTuQRY4nU77rmWP86l3yAkKTeLKvhO9n1M"/></div><p>To compile this we simply type:</p><p>g++ example8.cpp -o example8</p><p>./example8</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHNiUqDNuY_9g/article-inline_image-shrink_1000_1488/0/1524219035247?e=1614211200&amp;v=beta&amp;t=iJQkN12Yo1uhU1L7dBM2KgIKNzaRW5d_niNY1No8S2Q"/></div><p>We see 4 printed to the screen.</p><p>Let’s break it down:</p><p>We create a variable <strong>myNumber = 16</strong> to which we create another variable <strong>myNumberSize</strong> which holds the value of the size of <strong>myNumber</strong>. We see that when we execute our code it shows 4 therefore we see that the SizeOf operator indicates an integer is 4 bytes wide.</p><p>Next week we will dive into Debugging SizeOf Operator.</p>