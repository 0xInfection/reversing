## Part 7: Transistors And Memory

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

In our last lesson, we took a very deep dive into the hexadecimal number system. I am going to keep this weeks lesson short so that you can re-read last weeks lesson. I can not emphasize how important it is to understand hexadecimal number conversions in addition to the ability to manually add and subtract them.

In the real world, we have calculators, in the real world we use the Windows operating system, in the real world professional reverse engineers use GUI debuggers like IDA Pro and others.

The question is, why am I not jumping right into the core of what real reverse engineers do? The answer is simple, one must have a deep respect and understanding of the machine in order to become great. We will never change the world without fully understanding it first. Patience and perseverance win the day.

I focus on on Linux and console-based programming because most professional servers utilize Linux and therefore is the greatest threat of malware. Understanding Linux Assembly allows you to very easily grasp the library-choking portable executable format of Windows Assembly in a much deeper way.

As I step off the soap box, lets get back to the basics of computers so here we go!

When we ask ourselves what is a computer one must go down to as about as basic as one can get.

Electronic computers are simply made out of transistor switches. Transistors are microscopic crystals of silicon that use electrical properties of silicon to act as switches. Modern computers have what are referred to as field-effect transistors.

Let's use an example of 3 pins. When an electrical voltage is applied to pin 1, current then flows between pins 2 and 3. When the voltage is removed from the first pin, current stops flowing between pins 2 and 3.

When we zoom out a bit we see that there are also diodes and capacitors when taken together with the transistor switches we now have a memory cell. A memory cell keeps a minimum current flow to which when you put a small voltage on its input pin and a similar voltage on its select pin, a voltage will appear and remain on its output pin. The output voltage remains in its set state until the voltage is removed from the input pin in conjunction with the select pin.

Why is this important you ask. Very simply, the presence of voltage indicates a binary 1 and the absence of voltage indicates a binary 0 therefore the memory cell holds one binary digit or bit which is either 1 or 0 meaning on or off.

In our next lesson we will discuss bytes and words.