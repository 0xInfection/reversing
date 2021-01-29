## Part 15 - Float Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to talk about the C++&nbsp;_float_&nbsp;datatype that stores floating point values.

<pre spellcheck="false">#include &lt;iostream&gt;

int main()
{
&nbsp; &nbsp; float my_float = 10.1;

&nbsp; &nbsp; std::cout &lt;&lt; my_float &lt;&lt; std::endl;

&nbsp; &nbsp; return 0;
}
</pre>

Very simply we create a float and assign a simple value to it and print it.

Let's compile and link.

<pre spellcheck="false">g++ -o 0x05_float_primitive_datatype 0x05_float_primitive_datatype.cpp
</pre>

Let's run.

<pre spellcheck="false">./0x05_float_primitive_datatype
</pre>

We simply see the following.

<pre spellcheck="false">10.1
</pre>

It successfully echoed&nbsp;_10.1_&nbsp;to the terminal stdout. Very simple.

Next week we will debug this very simple example.