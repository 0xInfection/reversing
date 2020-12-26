# Part 24 – Debugging SUB

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

As stated, subtraction in ARM has four instructions which are SUB, SBC, RSB and RSC. We will start today with SUB.

Please keep in mind when you add the S suffix on the end of each such as SUBS, SBCS, RSBS, RSCS, it will affect the flags. We have spent enough time on flags in the prior lessons so that you should have a firm grasp on this now.

Let’s re-examine our example of SUB:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGNYncBi1u5gQ/article-inline_image-shrink_1000_1488/0/1520242319262?e=1614211200&amp;v=beta&amp;t=yGVyY4CYaYYfm5odLkZIZD6eLIYhTGEigucWmfI-ZoI"/></div>

We simply take __67 decimal__ and move into __r1__ and __53 decimal__ and move into __r2__ and subtract r1 – r2 and put the result in __r0__.

Let’s debug.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEEItLzcF9iEQ/article-inline_image-shrink_1000_1488/0/1520211071860?e=1614211200&amp;v=beta&amp;t=UO3gLszLB_OyFDzeMWP3RQc5PsWgKhUlp4tfV1vg5dc"/></div>

As we can see the registers are clear. Lets step through and see what the value of __r0__ becomes.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH-r9wuFzXkiQ/article-inline_image-shrink_1000_1488/0/1520241790816?e=1614211200&amp;v=beta&amp;t=b-mMKANiy2mcECahVK1YAbIl5G8kG1DKOr0TSSQqqnE"/></div>

As you can see above __r0__ now has __decimal__ __14__ which works as expected.

Next week we will dive into SUB hacking.