# Part 5 - Hacking "Hello World"

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to look at a basic I/O C++ program that has some minimal validation.

Before I get into the brief lecture as I try to keep these short, I wanted to explain why I am not using the textbook straight _cin_ examples that you see across the globe.

The _cin_, standard input stream, which takes input from the keyboard is referred to as our stdin.

What _cin_ does is use whitespace, tab and newline as a terminator to the input stream. For example if you input _'abc'_ and hit a tab or put a whitespace or newline by hitting return the data to the right of it will be ignored.

The problem is if you read from _cin_ again it will pick up the remaining data in the stream if you do not flush the input buffer.

If you had for example:

<pre spellcheck="false">std::cin &gt;&gt; val1;
std::cin &gt;&gt; val2;
</pre>

If the user enters _1_ and then leaves a space and then _2_ and presses enter, you have no issue. _1_ will be assigned into _val1_ and _2_ will be assigned to _val2_ as they are chained.

The problem is what if you enter _'Hey Jude'_ instead of an integer? What happens is it tries to read an integer and it goes into a failed state and from that point everything else it is extracting is unreliable.

I did not mean to be long winded but I really wanted to emphasize why you would NEVER use _cin_ by itself and I mean NEVER!

Let's take a look at our basic i/o program that we will debug in the next lesson with a very basic C++ program that validates input.

<pre spellcheck="false">#include &lt;iostream&gt;
#include &lt;sstream&gt;
#include &lt;string&gt;

int main()
{
    int age = 0;
    bool valid = false;
    char null = '\0';

    while (!valid)
    {
        std::cout &lt;&lt; "Enter Age: ";

        // Get input as string
        std::string line;
        getline(std::cin, line);

        // Init stringstream
        std::stringstream is(line);

        // Attempt to read a valid age from the stringstream and
        // if a number can't be read, or there is more than white
        // space in the string after the number, then fail the read
        // and get another string from the user and make sure the 
        // dude is at least a year old and less than or equal to
        // 100 years old
        if (!(is &gt;&gt; age) || (is &gt;&gt; std::ws &amp;&amp; is.get(null)) || age &gt;= 100 || age &lt;= 0)
            std::cout &lt;&lt; "Dude be real!" &lt;&lt; std::endl;
        else
            valid = true ;
    }

    std::cout &lt;&lt; "Your are " &lt;&lt; age &lt;&lt; " years old, seems legit!" &lt;&lt; std::endl;

    return 0;
}
</pre>

We start by importing _iostream_, _sstream_ and _string_. So far nothing tricky.

We then prompt the user to enter their age. We then create a string object called _line_ and take advantage of C++ _getline()_ which is a standard C++ library function that is used to read a string or a line from an input stream properly.

We then take advantage of the _stringstream_ as it associates a string object with a stream allowing you to read from the string as if it were a stream like we would do with raw _cin_. In this simple example we create an _is_ object which is short for input stringstream and connect it with our _line_ object.

Then before we echo data to stdout we do a little validation. We first check to see if _age_ is the type it was defined as which is an _int_ OR is there a white space in the stream after a given integer OR is age greater than _100_ or less than _0_. Very simply it provides a response if the input does not meet this criteria.

Finally if all is well it echoes out a simple _cout_.

Let's compile and link.

<pre spellcheck="false">g++ -o 0x02_asm64_basicio 0x02_asm64_basicio.cpp
</pre>

Let's run.

<pre spellcheck="false">./0x02_asm64_basicio
</pre>

Depending on what you enter it will validate as appropriate as described above. PLEASE try this example and manipulate the source to get a full understanding of what is going on here.

In our next lesson we will debug this very simple binary using our dev build of Radare2.