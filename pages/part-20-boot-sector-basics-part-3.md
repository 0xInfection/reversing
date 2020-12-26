# Part 20 - Boot Sector Basics \[Part 3\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Today we continue our Boot Sector Basics. Let's examine the code:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEiNTz3tBIr7g/article-inline_image-shrink_1000_1488/0/1546600881811?e=1614211200&amp;v=beta&amp;t=Ms5-_urNJVvO_qYnGfF-7438VEm6TSBxZo72NN2wXZE"/></div>

We add a string to our code as seen above and compile.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHlYsC28Elo5Q/article-inline_image-shrink_1000_1488/0/1546600938007?e=1614211200&amp;v=beta&amp;t=9uDtyFz3O7jHz-h8qdkkzCi4fKIbcbXe78IpfyB3GuY"/></div>

Let's examine the binary in a hex editor.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFxIaweKrFOxQ/article-inline_image-shrink_1000_1488/0/1546600963265?e=1614211200&amp;v=beta&amp;t=wTaa16oIdkj8b35w2aAiDaFBCE0oRCI8mnzFk505s-8"/></div>

Closely examine the above. We see our original code which we do not have to review however now we see a series of numbers, hex numbers that represent ASCII characters. We see that each letter corresponds with a letter. When we say that ultimately everything goes down to 0 and 1 this is a proof of concept. As you can see __EB __is selected above and we can see those hex values ultimately go to __11101011__ in binary.

Homework: Google and research the ASCII conversion table and do some research on your own and better understand how hex values represent characters.

Next week we take it to the next level. Stay tuned!