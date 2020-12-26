# Part 21 - How To Compile A Program

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Let’s look again at last weeks C program and take a deeper look at how we turn that source code into an executable file.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="imgs/862372891.jpg"/></div>

To compile this program in C, we simply type:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/568927047.jpg"/></div>

This single step will create __exit.o__ which is the binary object file and __exit__ which is the binary executable file.

If we wanted to convert this C source code to Assembly, we need to use the GNU compiler in the below fashion. Lets start by running the below command in the terminal:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/115786978.jpg"/></div>

Let’s begin with the -S switch.&nbsp;The -S switch will create comparable AT&amp;T Syntax Assembly source code.&nbsp;The -m32 will create a 32-bit executable and the -O0 will tell the compiler how much optimization to use when compiling the binary.&nbsp;That is the capital O and the numeric 0.&nbsp;Numeric 0 in that case means no optimization which means it is at the most human readable instruction set.&nbsp;If you were to substitute a 1, 2 or 3 the amount of optimization increases as the values go up.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/680912813.jpg"/></div>

This step above creates exit.s which is the equivalent Assembly Language source code as we mentioned above.

We then need to compile the Assembly source code into a binary object file which will generate a __exit.o__ file.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/438826375.jpg"/></div>

Finally we need to use a linker to create the actual binary executable code from the binary object file which will create an executable called exit.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/249502499.jpg"/></div>

Last week when we examined the executable file exit in a program called objdump, and examined the main area we saw the following below except this time we will use AT&amp;T Assembly Language Syntax:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/878108058.jpg"/></div>

This command above will create the following output below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/893328572.jpg"/></div>

Lets examine the code in the debugger.&nbsp;Let’s start GDB which is the GNU debugger and first list the source code by typing l, then set a breakpoint on main and run the program.&nbsp;Finally we will disassemble and review the output below:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/36797574.jpg"/></div>

In each of the three above examinations, you will essentially see the same set of instructions which we will take a deeper look as to what is exactly going on in future tutorials.

Throughout this tutorial series thus far we have been looking at Intel Syntax Assembly Language. We are going to turn our focus to AT&amp;T Syntax as I have stated above as this is the natural syntax utilized in Linux with the GNU Assembler and GNU Debugger.

The biggest different you will see is that in AT&amp;T Syntax, the source and destinations are reversed.

AT&amp;T Syntax : __movl %esp, %ebp__ \[This means move esp into ebp.\]

Intel Syntax : __mov esp, ebp__ \[This means move ebp into esp.\]

You will also see some additional variances as AT&amp;T uses additional variances which we will cover in a later tutorial.

If we wanted to create a pure Assembly Code program which does the same thing above we would type:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/49995151.jpg"/></div>

To compile this we would use the GAS Assembler and Linker:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="imgs/1024354826.jpg"/></div>

To run any executable in Linux you type ./ and the name of the binary executable. In this case we type ./exit and press return. When we do so, nothing happens. That is good as all we did was create a program that exited to the OS.

I look forward to seeing you all next week when we dive into more assembly&nbsp;code!