# Part 14 - Hello World

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we begin our journey into the world of C++ and gaining a better understanding of how C++ interacts with our ARM processor.

The prior lessons in this series focus on the basics of the ARM processor and touch upon its architecture and how everything ultimately translates down to Assembly Language and then ultimately opcodes into machine language.

We start with our first program in C++ which is our “Hello World” program.&nbsp;Let’s dive in and break each line down step-by-step and see how this language works.&nbsp;We will call this __example1.cpp__ and save it to our device.

<pre spellcheck="false">#include &lt;iostream&gt;
&nbsp;
int main(void) {
    std::cout &lt;&lt; “Hello World” std::endl;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;return 0;
}
</pre>

<div class="slate-resizable-image-embed"><img src="/imgs/1520191083072.jpg"/></div>

To compile this we simply type:

<pre spellcheck="false">g++ example1.cpp -o example1
</pre>

We simply then type:

<pre spellcheck="false">./example1
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-left"><img src="/imgs/1520237920732.jpg"/></div>

  

SUCCESS!&nbsp;We see “Hello World” printed to the standard output or terminal!

Lets break it down line by line:

__\#include &lt;iostream&gt; __is referred to as a preprocessor statement.&nbsp;These preprocessor statements happen just before the compilation of the rest of the code.&nbsp;The \#include keyword will find a file called __iostream__ and take all of the contents of that file and paste it into the existing code we just created.&nbsp;These files are also called header files.&nbsp;

We call __iostream__ because we need a declaration for a function called __cout__ and __endl__.&nbsp;The __cout__ function allows us to print text to the standard output or terminal and the __endl__ function creates a new line after the text has been displayed.

The main section which is of type integer is the entry point into the main application or binary.&nbsp;You will notice a __void__ inside the __()__ which indicates that it does not have any parameters which will be passed into the function.

The __std __indicates a namespace which is quite simply a mechanism to organize code into logical groups in order to prevent name collisions when you are dealing with multiple libraries.

You will see many examples where they declare a using namespace std; however I will NEVER utilize this approach as it can cause naming collisions in more complex applications.

The __&lt;&lt;__ operator is referred to as an overloaded operator.&nbsp;They are essentially a function very similar to __printf__ in the C language.&nbsp;We are simply moving the __“Hello World” __string into the __cout__ function through the use of the __&lt;&lt;__ overloaded operator.&nbsp;We then push the __endl__ which creates a new line to the console.

The final line is the return 0.&nbsp;Since our main function is of type int, we have to return something.&nbsp;In C++ 11 there is no need for this in the main function however is required for every other function.&nbsp;I will stick to tradition and simply include it.

The next stage is that we compile the file.&nbsp;The first thing that occurs is the entire contents of the iostream header goes into the source file as we discussed.&nbsp;The compile process is where the C++ code gets translated into machine code.&nbsp;The next stage of compilation occurs when the rest of the lines of our existing code are parsed through.&nbsp;Essentially we have all of the contents of iostream into a new file and then all of the contents of our existing file added to a single file.

Compiling takes our text file the cpp file and converts it into an intermediate format called an obj file.&nbsp;An abstract syntax tree is created which is a conversion of constant data, variables and instructions.

Once the tree is created the code is generated.&nbsp;This means we now have machine code that our ARM CPU will execute.&nbsp;Every cpp file (translation units) which will have its own respective obj file associated with it.&nbsp;

Linking takes our obj files, our compiled files, in addition to the C++ Standard Library and finds where each symbol and function is and link them all together into one executable.&nbsp;&nbsp;&nbsp;

The concepts above may appear a bit confusing if you are new to programming however as you code and compile and later debug and hack in Assembly Language it will all become very clear and you will learn to master the processor.

Next week we will dive into Debugging Hello World.