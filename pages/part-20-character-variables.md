# Part 20 – Character Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The next stage in our journey is that of character variables.&nbsp;Unlike the strings we have dealt with thus far, a character only takes up one byte of data.

Keep in mind, when we deal with any character data, we deal with literally two hex digits which are the ASCII code that represents an actual character that we see on our respective terminals.

Remember that each hex digit is 4 bits in length.&nbsp;Therefore two hex digits are 8 bits in length or a byte long.&nbsp;

To recap, each character translates down to an ASCII code in hex which the processor understands.&nbsp;The value of __n__ is __0x6e__ hex or __110__ decimal.&nbsp;You can review any ASCII table to see where we derived this value.&nbsp;This will come in handy in the next lesson.

We start with our third program in C++ which is our “Character Variable” program.&nbsp;Let’s dive in and break each line down step-by-step and see how this language works.&nbsp;We will call this example3.cpp and save it to our device.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; char yes_no = ‘n’;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; yes_no &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520190636660.jpg"/></div>

To compile this we simply type:

g++ example3.cpp -o example3

We simply then type:

./example3

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520211586776.jpg"/></div>

SUCCESS!&nbsp;We see “__n__” printed to the standard output or terminal!

Let’s break it down:

We utilize the __char __keyword to indicate a character variable to which we assign it the value of __n__.

We then utilize the __cout __function to print it to the standard output or terminal and add a new line with the __endl__ function.

That’s it!&nbsp;Very simple.

Next week we will dive into Debugging Character Variables.