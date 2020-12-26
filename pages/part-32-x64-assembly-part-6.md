# Part 32 - x64 Assembly \[Part 6\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let's again review our source code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFkuQVAI7K9yw/article-inline_image-shrink_1000_1488/0/1553853169947?e=1614211200&amp;v=beta&amp;t=RuIHTtmQ8NPd8AFgdiGJPmcl1_tnbCYgLIlEdagl9Ng"/></div>

Let's compile...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHpIdxHsGfWzg/article-inline_image-shrink_1000_1488/0/1553853185424?e=1614211200&amp;v=beta&amp;t=e3tedTBG1kUM0q73geebuWWWNcRKcqhKNM_x9bru-1w"/></div>

As we have seen before it produces our string.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEWLfhR-z3pZA/article-inline_image-shrink_1000_1488/0/1553853213341?e=1614211200&amp;v=beta&amp;t=uw-uGYM25m3aHDbpR9oV0MXk1J0Pi8CNSTmmSAwowS8"/></div>

We debug and see the string being moved into __0x6000d8__ and then __RSI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGzJDJbDIwVhg/article-inline_image-shrink_1000_1488/0/1553853259407?e=1614211200&amp;v=beta&amp;t=XjlbuMAjBnDl3pzqVmUMqs5a3AUndxI_kXjkJWUrmeo"/></div>

Just to verify we can see the string at the aforementioned address. NOW FOR A BIT OF FUN :)...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHvCI2zv9mhkw/article-inline_image-shrink_1000_1488/0/1553853296959?e=1614211200&amp;v=beta&amp;t=-yyJZ4q1M4QYuTbF_4n6IRdqAkpRNqIwdqsP777kuTs"/></div>

Here we demonstrate we have the power to simply hack and redefine the string in memory. We are simply setting a char byte length and setting a new string.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEEaDkAAZehvA/article-inline_image-shrink_1000_1488/0/1553853373225?e=1614211200&amp;v=beta&amp;t=iOb86Sh62beuI0R7Tgdfhs2tGqtTmRYv9PzDv-U4D5Q"/></div>

As we can see we have successfully altered the string in memory.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFQuIyqZscy5w/article-inline_image-shrink_1000_1488/0/1553853413835?e=1614211200&amp;v=beta&amp;t=9_l0T8eeqoSGBW-IhUeuJ9-PmO7KliiUHL3aZ4OKzks"/></div>

We continue and run through the binary and see that our hack continues through __RSI__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEjZ0vlo3Qn-Q/article-inline_image-shrink_1000_1488/0/1553853461475?e=1614211200&amp;v=beta&amp;t=QWA6HzLFBdnZJDMj9Oez3_mrjJcaE6evkAKKnXopGr8"/></div>

Finally we see when we run the binary we have successfully hacked it's operation. This is a very simple example however shows the power of truly understanding assembly at this level. GUI debugger tools will also provide this functionality however I like to use the command line tools so that they could be used on every environment.

The purpose of these tools is to UNDERSTAND how this is done and what to look for when you are professionally reversing in real-time. You need to understand how an attacker can alter memory and/or instructions. We need more professional RE's to help defend infrastructures throughout the world and hopefully these tutorials motivate you toward a career in such.