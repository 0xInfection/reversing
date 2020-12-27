## Part 35 - ASM Debugging 5 \[Indirect Addressing With Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our fifth program we demonstrated how we can manipulate indirect addressing with registers.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520483251669.jpg"/></div>

I want to start by addressing the question of why I use AT&amp;T syntax. In previous lessons I provided many ways to easily convert back and forth between AT&amp;T syntax and Intel syntax.

I deliberately choose this path so that it forces you to be comfortable with the most complex flavor of x86. If you are confused with this syntax please review the prior lessons as I go through the differences between both.

Let’s recap. We will use objdump to take a compiled binary such as the one above that we compiled in our last lesson and show how we can view it’s Intel source code.

__objdump -d -M intel indirect\_addressing\_with\_registers | grep \_start.: -A24 __

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148750030.jpg"/></div>

Now back to our regularly scheduled program.

Let’s load the binary into GDB and break on \_start, step a few steps and examine 6 of the 11 values inside the constants label.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520145698959.jpg"/></div>

We then move the memory address of the constants label into edi and move the immediate value of 25 decimal into the second index of our array. This is in essence a source code hack as we are changing the original value of 8 to 25.

If you examine the source code you see line 18 where we load the value of 1 into edi. Keep in mind this is the second value as arrays are 0 based.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520241367735.jpg"/></div>

You can see we changed the value of 8 decimal into 25 as explained.

This is our first introduction to arrays in assembly language. It is critical that you understand how they work as you may someday be a Malware Analyst or Reverse Engineer looking at the compiled binary of any number of higher-level program compiled arrays.

In our next lesson we will manually hack one of the values in GDB. Keep in mind, we will have to overwrite the contents inside an actual memory address with an immediate value. The fun is only beginning!

I look forward to seeing you all next week when we dive into hacking our fifth assembly program!