## Part 12 - Boolean Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to talk about the C++ _boolean_ datatype that stores either a _0_ or _1_ to represent _0_ for _false _and _1_ for anything _true_.

This kind of flag is used extensively in programming in general and we will look at another very basic program to understand its simple usage.

<pre spellcheck="false">#include &lt;iostream&gt;
	
	int main()
	{
	    bool my_bool = true;

	    std::cout &lt;&lt; my_bool &lt;&lt; std::endl;

	    return 0;
	}
</pre>

We see that we are creating a _bool_ and assigning it a _true _value or _1 _value and printing it.

Let's compile and link.

<pre spellcheck="false">g++ -o 0x04_asm64_boolean_primitive_datatype 0x04_asm64_boolean_primitive_datatype.cpp
</pre>

Let's run.

<pre spellcheck="false">./0x04_asm64_boolean_primitive_datatype
</pre>

We simply see the following.

<pre spellcheck="false">1
</pre>

It successfully echoed _1_ to the terminal stdout. Very simple.

Next week we will debug this very simple example.