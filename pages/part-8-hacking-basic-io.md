<h1>Part 8 - Hacking Basic I/O</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking_c-_arm64</p><p>Today we are going to talk about the first of the C++ primitive.  The <em>char</em> dataype is used to store a single character and must be surrounded by single quotes.</p><p>Let's look at our basic example.</p><pre spellcheck="false">#include &lt;iostream&gt;

int main()
{
    char my_char = 'c';


    std::cout &lt;&lt; my_char &lt;&lt; std::endl;

    return 0;
}
</pre><p>Extremely simple.  We are simply creating a char variable called <em>my_char </em>and assigning it the character <em>c</em>.</p><p>We then print it to stdout and nothing more.</p><p>Let's compile and link.</p><pre spellcheck="false">g++ -o 0x03_asm64_char_primitive_datatype 0x03_asm64_char_primitive_datatype.cpp
</pre><p>Let's run.</p><pre spellcheck="false">./0x03_asm64_char_primitive_datatype
</pre><p>Very simply we see the following.</p><pre spellcheck="false">c
</pre><p>It successfully echoed c to the terminal stdout.  Very simple.  </p><p>Next week we will debug this very simple example.</p><p><br/></p>