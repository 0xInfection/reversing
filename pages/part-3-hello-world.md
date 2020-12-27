## Part 3 - "Hello World"

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to start at the beginning and take a very simple C++ program that does nothing more than use the stream insertion operator to send a string literal to the stdout and then use the end line manipulator to flush the output buffer.

Let's start by creating a file 0x01\_asm64\_helloworld.cpp and type the following into it.

<pre spellcheck="false">#include &lt;iostream&gt;

int main()
{
&nbsp; &nbsp; std::cout &lt;&lt; "Hello World!" &lt;&lt; std::endl;
&nbsp; &nbsp; return 0;
}
</pre>

Let's compile and link.

<pre spellcheck="false">g++ -o 0x01_asm64_helloworld 0x01_asm64_helloworld.cpp
</pre>

Let's run.

<pre spellcheck="false">./0x01_asm64_helloworld
</pre>

We see the simple result.

<pre spellcheck="false">Hello World!
</pre>

These lessons are deliberately intended to be SHORT an SIMPLE. I know a number of you are more advanced however I really want to make this course as beginner friendly as possible.

In our next lesson we will debug this very simple binary using our dev build of Radare2.