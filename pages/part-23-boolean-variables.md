# Part 23 – Boolean Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The next stage in our journey is that of Boolean variables.&nbsp;The name goes back to the great George Boole to which all modern computer science has derived.&nbsp;

At the lowest level a value is either 0 or 1, false or true, + &lt; 5 volts or +5 volts, etc.

Let’s examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bool isHacked = false;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; isHacked &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/337235772.jpg"/></div>

To compile this we simply type:

<pre spellcheck="false">g++ example4.cpp -o example4

./example4
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/49260221.jpg"/></div>

SUCCESS!&nbsp;We see __0__ printed to the standard output or terminal!

Let’s break it down:

We create a boolean variable called __isHacked __to which we assign a value of __false__ or __0__.&nbsp;When we run the binary we clearly see the value __0__ that successfully was echoed to the standard output.

Next week we will dive into Debugging Boolean Variables.