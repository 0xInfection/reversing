# Part 20 - Boot Sector Basics \[Part 3\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we continue our Boot Sector Basics. Let's examine the code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/402499118.jpg"/></div>

We add a string to our code as seen above and compile.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="imgs/242972808.jpg"/></div>

Let's examine the binary in a hex editor.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/281927479.jpg"/></div>

Closely examine the above. We see our original code which we do not have to review however now we see a series of numbers, hex numbers that represent ASCII characters. We see that each letter corresponds with a letter. When we say that ultimately everything goes down to 0 and 1 this is a proof of concept. As you can see __EB __is selected above and we can see those hex values ultimately go to __11101011__ in binary.

Homework: Google and research the ASCII conversion table and do some research on your own and better understand how hex values represent characters.

Next week we take it to the next level. Stay tuned!