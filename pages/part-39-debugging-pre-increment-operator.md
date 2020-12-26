# Part 39 – Debugging Pre-Increment Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQGIZYwlBA99fg/article-inline_image-shrink_1000_1488/0/1526639245794?e=1614211200&amp;v=beta&amp;t=eVvTTprlCAOEqV7fpMN_zVznLH81lWT1GL6lJIYGuuk"/></div>

To compile this we simply type:

g++ example9.cpp -o example9

./example9

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQE75NiyR4ifTQ/article-inline_image-shrink_1000_1488/0/1526639272084?e=1614211200&amp;v=beta&amp;t=GudMLB3bIPwAh4DvMF4_aZfhFqBK7GLWN76V6OBOqyo"/></div>

We see 17 printed to the screen.

Let’s break it down:

We create a variable __myNumber = 16__ to which we create another variable __myNewNumber__ which pre-increments the value of __myNumber__.&nbsp;We see that when we execute our code it shows 17.

When we pre-increment the value of the variable is incremented before assigning it to another variable.&nbsp;For example __myNumber__ is __16__ so it gets incremented before being assigned to __myNewNumber__ so therefore we get __17__.

Let’s debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQHslw_KZKVWJQ/article-inline_image-shrink_1000_1488/0/1526639315124?e=1614211200&amp;v=beta&amp;t=rIddupyFWMyTKId7Bb1-Da4Fgv5rhmhfcqRA3mirrRw"/></div>

We do our normal start in gdb and break on main.&nbsp;Take note at __main+24__ we are moving the value of __1__ into __r3__.&nbsp;We then see at __main+28__ we are storing that value at __r11-8__ to which we will set a breakpoint and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQHWgyX00i86Ew/article-inline_image-shrink_1000_1488/0/1526639338414?e=1614211200&amp;v=beta&amp;t=qtUgbZmqC2dfqsqisZY6BsfmzvDi1fYdxaqKEj6ZQ14"/></div>

As we evaluate the value in __r3__ at this stage we see __17__.&nbsp;Remember back in our original code that the value in the __myNumber__ variable was __16__.&nbsp;We can see that the pre-increment operator was successful to increment the value __1__ to give us __17__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQGKrEmz0bC6kw/article-inline_image-shrink_1000_1488/0/1526639366619?e=1614211200&amp;v=beta&amp;t=XWukpz5i5U8FogJnw41wGDideBWZ_Bv8hQ9xbQ0iD60"/></div>

We see that when we continue through the code the value __17__ is successfully echoed to the terminal as expected.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQHghS8AmmLqoQ/article-inline_image-shrink_1000_1488/0/1526639388837?e=1614211200&amp;v=beta&amp;t=MbjxgZEvFGS5CQZ2Xzvbg1olaMhVG0E2flXEGqhmllE"/></div>

Next week we will dive into Hacking Debugging Pre-Increment Operator.