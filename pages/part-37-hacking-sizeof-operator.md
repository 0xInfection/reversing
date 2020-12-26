# Part 37 – Hacking SizeOf Operator

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s re-examine our code.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumberSize = sizeof(myNumber);

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumberSize &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEpE1ZooJR-rA/article-inline_image-shrink_1000_1488/0/1525429032559?e=1614211200&amp;v=beta&amp;t=fog91Wr6cCGUKW0qZniZT-fTmvBjVQPpSWFtAMFoyh0"/></div>

Remember that we create a variable __myNumber = 16__ to which we create another variable __myNumberSize__ which holds the value of the size of __myNumber__.&nbsp;We see that when we execute our code it shows 4 therefore we see that the SizeOf operator indicates an integer is 4 bytes wide.

Let’s review last week’s code as we start with debugging and breaking on main.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGombOe64AHYw/article-inline_image-shrink_1000_1488/0/1525429072643?e=1614211200&amp;v=beta&amp;t=v8Ecj8g1UQgb_mo-_ge6bBIq0_EEkP0ZZWWzkZkS-2U"/></div>

Let’s break on __main+20__ as we can see the value of __4__ being moved into __r3__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGZzt2H1gO6Ng/article-inline_image-shrink_1000_1488/0/1525429109049?e=1614211200&amp;v=beta&amp;t=Wm--Y966fPj86rjWdqr8YeV_AmQiuItUyQrpw_moF64"/></div>

Let’s examine what is going on at __main+16__ as we can see that we are storing into the value of __$r11-8__ that which exists in __r3__ which in our case is __16__.&nbsp;This makes sense as when we examine our original code the value of __myNumber__ was in fact __16__.&nbsp;We can see this here when we examine the value inside __$r11-8__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF347FWqUQLgw/article-inline_image-shrink_1000_1488/0/1525429200465?e=1614211200&amp;v=beta&amp;t=9k7zExommXDLg-Zyi9ouW4LYDlQQq3sYB6d6NMwI1cg"/></div>

As we can see above the value inside __$r11-12__ is__ 4__ as that represents the value that __SizeOf__ is returning as the integer __16 __is in fact 4 bytes wide.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGvED2Tu0AkgA/article-inline_image-shrink_1000_1488/0/1525429249458?e=1614211200&amp;v=beta&amp;t=Kw_c8q3r-oP_nx6OtURO4VDLcruSwsxiHIXr6oCW7yE"/></div>

Finally when we continue execution we in fact see the value __4__ echoed to the terminal.

Let’s hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEoruTVI9YtvA/article-inline_image-shrink_1000_1488/0/1525429287002?e=1614211200&amp;v=beta&amp;t=D3fLh_rkJUDSuTSyJ0BgzEqRiQLOyJlaEIoG4Tfz44E"/></div>

We run and break on __main+28__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFQNixyxSeE3g/article-inline_image-shrink_1000_1488/0/1525429310244?e=1614211200&amp;v=beta&amp;t=XinRBAEitQL2198eS1_5a3u2_ROSuoYkvZptybwQV8E"/></div>

We see the value in __r3__ is __4__ which is expected.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG4OW-9axGUAA/article-inline_image-shrink_1000_1488/0/1525429336631?e=1614211200&amp;v=beta&amp;t=BBDwsH6JHFsWV9q1pITguax0beEeJCFEks5BS5e_Og8"/></div>

We break on __main+36__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH78Te-swZRnA/article-inline_image-shrink_1000_1488/0/1525429367083?e=1614211200&amp;v=beta&amp;t=uPjem_s1lUWprpi_j_mjP7gQxOjW7HTAFs2me5fS8XM"/></div>

We see the value in __r1__ is __4__ which should make logical sense as the value was stored from __r3__ into __r11-12__ and then back to __r1__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFCMNWoL5zqug/article-inline_image-shrink_1000_1488/0/1525429391206?e=1614211200&amp;v=beta&amp;t=qRQw89cdBPIDkSDSALFgTVvCaB6_-YIRhpS-QO6h4Zk"/></div>

Let’s hack the value in __r1__!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF4slwiFCRpnQ/article-inline_image-shrink_1000_1488/0/1525429414806?e=1614211200&amp;v=beta&amp;t=TaLF_EpQO_ajhTYwf_3Yng6JP1sMpkPgF5Z8GFmCcWE"/></div>

Success!&nbsp;We have hacked the machine!

Next week we will dive into the Pre-Increment Operator.