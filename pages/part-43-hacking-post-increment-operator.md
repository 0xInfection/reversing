# Part 43 – Hacking Post-Increment Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

We create a variable&nbsp;__myNumber = 16&nbsp;__to which we create another variable&nbsp;__myNewNumber__ which post-increments the value of&nbsp;__myNumber__.&nbsp;We see that when we execute our code it shows&nbsp;__16__&nbsp;as the value of&nbsp;__myNewNumber__&nbsp;and&nbsp;__17__&nbsp;as the value of&nbsp;__myNumber&nbsp;__as&nbsp;__myNewNumber__&nbsp;does not get incremented as only&nbsp;__myNumber__&nbsp;get incremented as it is a post operator.

When we post-increment the value of the variable is incremented after assigning it to another variable.&nbsp;For example&nbsp;__myNumber__&nbsp;is&nbsp;__16__&nbsp;so it gets incremented after being assigned to&nbsp;__myNewNumber__&nbsp;so therefore we get&nbsp;__17__.

Let's debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/469972610.jpg"/></div>

Let's break on&nbsp;__\*main+28__&nbsp;and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/175793367.jpg"/></div>

As we can see the value in&nbsp;__r3__&nbsp;is __16__ and the value in&nbsp;__r2__&nbsp;is __17__. We can see that as they are loaded from memory into the registers in&nbsp;__\*main+12__&nbsp;directly by the&nbsp;__mov__&nbsp;instruction and&nbsp;__\*main+24__&nbsp;we add __1__ into&nbsp;__r3__&nbsp;and then put that value into&nbsp;__r2__.

Let's hack this baby!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/632871842.jpg"/></div>

We know we can now set the value of __r3__ to our heart's desire!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/750991630.jpg"/></div>

As we continue we see the c++ __cout__ function echo our new hacked value to the screen!

Next week we will dive into the Pre-Decrement Operator.