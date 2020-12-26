# Part 41 – Post-Increment Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s dive into our code.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGoB-NC7aSBVQ/article-inline_image-shrink_1000_1488/0/1527849027049?e=1614211200&amp;v=beta&amp;t=VsiIVh9rOhN1AhL7FLuVbe6c68VIX7-ERH6ZWDsgLds"/></div>

To compile this we simply type:

g++ example10.cpp -o example10

./example10

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEhgw3K1hwN_g/article-inline_image-shrink_1000_1488/0/1527849063244?e=1614211200&amp;v=beta&amp;t=yFK3wXgvyF2set8O6gUIbIiWRdsMyRn12WtxQGXVd90"/></div>

We see 16 and 17 printed to the screen.

Let’s break it down:

We create a variable __myNumber = 16__ to which we create another variable __myNewNumber__ which post-increments the value of __myNumber__.&nbsp;We see that when we execute our code it shows __16__ as the value of __myNewNumber__ and __17__ as the value of __myNumber __as __myNewNumber__ does not get incremented as only __myNumber__ get incremented as it is a post operator.

When we post-increment the value of the variable is incremented after assigning it to another variable.&nbsp;For example __myNumber__ is __16__ so it gets incremented after being assigned to __myNewNumber__ so therefore we get __17__.

Next week we will dive into Debugging Post-Increment Operator.