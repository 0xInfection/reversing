## Part 40 - Hacking Hello World!

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Ok it is time we look at the most basic C program, debug it and hack it. If we are to have mastery we must create and destroy in a single-step so that we have mastery over the domain.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1565910335250.jpg"/></div>

Let us fire up VIM and type out the following. We include our standard library and create a main function to which we use the library function of printf to echo a string of chars and since the type of main is int meaning integer we return 0.

Let us compile and see what happens when we run:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1565910684168.jpg"/></div>

As we see like we did in our C++ example we see '__Hello World!__' echoed successfully.

Let's debug in Radare:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566057508295.jpg"/></div>

This is simple, we use __aaa__ to analyze the binary and seek to main with __s sym.main__.

Let's look at the assembly and analyze:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1566057552155.jpg"/></div>

Assembly! The definition of raw sexy!

I went over this in detail in the previous lessons on Assembly but let us review.

1)We __push rbp __which means we push the value currently in the base pointer onto the stack.

2)We __lea rdi, qword str.Hello\_World __which means we load the effective address of the quad word of our string into the __rdi__ register. So far should be simple for you to follow along.

3)We then __call sym.imp.puts__ um wait! We used __printf__ what the hell! Well our compiler optimizes our code and the compiler chose the __puts__ function in the stdio library to echo the string to our terminal. Again easy enough.

4)We clean out __eax__ and then pop the original value in the __rbp__ register back into __rbp__. If you are confused by this review the earlier part of the series please.

We know our string '__Hello World!__' lives at a pretty house in Arlington, VA at the address of __0x2004__ well ok, it's not Arlington, VA but it is in mapped memory (since we are not technically debugging we are messing with mapped code meaning the same values on disk).

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1565911732441.jpg"/></div>

To confirm we see the value at __0x2004__ is '__Hello World!__' Let's hack that value to anything we want with the __w__ command and write directly to that mapped memory address.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1565911764019.jpg"/></div>

Let us re-examine who NOW lives in our Arlington, VA house!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1565911840111.jpg"/></div>

Success! We hacked the value and when we exit our debugger we see:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1565911868600.jpg"/></div>

We have successfully altered the binary.

This is alot to digest here. If you are stumped ask questions in the comments PLEASE! Do not continue as I am here to help. It is CRITICAL you understand these most basic things before we continue!