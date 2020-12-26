# Part 40 – Hacking Pre-Increment Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s one again re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber
= 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int
myNewNumber = ++myNumber;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout
&lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGGSCeZ81dxAg/article-inline_image-shrink_1000_1488/0/1527247718232?e=1614211200&amp;v=beta&amp;t=2wF8RoJBxFmwtLH-fBMuYSm1d2X92UyaiNHi9CB3aHM"/></div>

To compile this we simply type:

g++ example9.cpp -o example9

./example9

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEzYFvA9id5BQ/article-inline_image-shrink_1000_1488/0/1527247743089?e=1614211200&amp;v=beta&amp;t=0NbA_rhF0jdSKRxiu4s5aoeYYlsJMM5gCnZ1pZzm63M"/></div>

  

We see 17 printed to the screen.

Let’s break it down:

We create a variable __myNumber = 16__ to which we create another variable __myNewNumber__ which pre-increments the value of __myNumber__.&nbsp;We see that when we execute our code it shows 17.

When we pre-increment the value of the variable is incremented before assigning it to another variable.&nbsp;For example __myNumber__ is __16__ so it gets incremented before being assigned to __myNewNumber__ so therefore we get __17__.

Let’s debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH7rGJjXZNIWA/article-inline_image-shrink_1000_1488/0/1527247841094?e=1614211200&amp;v=beta&amp;t=ZRxKsK0YgKPhyLCFtq9u3YuvV4cpTYdHb2uZZbVyCHg"/></div>

We do our normal start in gdb and break on main.&nbsp;Take note at __main+24__ we are moving the value of __1__ into __r3__.&nbsp;We then see at __main+28__ we are storing that value at __r11-8__ to which we will set a breakpoint and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH0Ai26azwgrQ/article-inline_image-shrink_1000_1488/0/1527247877140?e=1614211200&amp;v=beta&amp;t=LWTuaPvvKNI9DHX3IiYi4OU1katWEhbUkyYGDgXQqrg"/></div>

As we evaluate the value in __r3__ at this stage we see __17__.&nbsp;Remember back in our original code that the value in the __myNumber__ variable was __16__.&nbsp;We can see that the pre-increment operator was successful to increment the value __1__ to give us __17__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFnexmmu5b6NQ/article-inline_image-shrink_1000_1488/0/1527247908955?e=1614211200&amp;v=beta&amp;t=hKipNfOr10DqzyLW8Oq1IkQ1PCCif8frakHIYBGu7pY"/></div>

We see that when we continue through the code the value __17__ is successfully echoed to the terminal as expected.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFpJRBHqQkFlw/article-inline_image-shrink_1000_1488/0/1527247930003?e=1614211200&amp;v=beta&amp;t=t-95RqYL5RmC0vxOGxcnn-3c-W59XKFWopmZac5zExI"/></div>

Let’s re-run the program.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHKvBrXb9CAtQ/article-inline_image-shrink_1000_1488/0/1527248017494?e=1614211200&amp;v=beta&amp;t=8u-OX1q_6G_uPJCElmfOb1HUCNa6ttcFVRZJHVWgufE"/></div>

Let’s hack!&nbsp;Here were review the value in r3 which we know to be 17.&nbsp;Let’s hack it to something else.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHbMkrTcwy82Q/article-inline_image-shrink_1000_1488/0/1527248050749?e=1614211200&amp;v=beta&amp;t=G567T344xQo-czKG9ylBy2r0vXz81IAN77BZ65CXqkk"/></div>

Success!&nbsp;As we can see when we continue we now see the hacked value echoing to the terminal.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEwftN7tm5Ynw/article-inline_image-shrink_1000_1488/0/1527248118408?e=1614211200&amp;v=beta&amp;t=AYXFWvxFa5dFpGvqm1JEhtR1inZQxR-G8DvKorJsFw4"/></div>

Next week we will dive into the Post-Increment Operator.

  

  