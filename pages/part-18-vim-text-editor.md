# Part 18 - vim Text Editor

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Now that we have a working version of Linux, we need a text editor that we can work with in the terminal.

To begin, open your terminal and type:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="imgs/703651578.jpg"/></div>

This will open up the vi text editor.&nbsp;The first thing you need to type is the letter ‘i’ to set the editor to insert mode so you may begin typing.

<div class="slate-resizable-image-embed slate-image-embed__resize-left"><img src="imgs/425100774.jpg"/></div>

&nbsp;&nbsp;

After you a done typing, press the ‘__esc__’ key and type ‘__:wq__’ and press enter.

Congratulations! You created your first file! This is a one time file that we need to create in order to use our text editor they way we want it to perform.

The first line states __set number__ which means we would like each file to show line numbers as this is essential for debugging code. The__ set smartindent__, __set tabstop__, __set shiftwidth__ and __set expandtab__ statements set forth rules to properly format code and allow 4 spaces per tab indent which will help our code to look clean.

There are several commands you need to be aware of. Keep in mind, to go into command mode rather than insert mode you must press the ‘__esc__’ key. Below are the most common commands:

__j__ or down-arrow \[move cursor down one line\]

__k__ or up-arrow \[move cursor up one line\]

__h__ or left-arrow \[move cursor left one character\]

__l__ or right-arrow \[move cursor right one character\]

__0__ \[move cursor to the start of the current line\]

__$__ \[move cursor to the end of the current line\]

__b__ \[move cursor back to the beginning of preceding word\]

__dd__ \[deletes the line the cursor is on\]

__D__ \[deletes from the cursor position to the end of the line\]

__yy__ \[copies the current line\]

__p__ \[puts the copied text after the cursor\]

__u__ \[undo the last change to the file\]

__:w__ \[save file\]

__:wq__ \[save file and exit text editor\]

__:q!__ \[quit text editor and do not save any changes\]

You will be consistently moving between command mode ‘__esc__’ and insert mode ‘__i__’. Remember that when you want to insert characters you need to be in insert mode and when you want to move the cursor other than moving to the next line, you need to be in command mode.

Now that we have vi configured, lets install vim which has some better functionality. Simply type:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/879562831.jpg"/></div>

Once that is installed instead of using vi we will now use vim.

I look forward to seeing you all next week when we talk about why it’s important to learn Assembly Language.