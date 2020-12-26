# Part 7 - Word Lengths

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The x64 architecture is a backwards-compatible extension of the x86 platform. It provides a legacy 32-bit mode, which is identical to x86, and a new 64-bit mode.&nbsp;You can review my legacy x86 tutorial if you would like to get more information right here on LinkedIn.

The term "x64" includes both AMD 64 and Intel64. The instruction sets are similar.

x64 extends x86's 8 general-purpose registers to be 64-bit, and adds 8 new 64-bit registers. The 64-bit registers have names beginning with "__r__", so for example the 64-bit extension of __eax__ is called __rax__. The new registers are named __r8__ through __r15__.

The lower 32 bits, 16 bits, and 8 bits of each register are directly addressable in operands. This includes registers, like __esi__, whose lower 8 bits were not previously addressable. The following table specifies the assembly-language names for the lower portions of 64-bit registers.

The table below breaks out each bytes distinction.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4D12AQHFdX_EmtcB1Q/article-inline_image-shrink_1500_2232/0/1538735142722?e=1614211200&amp;v=beta&amp;t=Sy_VAzyAPcfSGlvo7jOz_M9oB-pbZIYGUPTuKfs5w6E"/></div>

Operations that output to a 32-bit subregister are automatically zero-extended to the entire 64-bit register. Operations that output to 8-bit or 16-bit subregisters are _not_ zero-extended (this is compatible x86 behavior).

The high 8 bits of __ax__, __bx__, __cx__, and __dx__ are still addressable as __ah__, __bh__, __ch__, __dh__, but cannot be used with all types of operands.

The instruction pointer, __eip__, and __flags__ register have been extended to 64 bits (__rip__ and __rflags__, respectively) as well.

The x64 processor also provides several sets of floating-point registers:

*   Eight 80-bit x87 registers.
*   Eight 64-bit MMX registers. (These overlap with the x87 registers.)
*   The original set of eight 128-bit SSE registers is increased to sixteen.

Next week we will dive into calling conventions! Stay tuned!