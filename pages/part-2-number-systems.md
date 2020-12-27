## Part 2 – Number Systems

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

At the core of the microprocessor are a series of binary numbers which are either +5V (on or 1) or 0V (off or 0). Each 0 or 1 represents a bit of information within the microprocessor. A combination of 8 bits results in a single byte.

Before we dive into binary, lets examine the familiar decimal. If we take the number 2017, we would understand this to be two thousand and seventeen.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520147341286.jpg"/></div>

Let’s take a look at the binary system and the basics of how it operates.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520216778060.jpg"/></div>

If we were to convert a binary number into decimal, we would very simply do the following. Lets take a binary number of 0101 1101 and as you can see it is 93 decimal.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520212802125.jpg"/></div>

Adding the values in the value column gives us 0 + 64 + 0 + 16 + 8 + 4 + 0 + 1 = 93 decimal.

If we were to convert a decimal number into binary, we would check to see if a subtraction is possible relative to the highest order bit and if so, a 1 would be placed into the binary column to which the remainder would be carried into the next row. Let’s consider the example of the decimal value of 120 which is 0111 1000 binary.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520194446121.jpg"/></div>

1)Can 128 fit inside of 120: No, therefore 0.

2)Can 64 fit inside of 120: Yes, therefore 1, then 120 – 64 = 56.

3)Can 32 fit inside of 56: Yes, therefore 1, then 56 – 32 = 24.

4)Can 16 fit inside of 24: Yes, therefore 1, then 24 – 16 = 8.

5)Can 8 fit inside of 8: Yes, therefore 1, then 8 – 8 = 0.

6)Can 4 fit inside of 0: No, therefore 0.

7)Can 2 fit inside of 0: No, therefore 0.

8)Can 1 fit inside of 0: No, therefore 0.

When we want to convert binary to hex we simply work with the following table.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520211831076.jpg"/></div>

Lets convert a binary number such as 0101 1111 to hex. To do this we very simply look at the table and compare each nibble which is a combination of 4 bits. Keep in mind, 8 bits is equal to a byte and 2 nibbles are equal to a byte.

0101 = 5

1111 = F

Therefore 0101 1111 binary = 0x5f hex. The 0x notation denotes hex.

To go from hex to binary it’s very simple as you have to simply do the opposite such as:

0x3a = 0011 1010

3 = 0011

A = 1010

It is important to understand that each hex digit is a nibble in length therefore two hex digits are a byte in length.

To convert from hex to decimal we do the following:

0x5f = 95

5 = 5 x 16^1 = 5 x 16 = 80

F = 15 x 16^0 = 15 x 1 = 15

Therefore we can see that 80 + 15 = 95 which is 0x5f hex.

Finally to convert from decimal to hex. Lets take the number 850 decimal which is 352 hex.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520238915130.jpg"/></div>

We put the numbers together from bottom to the top and we get 352 hex.

“Why the hell would I waste my time learning all this crap when the computer does all this for me!”

If you happen to know any reverse engineers please if you would take a moment and ask them the above question.

The reality is, if you do NOT have a very firm understanding of how all of the above works, you will have a hard time getting a grasp on how the ARM processor registers hold and manipulate data. You will also have a hard time getting a grasp on how the ARM processor deals with a binary overflow and it’s effect on how carry operations work nor will you understand how compare operations work or even the most basic operations of the most simple assembly code.

I am not suggesting you memorize the above, nor am I suggesting that you do a thousand examples of each. All I ask is that you take the time to really understand that literally everything and I mean everything goes down to binary bits in the processor.

Whether you are creating, debugging or hacking an Assembly, Python, Java, C, C++, R, JavaScript, or any other new language application that hits the street, ultimately everything MUST go down to binary 0 and 1 to which represent a +5V or 0V.

We as humans operate on the base 10 decimal system. The processor works on a base 16 (hex) system. The registers we are dealing with in conjunction with Linux are addressed in 32-bit sizes. When we begin discussion of the processor registers, we will learn that each are 32-bits wide (technically the BCM2837 are 64-bit wide however our version of Linux that we are working with is 32-bit therefore we only address 32-bits of each register).

Next week we will dive into binary addition! Stay tuned!