# Part 31 - x64 Assembly \[Part 5\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's review our code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQElNN_jEOL1BA/article-inline_image-shrink_1000_1488/0/1553248751760?e=1614211200&amp;v=beta&amp;t=kM0LO-0o2zwHqVXB3Cdbc-OVQ4pM61KFFA9ZLwkje8M"/></div>

Compile...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHZZXT8eNsPtQ/article-inline_image-shrink_1000_1488/0/1553248766003?e=1614211200&amp;v=beta&amp;t=v1I8qrtpJ90W8bkRnD4in1ciuV0QhbRrUBUztloznP0"/></div>

Debug...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEuLBaBtI8MTw/article-inline_image-shrink_1000_1488/0/1553248783477?e=1614211200&amp;v=beta&amp;t=tGW5Z4y3F3Gsp0WWhYqYpvQgTpTOk8_Jle8a9sz4zk0"/></div>

Let's evaluate what is inside the memory address of 0x6000d8.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG9j-_tdPqNAw/article-inline_image-shrink_1000_1488/0/1553248844375?e=1614211200&amp;v=beta&amp;t=Jrbii9tYGCkHpXZ3gakSK3SBw81AXhnt5Xo4BW6MV7Y"/></div>

As we can see "__Hello World__" with the return character will then be moved into our __RSI__ register.

Next week we will examine this a bit closer.