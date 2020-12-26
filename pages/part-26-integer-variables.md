# Part 26 – Integer Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The next stage in our journey is that of Integer variables.&nbsp;

A 32-bit register can store 2^32 different values. The range of integer values that can be stored in 32 bits depends on the integer representation used. With the two most common representations, the range is 0 through 4,294,967,295 (2^32 − 1) for representation as an (unsigned) binary number, and −2,147,483,648 (−2^31) through 2,147,483,647 (2^31 − 1) for representation as two's complement.

Keep in mind with 32-bit memory addresses you can directly access a maximum of 4 GB of byte-addressable memory.

Let’s examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 777;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFFzKE2-NeJbw/article-inline_image-shrink_1000_1488/0/1520215369999?e=1614211200&amp;v=beta&amp;t=tcd0zfGK3F2vSd51-VRdfAowyhHj5wXJaxr7zh1tD0A"/></div>

To compile this we simply type:

g++ example5.cpp -o example5

./example5

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFyKh1MJYpK9A/article-inline_image-shrink_1000_1488/0/1520195285687?e=1614211200&amp;v=beta&amp;t=6ZztORjcanzS5t2iEaY0ME83-6C6OK94tOAFd8QHHNc"/></div>

SUCCESS!&nbsp;We see __777__ printed to the standard output or terminal!

Let’s break it down:

We assign the integer __777 __directly into the variable __myNumber __and then print it out to the terminal with the c++ __cout__ function.

Next week we will dive into Debugging Integer Variables.