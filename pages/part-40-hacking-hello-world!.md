# Part 40 - Hacking Hello World!

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In C we have several data types to which we can create variables. I will use a few simple examples:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF0lTxSlpkdzg/article-inline_image-shrink_1000_1488/0/1566059490750?e=1614211200&amp;v=beta&amp;t=X5ccABhSzmE5bD2gmva5FJplThR2c_xONsBYsxI-R14"/></div>

Let's compile and run:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFMa_KQ9e7L7w/article-inline_image-shrink_1000_1488/0/1566059504696?e=1614211200&amp;v=beta&amp;t=sukddB6YZTWB61SyOEyc2-u40daJfLEzGZhZYundQu8"/></div>

Ok as we can see we have a character an integer and a double. These are some of the most basic data types in C to which we have created a series of variables as shown above.

Let us load the binary into Radare:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG88rogOT--Rg/article-inline_image-shrink_1000_1488/0/1566059659639?e=1614211200&amp;v=beta&amp;t=KtzF4AeYMvnrTV8zYWSyKKTYdTstKBPBUF-bYyuen5E"/></div>

Let's disassemble at main:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGJFXIxmucxlA/article-inline_image-shrink_1000_1488/0/1566059725847?e=1614211200&amp;v=beta&amp;t=1Bet2_2GjTOn4YHp6UZI0DneGwgbdjFCOY-4Asx_vP4"/></div>

Ok very simply we see 3 variable declarations defined up at the top in reverse order as they are __local\_1h __which is our __char a,__ __local\_8h__ which is our __int b__ and __local\_10h__ which is our __double c__. You can also see the __rbp__ base pointer allocating space for these variables. This is nice pseudo code that the debugger shows you up top.

Ok stay with me!

Within memory at __0x0000113d __we see the instructions __mov byte \[local1\_h\], 0x61__ which is in our ascii table a lowercase '__a'__. We know that \[local1\_h\] is not real code however what is going on under the hood is the fact that these variables are pushed onto the stack in reverse order as we can see above. Therefore, if we were to hack our code to something like __mov byte \[rbp-0x1\], 0x62 __what do you think might happen? Very simple, we know that in reality the code at the mapped memory address of __0x0000113d__ what is really going on is __mov byte \[rbp-0x1\], 0x61__. Quite simply what we have just done is hack our value of '__a__' to '__b__'. This should hopefully make sense to you.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE3YbPwMU1fZQ/article-inline_image-shrink_1000_1488/0/1566060689050?e=1614211200&amp;v=beta&amp;t=Tidp_5u84y163rKBa8kFotsuOzWdqTqLucNnp2-2mOs"/></div>

Now let us re-examine our binary:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE8R6N6YFxKbw/article-inline_image-shrink_1000_1488/0/1566060755864?e=1614211200&amp;v=beta&amp;t=Q3vCC9KZIt-ZMZYbNohvupWuoxXkk77ulPo6jwAnueg"/></div>

As we can clearly see at memory address __0x0000113d __we in fact see '__b__'. We have successfully hacked this portion.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFSACBZ6FLNLw/article-inline_image-shrink_1000_1488/0/1566060872094?e=1614211200&amp;v=beta&amp;t=viCIGWFdU2K9ClpVrNu16mdK0fRkMfP7MVckDtcTIHM"/></div>

We exit out of Radare and re-run the binary and we can see we have successfully hacked the value.

HOMEWORK TIME! I want you to with this knowledge now hack the __int__ and the __double__. I want you to put your results in the comment sections below. It is VERY important that you type all of this out and actually explore the exercises so I am looking forward to seeing your hacks in the comments!