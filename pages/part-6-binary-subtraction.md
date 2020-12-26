# Part 6 - Binary Subtraction

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Before we dive into the architecture lets talk about how we define various bits and how they are structured within the processor.

In both x64 and x86, we define a byte as 8 bits.&nbsp;We define a word as 16 bits.&nbsp;We define a double word as 32 bits and a quadword as 64 bits.&nbsp;Finally we define a double quadword as 128 bits.&nbsp;

Intel processors store bytes as what we refer to as "little endian," meaning lower significant bytes are stored in lower memory addresses.&nbsp;Lets give an example of a simple 16-bit or 2 byte value.&nbsp;On disk - 0xAABB.&nbsp;When it goes into memory it is stored as 0xBBAA as I hope this provides a good visual as this concept can be quite confusing.

Keep in mind, 8 bits make up a byte.&nbsp;4 bits are also called a nibble which are equivalent to one hex digit.

Next week we will dive into general architecture! Stay tuned!