# Part 29 - ASM Debugging 3 \[Moving Data Between Memory And Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s debug!&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQELk1JWHDXRRA/article-inline_image-shrink_1000_1488/0/1520241537282?e=1614211200&amp;v=beta&amp;t=wxz4GFSOQerLn5PBW1fDiVmNPoCL8cKDHUjdztwZxdg"/></div>

Specifically we will move the value of inside the constant integer of 10 decimal into ECX.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEOMiidq-M1SQ/article-inline_image-shrink_1000_1488/0/1520590508110?e=1614211200&amp;v=beta&amp;t=9w4KV6C3YNunOIRZDX1D5fCyLMKBfIK9qT2uvrQt6go"/></div>

We open GDB in quiet mode and break on \_start and run by following the commands above.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH-Xze0rkkRYA/article-inline_image-shrink_1000_1488/0/1520193652626?e=1614211200&amp;v=beta&amp;t=ee0Ncjmi1-QSIP1iLGH8ktddRe3MMs7j9EmgaVXyDV8"/></div>

As we can see when we info registers the value of ECX is 0.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHfV8fLsbsvYg/article-inline_image-shrink_1000_1488/0/1520590507589?e=1614211200&amp;v=beta&amp;t=YioiuEKoylbeFMVmyNcFgnZcCDW4Hr7KWlwpRF9MQa8"/></div>

After we step into twice, we now see the value of ECX as 10 decimal of 0xa hex.

I look forward to seeing you all next week when we dive into hacking our third assembly program!