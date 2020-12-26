# Part 4 - Number Systems

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Binary addition can occur in one of four different fashions:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEHGI2NtcbEpw/article-inline_image-shrink_1000_1488/0/1536919520880?e=1614211200&amp;v=beta&amp;t=g5nDW8-pjzrtS-zceS15nmDthMX0K0FSCSvkG--z_jE"/></div>

Keep in mind the (1) means a carry bit. It very simply means an overflow.

Lets take the following 4-bit nibble example:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEuxTFAbWL4pg/article-inline_image-shrink_1000_1488/0/1536919547320?e=1614211200&amp;v=beta&amp;t=H8qaDhoHP1j9uJo-G3YozEuy_pQDj-EvxHqUK1cttkQ"/></div>

We see an obvious carry in the 3rd bit. If the 8th bit had a carry then this would generate a carry flag within the CPU.

Let’s examine an 8-bit number:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGZ7rS85AhNJg/article-inline_image-shrink_1000_1488/0/1536919574450?e=1614211200&amp;v=beta&amp;t=ky71UsTeRPpgjoXtyPONCvZAD-IG8pUrPf5UqSXx0Z4"/></div>

If we had:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEcKfjjIlVIBQ/article-inline_image-shrink_1000_1488/0/1536919592305?e=1614211200&amp;v=beta&amp;t=xPWOuFkAYw-aIBMVc7xIBg9zB4IzV6KAEoUc8-Wl30A"/></div>

Here we see a carry bit which would trigger the carry flag within the CPU to be 1 or true. We will discuss the carry flag in later tutorials. Please just keep in mind this example to reference as it is very important to understand.

Next week we will dive into binary subtraction! Stay tuned!