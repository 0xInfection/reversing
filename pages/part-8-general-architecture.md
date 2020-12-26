# Part 8 - General Architecture

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The x64 processor uses what we refer to as \_\_fastcall.&nbsp;

The&nbsp;\_\_fastcall&nbsp;calling convention specifies that arguments to functions are to be passed in registers, when possible. This calling convention only applies to the x86 architecture.

The first two DWORD or smaller arguments that are found in the argument list from left to right are passed in __ecx__ and __edx__ registers; all other arguments are passed on the stack from right to left.

Called function pops the arguments from the stack.

At sign (@) is prefixed to names; an at sign followed by the number of bytes (in decimal) in the parameter list is suffixed to names.

No case translation performed.

Here is a simple breakdown to illustrate:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGixhqL7odqYA/article-inline_image-shrink_1000_1488/0/1539336219028?e=1614211200&amp;v=beta&amp;t=Xx9UCsDsmCSqL3PWXUzoGKn03AdI4gdv8jiyWNS58Og"/></div>

If you have two parameters you are passing from a function, for example int __x__ and int __y__ and it is a QWORD, __x__ will go into __rcx__ and __y__ will go into__ rdx__.&nbsp;

If you have five parameters you are passing for example int __a__, int __b__, int __c__, int __d__, int __e__ and it is a WORD in length, __a__ will go into __cx__, __b__ into __dx__, __c__ into __r8w__, __d__ into r9w and e into the stack.

  

Next week we will dive into boolean instructions! Stay tuned!