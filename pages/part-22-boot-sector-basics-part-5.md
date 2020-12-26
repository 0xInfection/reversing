# Part 22 - Boot Sector Basics \[Part 5\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

This week we will focus on how to use QEMU which is an emulator to boot our simple new OS.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGpi-PK5j998Q/article-inline_image-shrink_1000_1488/0/1547804344026?e=1614211200&amp;v=beta&amp;t=IBztzEC3T4lBRbW-P1AV6bLVvaAezwaiVTaXD60l7Do"/></div>

Type the above to obtain qemu specifically for x86 systems.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFLr2K85q2lXQ/article-inline_image-shrink_1000_1488/0/1547804375264?e=1614211200&amp;v=beta&amp;t=QR17A5C0AWJQZVbL6gY7bft5Ylgs7P0gdMe9Rn39eHU"/></div>

Run the emulator with our binary.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFhj43ScF5wpQ/article-inline_image-shrink_1000_1488/0/1547804407713?e=1614211200&amp;v=beta&amp;t=orxVGVuFdI9RGCtJcRXY67JbS_BGAYwvxhKZwRN_aLg"/></div>

You will see the following. Keep in mind it does nothing but an infinite loop jump which we discussed in detail in previous lessons. This however is the most basic x86 OS one can create.

It simply looks for the signature which we spoke of last week (if this does not make sense please review last weeks lecture) and if it is exactly 200h bytes and it is placed at the first sector of the boot medium the process will be successful.

If you are interested there are different emulators for different architectures.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGzKF1C-YM79Q/article-inline_image-shrink_1000_1488/0/1547804592522?e=1614211200&amp;v=beta&amp;t=aIxHPRHo3GiK5D2oYN84pVt1uKo3JmZZUxT8-NGwhtk"/></div>

Next week we will discuss memory addressing so that we can set up a stack within our simple os.