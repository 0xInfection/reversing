# Part 38 – Pre-Increment Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The next stage in our journey is that of the pre-increment operator.&nbsp;

Let’s examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNewNumber = ++myNumber;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFl1kw-26V6pg/article-inline_image-shrink_1000_1488/0/1526036616866?e=1614211200&amp;v=beta&amp;t=G-kQS1i6E1fNS_tOfvkLzQ_LmoInMxvdKVb63si3Vaw"/></div>

To compile this we simply type:

g++ example9.cpp -o example9

./example9

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE0hxqk9fJLyQ/article-inline_image-shrink_1000_1488/0/1526036640627?e=1614211200&amp;v=beta&amp;t=AOYJO94qJf8w-o9-ey2lS2OB5A4kboFsPTmz4YfzR4o"/></div>

We see 17 printed to the screen.

Let’s break it down:

We create a variable __myNumber = 16__ to which we create another variable __myNewNumber__ which pre-increments the value of __myNumber__.&nbsp;We see that when we execute our code it shows 17.

When we pre-increment the value of the variable is incremented before assigning it to another variable.&nbsp;For example __myNumber__ is __16__ so it gets incremented before being assigned to __myNewNumber__ so therefore we get __17__.

Next week we will dive into Debugging Pre-Increment Operator.