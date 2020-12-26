# Part 26 - ASM Debugging 2 \[Moving Data Between Registers\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s debug the second program below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG-3wBocPcG9Q/article-inline_image-shrink_1000_1488/0/1520143823093?e=1614211200&amp;v=beta&amp;t=gNSjB5Rp7DJQzUEfQdfRzL458UA-X_mwyZvPoBKAIho"/></div>

Lets fire up GDB and break on \_start, run the binary and disas:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHvCPh6ye_IEg/article-inline_image-shrink_1000_1488/0/1520559684472?e=1614211200&amp;v=beta&amp;t=Dm_o7VCAHXo-TMGDc3Mve2FQlUzZXbxafxZErgzaLo0"/></div>

Now lets __si__ twice and __i r__:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG5weq6I3RIiw/article-inline_image-shrink_1000_1488/0/1520203219432?e=1614211200&amp;v=beta&amp;t=q22QI8map6SmzGAGPqNoCMMCZP22OyKZkDokXQvd8nc"/></div>

As we can see the value of __0x16__ or __22__ decimal did move into EDX successfully. Now lets __si__ again.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHjBUYcs1wZGQ/article-inline_image-shrink_1000_1488/0/1520144473531?e=1614211200&amp;v=beta&amp;t=irArYVCrMSNDNZFqexGw9HlvbMFSWrF1c2n2zQRMigM"/></div>

As you can see we have successfully moved EDX into EAX.

I look forward to seeing you all next week when we dive into hacking our second assembly program!