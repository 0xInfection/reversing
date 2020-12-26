# Part 16 - ROL Instruction

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The ROR command stands for rotate right.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH5hHizs-GqYA/article-inline_image-shrink_1000_1488/0/1544181149655?e=1614211200&amp;v=beta&amp;t=H8oyHs_Kybqzps5MYmlaMWOm_imPaoXQiCuhQir4phk"/></div>

In our simple x64 example on an Ubuntu Linux machine above we see we&nbsp;mov 1&nbsp;into&nbsp;al&nbsp;and rotate right by 1 bit.

The binary representation is __00000001b__.&nbsp;If we __ROR__ 1 bit the value simply becomes __10000000b__ as demonstrated below.

We first compile and link by:

__nasm -f elf64 -o test.o test.asm__

__ld -o test test.o__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHiiu0Ea3MRQw/article-inline_image-shrink_1000_1488/0/1544181229818?e=1614211200&amp;v=beta&amp;t=fJXhy_12jFjUfcGlizmhSq4yZStXOpjOnPdL-uBmhxg"/></div>

We can see here in the debugger that&nbsp;al&nbsp;starts with&nbsp;1&nbsp;and when we rotate right it goes to&nbsp;__10000000b__.

Next week we will dive into Boot Sector Basics! Stay tuned!