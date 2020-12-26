# Part 18 - Boot Sector Basics \[Part 1\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

We are at the stage where we are going to start integrating real-world code. If you do not have an active linux desktop I would suggest you get Virtualbox and Ubuntu on either your Windows or Mac. I have a prior tutorial that will walk you through this process below. For some reason I am not able to embed the link so please just copy and paste it into your browser.

__https://www.linkedin.com/pulse/assembly-language-basic-malware-reverse-engineering-kevin-m-thomas-16/ __

You will additionally need a text editor for the terminal. I use VIM. You will find a link to set that up as well below.

__https://www.linkedin.com/pulse/assembly-language-basic-malware-reverse-engineering-kevin-m-thomas-17/__

In addition you will have to install nasm so you may simply type:

__sudo apt-get install nasm__

NASM is the assembler we will use and we will focus on the intel syntax. First go into the terminal and fire up Vim and type the following:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQH9sJkD2-acHw/article-inline_image-shrink_1000_1488/0/1545386856569?e=1614211200&amp;v=beta&amp;t=AOXUfVmqXdxzGQLZ8eNGijw7VeRQYfCeI1KvUB6Szuk"/></div>

Remember to type 'i' to insert and then 'esc' and 'wq' to go into command mode and save your file.

The above line simply sets an infinite loop and does nothing more. The __loop __label is created to which we simply __jmp__ back to itself. This code in itself will compile however it will not run in an OS as it does not trigger what we refer to as the magic number to which BIOS looks to understand this is the end of your boot sector. We will cover more on that in future lectures.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE2VHxoXB-_Nw/article-inline_image-shrink_1000_1488/0/1545387039903?e=1614211200&amp;v=beta&amp;t=vZqwxXb4Wx4GnqVtOHSDkjqMPN_dmMybO4zUl8ly95Q"/></div>

We type the above command assuming you saved your file in vim as __bootsector.asm__. This will create a binary file to which we will examine the contents within a hex editor. A hex editor is an application that examines each byte of data that is compiled into a file. We will see that our assembly instructions above will ultimately get translated down to their raw opcode values. The processor only understands raw opcodes which are simply operation codes. Below is a link to a table identifying the opcodes. I saved you the effort of referencing the intel dataset as it is literally thousands of pages and several volumes:

__http://ref.x86asm.net/coder64.html__

Let's use a hex editor like ghex and open up our bin file.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHUwVitDEnmMg/article-inline_image-shrink_1000_1488/0/1545387311381?e=1614211200&amp;v=beta&amp;t=FY8JDsbQXQv4yotiM0vvKDXKHPW2r6BfWIdTKea_4Yw"/></div>

We see __EB FE__ which are hex bytes and each letter is a nibble (a nibble is 4 bits or half a byte). Both __EB FE__ make up two full bytes. Keep in mind the processor reads from disk in reverse byte order such that __FE __gets read first and then __EB__. This process is called little endian and is how the x64 processor works.

If you review the table to which I provided the link you will see that __FE __represents an __INC__ or increment by one. This is our loop value.

Next you will find that __EB__ stands for __JMP__ which is our jump instruction above.

This is alot of information if you are new to assembly. Take it step-by-step and follow along with me in a real linux OS and with each lesson you will get a better understanding of the basics.

Next week we will build upon this lesson by adding some simple data to our binary.