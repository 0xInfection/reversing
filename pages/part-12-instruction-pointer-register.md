# Part 12: Instruction Pointer Register

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The instruction pointer register called the EIP register is simply the most important register you will deal with in any reverse engineering. The EIP keeps track of the next instruction code to execute. EIP points to the next instruction to execute. If you were to alter that pointer to jump to another area in the code you have complete control over that program.

Lets jump ahead and dive into some code. Here is an example of a simple hello world application in C that we will go into more detail much later in our tutorial series. For our purposes today, we will see the raw POWER of assembly language and particularly that of the EIP register and what we can do to completely hack program control.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520174518917.jpg"/></div>

Don’t worry if you do not understand what it does or its functionality. What to take note of here is the fact we have a function called unreachableFunction that is never called by the main function. As you will see if we can control the EIP register we can hack this program to execute that code!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520572373327.jpg"/></div>

We have simply compiled the code to work with the IA32 instruction set and ran it.&nbsp;As you can see there is no call to the __unreachableFunction__ of any kind as it is unreachable under normal conditions as you can see the ‘Hello World!\` printed when executed.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520572374855.jpg"/></div>

We have disassembled the program using the GDB Debugger.&nbsp;We have set a breakpoint on the main function and ran the program.&nbsp;The =&gt; shows where EIP is pointing to when we step to the next instruction.&nbsp;If we follow normal program flow, ‘Hello World! will print to the console and exit.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520191047777.jpg"/></div>

If we run the program again and do an examination of where EIP is pointing to we will see:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520173635003.jpg"/></div>

We can see EIP is pointing to main+17 or the address of 0x680cec83.

Lets examine the __unreachableFunction__ and see where it starts in memory and write down that address.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520572373912.jpg"/></div>

The next step is to set EIP to address 0x0804843b so that we hijack program flow to run the unreachableFunction.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520572373288.jpg"/></div>

Now that we have hacked control of EIP, lets continue and watch how we have hijacked the operation of a running program to our advantage!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520192688705.jpg"/></div>

Tada! We have hacked the program!

So the question in your mind is why did you show me this when I have no idea of what any of this is? It is important to understand that when we are doing a lengthy tutorial such as this we should sometimes look forward to see why we are taking so many steps to learn the basics before we dive in. It is important however to show you that if you stay with the tutorial your hard work will pay off as we will learn how to hijack any running program to make it do whatever we want in addition to proactively breaking down a malicious program so that we can not only disable it but trace it back to a potential IP of where the hack originated.

In our next tutorial we will continue our discussion of the IA-32 Architecture with the Control Registers.