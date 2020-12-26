<h1>Part 5 - Hacking "Hello World"</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking_c-_arm64</p><p>Today we are going to look at a basic I/O C++ program that has some minimal validation.</p><p>Before I get into the brief lecture as I try to keep these short, I wanted to explain why I am not using the textbook straight <em>cin</em> examples that you see across the globe.</p><p>The <em>cin</em>, standard input stream, which takes input from the keyboard is referred to as our stdin.</p><p>What <em>cin</em> does is use whitespace, tab and newline as a terminator to the input stream. For example if you input <em>'abc'</em> and hit a tab or put a whitespace or newline by hitting return the data to the right of it will be ignored.</p><p>The problem is if you read from <em>cin</em> again it will pick up the remaining data in the stream if you do not flush the input buffer.</p><p>If you had for example:</p><pre spellcheck="false">std::cin &gt;&gt; val1;
std::cin &gt;&gt; val2;
</pre><p>If the user enters <em>1</em> and then leaves a space and then <em>2</em> and presses enter, you have no issue. <em>1</em> will be assigned into <em>val1</em> and <em>2</em> will be assigned to <em>val2</em> as they are chained.</p><p>The problem is what if you enter <em>'Hey Jude'</em> instead of an integer? What happens is it tries to read an integer and it goes into a failed state and from that point everything else it is extracting is unreliable.</p><p>I did not mean to be long winded but I really wanted to emphasize why you would NEVER use <em>cin</em> by itself and I mean NEVER!</p><p>Let's take a look at our basic i/o program that we will debug in the next lesson with a very basic C++ program that validates input.</p><pre spellcheck="false">#include &lt;iostream&gt;
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
</pre><p>We start by importing <em>iostream</em>, <em>sstream</em> and <em>string</em>. So far nothing tricky.</p><p>We then prompt the user to enter their age. We then create a string object called <em>line</em> and take advantage of C++ <em>getline()</em> which is a standard C++ library function that is used to read a string or a line from an input stream properly.</p><p>We then take advantage of the <em>stringstream</em> as it associates a string object with a stream allowing you to read from the string as if it were a stream like we would do with raw <em>cin</em>. In this simple example we create an <em>is</em> object which is short for input stringstream and connect it with our <em>line</em> object.</p><p>Then before we echo data to stdout we do a little validation. We first check to see if <em>age</em> is the type it was defined as which is an <em>int</em> OR is there a white space in the stream after a given integer OR is age greater than <em>100</em> or less than <em>0</em>. Very simply it provides a response if the input does not meet this criteria.</p><p>Finally if all is well it echoes out a simple <em>cout</em>.</p><p>Let's compile and link.</p><pre spellcheck="false">g++ -o 0x02_asm64_basicio 0x02_asm64_basicio.cpp
</pre><p>Let's run.</p><pre spellcheck="false">./0x02_asm64_basicio
</pre><p>Depending on what you enter it will validate as appropriate as described above. PLEASE try this example and manipulate the source to get a full understanding of what is going on here.</p><p>In our next lesson we will debug this very simple binary using our dev build of Radare2.</p>