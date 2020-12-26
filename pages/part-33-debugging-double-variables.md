# Part 33 – Debugging Double Variables

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQHq9rfPCwU4uQ/article-inline_image-shrink_1000_1488/0/1523008391034?e=1614211200&amp;v=beta&amp;t=GFOm5M8Hs8kCCPgV7jek11DjQQHepThKkeeR530LJec"/></div>

Let’s debug!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQF13hr1oUP_5g/article-inline_image-shrink_1000_1488/0/1523008417137?e=1614211200&amp;v=beta&amp;t=83-2cNtEj1cuo596cGFrENjG7Q6yCBvt74YaSRnbhFE"/></div>

Let’s set a breakpoint at __main+24__ and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQGa4yo-7prDWA/article-inline_image-shrink_1000_1488/0/1523008442868?e=1614211200&amp;v=beta&amp;t=QYuRLbgiye9e5nVz6CTu-lhZFTIc8HOG7zbcR8ni93k"/></div>

We see the __strd r2, \[r11, \#-12\]__ and we have to fully understand that this means we are storing the value at the offset of __-12__ from register __r11__ into __r2__.&nbsp;Let’s now examine what exactly resides there.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQFzD9zGbbGeoQ/article-inline_image-shrink_1000_1488/0/1523008470513?e=1614211200&amp;v=beta&amp;t=oRrvF_Bm2odlVHEdhm0jwo-WXXsWrQImmM_UPUfiX6I"/></div>

Voila!&nbsp;We see __1337.77__ at that offset location or specifically stored into __0x7efff230__ in memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQGEW_Jfno00OQ/article-inline_image-shrink_1000_1488/0/1523008491495?e=1614211200&amp;v=beta&amp;t=B_4akLByN7VCBXgrqvf-L1jhcuctoNOZVyj5GWGjWQg"/></div>

Let’s step into twice which executes the __vldr d0, \[r11, \#-12\]__ as we understand that __1337.77__ will now be loaded into the double precision math co-processor __d0 __register.&nbsp;Let’s now print the value at that location below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQEkRvTaRmXHoQ/article-inline_image-shrink_1000_1488/0/1523008515533?e=1614211200&amp;v=beta&amp;t=stiDRksg4r1mBz7sSlSvA5H6jdjTVjBRCt8m5Pf0-B0"/></div>

Finally let’s continue and watch the value echo to the terminal.&nbsp;This completes our __cout__ c++ function.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C5612AQExaYtUzNoWKQ/article-inline_image-shrink_1000_1488/0/1523008538297?e=1614211200&amp;v=beta&amp;t=M_0UZ1oKWykW6QF0sxtrVHi_dQXu5Ax6eFMOOVO6o44"/></div>

Next week we will dive into Hacking Double Variables.