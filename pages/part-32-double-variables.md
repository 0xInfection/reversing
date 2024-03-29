## Part 32 – Double Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The next stage in our journey is that of double-precision floating-point variables.&nbsp;

A double-precision floating-point variable is different from a floating-point variable as it is 64-bits wide and 15-17 significant digits of precision.

Let’s examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; double myNumber = 1337.77;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1522403579256.jpg"/></div>

To compile this we simply type:

g++ example7.cpp -o example7

./example7

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1522403604790.jpg"/></div>

SUCCESS!&nbsp;We see 1337.77 printed to the standard output or terminal!

Let’s break it down:

We assign the floating-point variable__ __directly into the variable __myNumber __and then print it out to the terminal with the c++ __cout__ function.

Next week we will dive into Debugging Double Variables.