## Part 15: Stack

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Functions are the most fundamental feature in software development. A function allows you to organize code in a logical way to execute a specified task. It is not critical that you understand how functions work at this stage it is only important that you understand that when we start learning to develop, we want to minimize duplication by using functions that can be called multiple times rather than duplicate code taking up excessive memory.

When a program starts to execute a certain contiguous section of memory is set aside for the program called the stack.

The stack pointer is a register that contains the top of the stack. The stack pointer contains the smallest address, lets say for example 0x00001000, such that any address smaller than 0x00001000 is considered garbage and any address greater than 0x00001000 is considered valid.

The above address is random and is not an absolute where you will find the stack pointer from program to program as it will vary. Lets look at what the stack looks like from an abstract perspective:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520235829712.jpg"/></div>

The above diagram is what I want you to keep clear in your mind as that is what is actually happening in memory. The next series of diagrams will show the opposite of what is shown above.

You will see the stack growing upward in the below diagrams however in reality it is growing downward from higher memory to lower memory.

In the addMe example below, the stack pointer (ESP), when examined in memory on a breakpoint on the main function, lists 0xffffd050. When the program calls the addMe function from main, ESP is now 0xffffd030 which is LOWER in memory. Therefore the stack grows DOWNWARD despite the diagram showing it pointing upward. Just keep in mind when the arrows below are pointing upward they are actually pointing to lower memory addresses.

The stack bottom is the largest valid address of the stack and is located in the larger address area or top of the memory model. This can be confusing as the stack bottom is higher in memory. The stack grows downward in memory and it is critical that you understand that now as we go forward.

The stack limit is the smallest valid address of the stack. If the stack pointer gets smaller than this, there is a stack overflow which can corrupt a program to allow an attacker to take control of a system. Malware attempts to take advantage of stack overflows. As of recent, there are protections build into modern OS that attempt to prevent this from happening.

There are two operations on the stack which are push and pop. You can push one or more registers by setting the stack pointer to a smaller value. This is usually done by subtracting four times the number of registers to be pushed onto the stack and copying the registers to the stack.

You can pop one or more registers by copying the data from the stack to the registers, then to add a value to the stack pointer. This is usually done by adding four times the number of registers to be popped on the stack.

Let us look at how the stack is used to implement functions. For each function call there is a section of the stack reserved for the function. This is called the stack frame.

Let’s look at the C program we created in tutorial 12 and examine what the main function looks like:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520622740099.jpg"/></div>

We see two functions here. The first one is the unreachableFunction to which will never execute under normal circumstances and we also see the main function that will always be the first function to be called onto the stack.

When we run this program, the stack will look like this:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520622738609.jpg"/></div>

We can see the stack frame for int main(void) above.&nbsp;It is also referred to as the activation record.&nbsp;A stack frame exists whenever a function has started but yet to complete.&nbsp;For example, inside of the body of the int main(void) there is a call to int addMe(int a, int b) which takes two arguments a and b.&nbsp;There needs to be assembly language code in int main(void) to push the arguments for int addMe(int a, int b) onto the stack.&nbsp;Lets examine some code.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520231875596.jpg"/></div>

When we compile and run this program we will see the value of 5 to be print out like this:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520622737902.jpg"/></div>

Very simply, int main(void) calls int addMe(int a, int b) first and will get put on the stack like this:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144504701.jpg"/></div>

You can see that by placing the arguments on the stack, the stack frame for __int main(void)__ has increased in size. We also reserved space for the return value which is computed by __int addMe(int a, int b)__ and when the function returns, the return value in __int main(void)__ gets restored and execution continues in __int main(void)__ until it finishes.

Once we get the instructions for __int addMe(int a, int b)__, the function may need local variables so the function needs to push some space on the stack which would look like:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520622739277.jpg"/></div>

__int addMe(int a, int b)__ can access the arguments passed to it from __int main(void)__ because the code in __int main(void)__ places the arguments just as __int addMe(int a, int b)__ expects it.&nbsp;

FP is the frame pointer and points to the location where the stack pointer was just before __int addMe(int a, int b)__ moved the stack pointer or SP for int __addMe(int a, int b)__’s own local variables.

The use of a frame pointer is essential when a function is likely to move the stack pointer several times throughout the course of running the function. The idea is to keep the frame pointer fixed for the duration of __int addMe(int a, int b)__’s stack frame. In the meantime, the stack pointer can change values.

We can use the frame pointer to compute the locations in memory for both arguments as well as local variables. Since it does not move, the computations for those locations should be some fixed offset from the frame pointer.

Once it is time to exit __int addMe(int a, int b)__, the stack pointer is set to where the frame pointer is which pops off the __int addMe(int a, int b)__ stack frame.

In sum, the stack is a special region of memory that stores temporary variables created by each function including main. The stack is a LIFO which is last in, first out data structure which is managed and optimized by the CPU closely. Every time a function declares a new variable it is pushed onto the stack. Every time a function exists, all of the variables pushed onto the stack by that function are freed or deleted. Once a stack variable is freed, that region of memory becomes available for other stack variables.

The advantage of the stack to store variables is that memory is managed for you. You do not have to allocate memory manually or free it manually. The CPU manages and organizes stack memory very efficiently and is very fast.

It is critical that you understand that when a function exits, all of its variables are popped off the stack and lost forever. The stack variables are local. The stack grows and shrinks as functions push and pop local variables.

I can see your head spinning around and around. Keep in mind, these topics are complicated and will continue to develop in future tutorials. We have been dealing with a lot of confusing topics such as registers, memory and now the stack and it can be overwhelming. If you ever have questions, please comment below and I will help you to better understand this framework.

In our next tutorial we will discuss the heap.