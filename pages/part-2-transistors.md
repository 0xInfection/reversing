# Part 2 - Transistors

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our last tutorial we spoke briefly about binary to which we represent as either true or false.&nbsp;In binary, true is equal to 1 and false is equal to 0.&nbsp;Computers are ultimately built on this very simple concept to which at the core we have four possible logic gates which can be combined in an infinite amount of sequences.

Let’s start with the __AND Gate __below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGxanFD1TKo6A/article-inline_image-shrink_1000_1488/0/1535712345568?e=1614211200&amp;v=beta&amp;t=vtlDrCAGPOMkbjNQB16aHl6f9ha94th2JRyMju7t40I"/></div>

In an AND Gate there are two binary values to which outputs 1 only if both binary values are 1.&nbsp;

The __NOT Gate__ is represented below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGC25beH1I6gw/article-inline_image-shrink_1000_1488/0/1535712373734?e=1614211200&amp;v=beta&amp;t=Qc9q3hsPvuUUcKTvDEqY4-XpUAt0RRLzNhEEte-wR9E"/></div>

In a NOT Gate it simply takes a single binary value and negates it.

The __OR Gate__ is represented below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGehjgP7eKqzQ/article-inline_image-shrink_1000_1488/0/1535712396805?e=1614211200&amp;v=beta&amp;t=3Y2cOwDJFQAUyt3znmfX-1_Kl14yrCmzlRBBwm-p0RE"/></div>

In an OR Gate only one of the inputs has to be 1 in order to output a 1.

The __XOR Gate&nbsp;__ is represented below.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHu56HGdZkoIw/article-inline_image-shrink_1000_1488/0/1535712436598?e=1614211200&amp;v=beta&amp;t=uusMriZ0MOruIC7sUA3itLH1TQ9Ifl-wdn0NGhs4RwA"/></div>

In an XOR Gate if both inputs are either 0 or 1 the output is 0.

"The Why..." Ok so why am I going over this? What does this have to do with understanding Assembly or Reverse Engineering? Well... At the very CORE of all processors are these simple logic gates that when combined together form complex instructions. I could spend literally years showing you this in practice however I will leave that for another to pick up the charge. What is important is that you get a basic understanding of what is going on here when we ultimately see instructions such as AND, OR, XOR, etc when we code in Assembly and more importantly when we Reverse Engineer.

Stay tuned! We will be building our own very SIMPLE Operating System shortly!