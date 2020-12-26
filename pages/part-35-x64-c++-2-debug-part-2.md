# Part 35 - x64 C++ 2 Debug \[Part 2\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's review our code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQGrgrQLGRgjew/article-inline_image-shrink_1000_1488/0/1564757193950?e=1614211200&amp;v=beta&amp;t=kVYVxxQETwgEJ6zWm9ViX2uICON0ZDuy5GhcTkZ1J6E"/></div>

Compile:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQFpqdYdPykJbQ/article-inline_image-shrink_1000_1488/0/1564758303402?e=1614211200&amp;v=beta&amp;t=xFZg6K6urV0xy0IT897Vlh65G1joO8AyhgQQ8SoG4Qc"/></div>

Run:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQFSP-goeevtuw/article-inline_image-shrink_1000_1488/0/1564757239511?e=1614211200&amp;v=beta&amp;t=zNvuVN4dmg0EK2XLiZ_wLG1iZvpNE77YI_BEfVzmDmg"/></div>

Let's remember this line above when we compare against our hacked binary.

Let's open up our binary for write mode and simply analyze the binary.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQF6mr5D-4oIxw/article-inline_image-shrink_1000_1488/0/1564757311281?e=1614211200&amp;v=beta&amp;t=gPgvpS0TN7-TDqBF367QnrdmsoDhnWr4Bpu6pvWOzLA"/></div>

Ok, there is a lot going on here. Let's break it down. First, we open up Radare 2 in write mode by typing '__r2 -w ./1__' and then use the '__aaa__' command to analyze the binary. We then use '__s sym.main__' to seek to the main routine of the binary which is our entry point. We then do a '__pdf__' command to disassemble the binary.

We see what we refer to as the prologue where we push&nbsp;__rbp__&nbsp;the stack base pointer onto the stack. We then move&nbsp;__rsp__&nbsp;into&nbsp;__rbp__&nbsp;for safe keeping and then we reserve&nbsp;__0x10__&nbsp;hex bytes or 16 decimal bytes on the stack to make room for our string.

If none of this makes sense please go back to the beginning of the tutorial series to review basic assembly and the registers as it is CRITICAL you understand this before we move forward.

We can clearly see the qword of '__Hello World\\n__' at memory address&nbsp;__0x2005__&nbsp;and then we see our C++ library call for the output stream which is&nbsp;__cout__&nbsp;to display our string to the terminal.

Let's examine&nbsp;__0x2005__&nbsp;to verify that our string is at that location:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQHkJWtDc7EmeA/article-inline_image-shrink_1000_1488/0/1564757423920?e=1614211200&amp;v=beta&amp;t=UQkfF7VPhlpeWnX_f8z5Tc7xbikQCdyj6uXN4RIqpN4"/></div>

NOW TIME FOR THE HACK!

Let's hack the value to something like:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQFMs_3AsySrOw/article-inline_image-shrink_1000_1488/0/1564757454631?e=1614211200&amp;v=beta&amp;t=F3QPVQF5yL5ghoL-upyMWAoYrkRbhIyQunaEydYI9Tw"/></div>

Now let's see what is now inside memory value @ __0x2005__!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQG0emToOChRsQ/article-inline_image-shrink_1000_1488/0/1564757528202?e=1614211200&amp;v=beta&amp;t=7-e4rvFQjki1BhF17VYzwjzJuqTiwvgwzANbxLHat90"/></div>

BOOM! As we can see we have hacked the value and when we quit Radare 2 it will write it and modify our binary as such.,

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQEkfli50BnScQ/article-inline_image-shrink_1000_1488/0/1564757568026?e=1614211200&amp;v=beta&amp;t=bNldz3ZvmX-freL4QDoKFrD4N6Ob5MpSq-UY7tb71eU"/></div>

As you can see we have hacked the binary! This is very basic but now you have an elementary level of understanding of Reverse Engineering a C++ binary.

Next week we will continue our journey into C and step-by-step reverse engineering.