<h1>Part 36 – Debugging SizeOf Operator</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>Let’s re-examine our code.</p><pre spellcheck="false">#include &lt;iostream&gt;

 

int main(void) {

            int myNumber = 16;

            int myNumberSize = sizeof(myNumber);

 

            std::cout &lt;&lt; myNumberSize &lt;&lt; std::endl;

 

            return 0;

}
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHgptQ_VQwSZw/article-inline_image-shrink_1000_1488/0/1524823603695?e=1614211200&amp;v=beta&amp;t=JE95HGnqcS65BCLU9o0VR_kaRgDv8pkvxCd92GsjBxs"/></div><p>Remember that we create a variable <strong>myNumber = 16</strong> to which we create another variable <strong>myNumberSize</strong> which holds the value of the size of <strong>myNumber</strong>. We see that when we execute our code it shows 4 therefore we see that the SizeOf operator indicates an integer is 4 bytes wide.</p><p>Let’s debug and break on main.</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEUTym-EpArug/article-inline_image-shrink_1000_1488/0/1524823663114?e=1614211200&amp;v=beta&amp;t=a-UOAx5zKYDuuidewLOUyojPbLzpbPOTtwmkTp5m1e8"/></div><p>Let’s break on <strong>main+20</strong> as we can see the value of <strong>4</strong> being moved into <strong>r3</strong>.</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG3JSeuH4rvdw/article-inline_image-shrink_1000_1488/0/1524823735285?e=1614211200&amp;v=beta&amp;t=c-aAhv1tX9TMJfT7RrnP46mvWGSHfNj_wjpNi013s9k"/></div><p>Let’s examine what is going on at <strong>main+16</strong> as we can see that we are storing into the value of <strong>$r11-8</strong> that which exists in <strong>r3</strong> which in our case is <strong>16</strong>. This makes sense as when we examine our original code the value of <strong>myNumber</strong> was in fact <strong>16</strong>. We can see this here when we examine the value inside <strong>$r11-8</strong>.</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHHobJZaa2g0w/article-inline_image-shrink_1000_1488/0/1524823766343?e=1614211200&amp;v=beta&amp;t=MnA-lXx0X037uMcHovipABMEDTU9qkBAFhNT-T1eo-0"/></div><p>As we can see above the value inside <strong>$r11-12</strong> is<strong> 4</strong> as that represents the value that <strong>SizeOf</strong> is returning as the integer <strong>16 </strong>is in fact 4 bytes wide.</p><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGPlLoacEIaIQ/article-inline_image-shrink_1000_1488/0/1524823791885?e=1614211200&amp;v=beta&amp;t=oLfyQR0QByyxrlAAsBBb7fm5Bhip3qLL1y1Ecxfnzh0"/></div><p>Finally when we continue execution we in fact see the value <strong>4</strong> echoed to the terminal.</p><p>Next week we will dive into Hacking SizeOf Operator.</p>