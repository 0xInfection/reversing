<h1>Part 2 - Development Setup</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking_c-_arm64</p><p>Today we are going to start at the beginning and take a very simple C++ program that does nothing more than use the stream insertion operator to send a string literal to the stdout and then use the end line manipulator to flush the output buffer.</p><p>Let's start by creating a file 0x01_asm64_helloworld.cpp and type the following into it.</p><pre spellcheck="false">#include &lt;iostream&gt;


int main()
{
    std::cout &lt;&lt; "Hello World!" &lt;&lt; std::endl;
    return 0;
}
</pre><p>Let's compile and link.</p><pre spellcheck="false">g++ -o 0x01_asm64_helloworld 0x01_asm64_helloworld.cpp
</pre><p>Let's run.</p><pre spellcheck="false">./0x01_asm64_helloworld
</pre><p>We see the simple result.</p><pre spellcheck="false">Hello World!
</pre><p>These lessons are deliberately intended to be SHORT an SIMPLE. I know a number of you are more advanced however I really want to make this course as beginner friendly as possible.</p><p>In our next lesson we will debug this very simple binary using our dev build of Radare2.</p>