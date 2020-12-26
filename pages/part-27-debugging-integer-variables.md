# Part 27 – Debugging Integer Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code.&nbsp;I again want to include the below information from last week’s lesson to emphasize what is going on regarding integers.

A 32-bit register can store 2^32 different values. The range of integer values that can be stored in 32 bits depends on the integer representation used. With the two most common representations, the range is 0 through 4,294,967,295 (2^32 − 1) for representation as an (unsigned) binary number, and −2,147,483,648 (−2^31) through 2,147,483,647 (2^31 − 1) for representation as two's complement.

Keep in mind with 32-bit memory addresses you can directly access a maximum of 4 GB of byte-addressable memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEgOmunABZR9Q/article-inline_image-shrink_1000_1488/0/1520217390524?e=1614211200&amp;v=beta&amp;t=aUsuadmkyJCWWdW30FXeB7euTZWFGeswzPZRIGV41o0"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH4lRxHfajGFQ/article-inline_image-shrink_1000_1488/0/1520233314454?e=1614211200&amp;v=beta&amp;t=TNO5iB2UO3mmrUWENN4_7Qjg3O5otY5vur-Tep5jOeE"/></div>

We see at __main+12 __the address at __0x10730 __loading data into __r3__.&nbsp;Let’s take a closer look.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH5Z2EDTfO95A/article-inline_image-shrink_1000_1488/0/1520192010424?e=1614211200&amp;v=beta&amp;t=hYNEzxqHHW2z_qv1YZXlmhI2Kr7AY7Kz_imkdZuVqTw"/></div>

When we examine the data inside __0x10730__ we clearly see the integer __777__ present.&nbsp;When we continue we see __777 __echoed back to the terminal which makes sense as we utilized the __cout__ function within c++.\#linux \#arm \#asm \#cplusplus \#reverseengineering

Next week we will dive into Hacking Integer Variables.