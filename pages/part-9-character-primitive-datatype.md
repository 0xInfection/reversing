## Part 9 - Character Primitive Datatype

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to talk about the first of the C++ primitive. The _char_ dataype is used to store a single character and must be surrounded by single quotes.

Let's look at our basic example.

<pre spellcheck="false">#include &lt;iostream&gt;

int main()
{
    char my_char = 'c';

    std::cout &lt;&lt; my_char &lt;&lt; std::endl;

    return 0;
}
</pre>

Extremely simple. We are simply creating a char variable called _my\_char _and assigning it the character _c_.

We then print it to stdout and nothing more.

Let's compile and link.

<pre spellcheck="false">g++ -o 0x03_asm64_char_primitive_datatype 0x03_asm64_char_primitive_datatype.cpp
</pre>

Let's run.

<pre spellcheck="false">./0x03_asm64_char_primitive_datatype
</pre>

Very simply we see the following.

<pre spellcheck="false">c
</pre>

It successfully echoed c to the terminal stdout. Very simple. 

Next week we will debug this very simple example.

  