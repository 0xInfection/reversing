## Part 29 – Float Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The next stage in our journey is that of Floating-Point variables.&nbsp;

A floating-point variable is different from an integer as it has a fractional value attached to which we designate with a period.

Let’s examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

float main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 1337.1;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520592872663.jpg"/></div>

To compile this we simply type:

g++ example6.cpp -o example6

./example6

SUCCESS!&nbsp;We see 1337.1 printed to the standard output or terminal!

Let’s break it down:

We assign the floating-point variable__ __directly into the variable __myNumber __and then print it out to the terminal with the c++ __cout__ function.

Thus far we have a good understanding of the ARM registers however next week we will introduce the registers within the math co-processor that work with floating-point variables.&nbsp;The registers you have worked with up to now only store whole numbers or integers and at the Assembly level, any fractional value must be manipulated through the math co-processor registers.

Next week we will dive into Debugging Float Variables.