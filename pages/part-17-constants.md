## Part 17 - Constants

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

So far we have created, debugged and hacked a simple string echo to the standard terminal.&nbsp;We will expand upon that example by adding a constant.

A constant in C++ is a value that will not change throughout program execution (unless hacked).&nbsp;It is used such that you have a declaration early in the code so that if your future program architecture ever changes you can redefine the constant in one place rather than having to update code all through your code base.

It is standard practice to code our constants in all CAPS so that when we see it referenced somewhere in the code we know that value is a constant.

We start with our second program in C++ which is our “Constant” program.&nbsp;Let’s dive in and break each line down step-by-step and see how this language works.&nbsp;We will call this __example2.cpp__ and save it to our device.

<pre spellcheck="false">#include &lt;iostream&gt;
&nbsp;
int main(void) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cons tint YEAR = 2017;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; YEAR &lt;&lt; std::endl;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149852856.jpg"/></div>

To compile this we simply type:

<pre spellcheck="false">g++ example2.cpp -o example2
</pre>

We simply then type:

<pre spellcheck="false">./example2
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148263310.jpg"/></div>

SUCCESS!&nbsp;We see “__2017__” printed to the standard output or terminal!

Let’s break it down:

We utilize the __const __keyword to indicate a constant to which we assign it the integer value of 2017.

We then utilize the __cout __function to print it to the standard output or terminal and add a new line with the __endl__ function.

That’s it!&nbsp;Very simple.

Next week we will dive into Debugging Constants.