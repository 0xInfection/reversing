## Part 26 - Boot Sector Basics \[Part 9\]

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Before we dive into x64 Assembly I want to talk very briefly about what we refer to as long mode.

When the computer boots it needs to enable what we refer to as the A-20 line. In early architectures, processors had 20 address lines which were A-0 to A-19 to which could access 2 to the power of 20 bytes of information. The A-20 line is an external memory reference containing a 16-bit offset address added to a 16-bit segmented number which shifts 4 bits to get the additional access.

This process combined with the Global Descriptor Table allows you to work with your Control Register to to execute a far jump to enter protected mode which is 32-bits.

Long mode which is 64-bit mode which we are all familiar with in our modern architectures extend the address space to access 0xFFFFFFFFFFFFFFFF.

This topic alone can take weeks to explain however I wanted to at a very high level touch base on the fact that the processor needs to bridge to 32-bit mode and then finally to 64-bit through setting the A-20 line, working with the control register and GDT in combination with paging.

I took several months to get to this point so that you have a basic understanding of Assembly as we will start to get into actual 64-bit Assembly in the following tutorials and then our C++ tutorial to which we will reverse engineer each code block into 64-bit Assembly.