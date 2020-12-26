# Part 34 – Hacking Double Variables

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s review our code.

<pre spellcheck="false">int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; double myNumber = 1337.77;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGLd3n8WpFNwQ/article-inline_image-shrink_1000_1488/0/1523615576064?e=1614211200&amp;v=beta&amp;t=kmdkqZD6pX7LrO-BrSOl1d7l9nQobQb67P0-xIm55BM"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFpJt9hSeZsPw/article-inline_image-shrink_1000_1488/0/1523615640968?e=1614211200&amp;v=beta&amp;t=JcCX01aDTuN74muhsrpjl2I1s3zCyNBImnNUYHzw1kQ"/></div>

Let’s set a breakpoint at __main+24__ and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEXhoAmgbn53g/article-inline_image-shrink_1000_1488/0/1523615666432?e=1614211200&amp;v=beta&amp;t=41AeHp6OUfIYUtLg5iK8GRRy6qxDsoid3ncAQVe4z14"/></div>

We see the __strd r2, \[r11, \#-12\]__ and we have to fully understand that this means we are storing the value at the offset of __-12__ from register __r11__ into __r2__.&nbsp;Let’s now examine what exactly resides there.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHsOtL3xer-rA/article-inline_image-shrink_1000_1488/0/1523615689648?e=1614211200&amp;v=beta&amp;t=C9tjBb6N-74_nFLdeM_V37sfZ0GDN-gGmXnvn6mAczk"/></div>

Voila!&nbsp;We see __1337.77__ at that offset location or specifically stored into __0x7efff230__ in memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEz6bj7hNd5Dw/article-inline_image-shrink_1000_1488/0/1523615716304?e=1614211200&amp;v=beta&amp;t=iIf9BpdFBovowk6UEwTPwzOpPY6PEZdILxe-GjmmNaY"/></div>

Let’s step into twice which executes the __vldr d0, \[r11, \#-12\]__ as we understand that __1337.77__ will now be loaded into the double precision math coprocessor __d0 __register.&nbsp;Let’s now print the value at that location below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH0sWQh2CZMBA/article-inline_image-shrink_1000_1488/0/1523615745800?e=1614211200&amp;v=beta&amp;t=aWlmDcKu4GbuLOilaM8UT6fjowwKt2vAzKnUIjCVvwc"/></div>

Let’s hack the __d0__ register!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFHoOV0GfR3lQ/article-inline_image-shrink_1000_1488/0/1523615775560?e=1614211200&amp;v=beta&amp;t=y5Moa8Y-_nvzhEiPl8WUqsIOf70a0XSv6uNeQyoRPrA"/></div>

Now let’s reexamine the value inside __d0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHInrzbBhhUKg/article-inline_image-shrink_1000_1488/0/1523615802811?e=1614211200&amp;v=beta&amp;t=UpLgNkplYLSeMC7koZBVf8V_PQEHd5Ogy9cm0_RmgoI"/></div>

Let’s continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFVOohnNfJUlg/article-inline_image-shrink_1000_1488/0/1523615835964?e=1614211200&amp;v=beta&amp;t=1451rSdJIfRvs1VzATSeDqjfkvKExyLZVp3egTcXHkA"/></div>

Successfully hacked!

Next week we will dive into the SizeOf Operator.