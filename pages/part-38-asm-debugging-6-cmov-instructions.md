# Part 38 - ASM Debugging 6 \[CMOV Instructions\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Lets re-examine some source code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGOOpuoBls9HA/article-inline_image-shrink_1000_1488/0/1520234974923?e=1614211200&amp;v=beta&amp;t=egeAVQf1DBkHwM46Su06JBj-2unZAKyW-FT6_4sf70A"/></div>

Lets break on 0x08048092 which is line 31. Lets do a r to run and then type __print $ebx__. We can see the value of 7.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFAN6FeVgRwPg/article-inline_image-shrink_1000_1488/0/1520240729383?e=1614211200&amp;v=beta&amp;t=CvFG1xx9ojPNlw6nT1BockUesmLGI4yG8c3Wrz6lh60"/></div>

Ok now lets break on 0x080480b1 which is line 46. Remember when we are examining the value of __answer__, it has been converted to its ascii printable equivalent so in order to see the value of ‘7’ you would type __x/1c &amp;answer__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEj0DmfCZP6Rw/article-inline_image-shrink_1000_1488/0/1520498895208?e=1614211200&amp;v=beta&amp;t=UmjfvyShtAmZmWlE8VUEku66zZCUO8qf8GwuSoOGMf4"/></div>

I look forward to seeing you all next week when we dive into hacking our sixth assembly program!