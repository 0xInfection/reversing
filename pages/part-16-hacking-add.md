# Part 16 - Hacking ADD

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s again review our ADD example below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148983155.jpg"/></div>

Let’s debug:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143258587.jpg"/></div>

We see the value of __67__ decimal is being moved into __r1__ below:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520171779364.jpg"/></div>

Let’s hack! Lets set __r1 = 66__!

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520211664200.jpg"/></div>

Now we see we have hacked the program so when it adds the values it will have a different output. If you remember back to the last lecture, __r0 = 120__. Here we see we have hacked r1 and now the value of __r0__ is __119__!

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520211540477.jpg"/></div>

This is the power of understanding assembly. This is a VERY simple example however with each new series as I have stated we will create a program, debug and hack it.

This combination of instructions will help you to get hands on experience when learning how to have absolute control over an application and in the case of malware reverse engineering gives you the ability to make the binary do exactly what you want!

Next week we will dive into ADDS.