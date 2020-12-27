## Part 19 - Why Learn Assembly

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Why learn Assembly Language? Java is the most in-demand programming language and will get me a job immediately so why in the hell would I ever waste my damn time learning this archaic Assembly Language crap?

So many people ask me this question and it is true, Java is HOT and in the greatest demand and there is nothing wrong with learning Java however the threats that face society more than anything in this world, above everything else, is the Cyber Security threat. With that said, Java offers a great career path and I would encourage you to learn it however Java is not the only game in town.

Most malware is written in higher-level languages however most malware authors do not give the attackers their source code so they can properly deal with their crafted attack.

The hackers use a multitude of high-level languages and the demand for new professional Malware Analyst Reverse Engineers continue to grow daily.

When we examine malware, more than not we get only a compiled binary. The only thing we can do with a compiled binary is to break it down, instruction-by-instruction, in Assembly Language as EVERYTHING ultimately goes down to Assembly Language.

When someone says Assembly Language is a dinosaur I say to those people, lets have that conversation when your entire network is brought to its knees and you can’t login to a single terminal or manipulate a single machine on your network. Lets talk about how useless Assembly Language is at that time.

Understanding Assembly Language allows one to open a debugger on an a running process. Each running program has a PID to which is a numerical value which designates a running program. If we open a running process or any bit of malware with a professional or open-source tool like GDB, we can see EXACTLY what is going on and then grab the EIP instruction pointer to go where we need it to go to have COMPLETE control over program flow.

Most malware is written, as I have stated, in a middle-level language and once compiled it can be read by the hardware or OS as it is not human-readable. In order for professional Cyber Security Engineers to understand this, they must learn to read, write and properly debug Assembly.

Assembly Language is low-level and has many more instructions than you would see in a higher-level application.

The prior 18 lessons in this tutorial series gave you the basics of x86 hardware. As I have stated in prior tutorials, we will focus on 32-bit Assembly debugging as most malware is going to try to affect as many systems as possible and although there is 64-bit malware, 32-bit malware is significantly more destructive and dangerous and will be the focus of this series.

I look forward to seeing you all next week when we learn the basics of instruction code handling.