# Part 37 - x64 C &amp; Genesis Of Life

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Ok so what now? Where are we in the world? What is our purpose? What shall I focus on? What shall I learn?

There are over 30 billion devices connected to the Internet today. Nonetheless, the common thread in all basic architecture is the C programming language.

We have established that networking can be described in a very high-level pseudo framework called the OSI Model which has 7 layers.

__P__LEASE __D__O __N__OT __T__HROW __S__AUSAGE __P__IZZA __A__WAY. Ok I am not insane, well, ok I am but this is a good standard agreed upon way to remember the layers in the OSI model which is our Open Systems Interconnection model.

1)__PHYSICAL LAYER__ - Raw electrical layer which read voltages on an ethernet cable or reading the Wi-Fi RF (radio frequencies). Protocols associated: USB, DSL, ISDN, Infrared, etc...

2)__DATA LINK LAYER __- Deals with how a message between notes starts and ends called framing which has some error correction, detection and some flow control. Protocols associated: Ethernet, VLAN, etc...

3)__NETWORK LAYER__ - Transmits packets between nodes in different networks which involves routing. Protocols associated: IPX, NAT, ICMP, ARP, etc...

4)__TRANSPORT LAYER__ - Reliably deliver data between two hosts which must split it up into chunks to send. Protocols associated: NetBIOS, TCP, UDP, etc...

5)__SESSION LAYER__ - Adds checkpoint and resume in addition to term dialogues. Protocols associated: SMB, SOCKS, etc...

6)__PRESENTATION LAYER__ - Where data structure for and presentation for an application are created where we have encoding, serialization and encryption. Protocols associated: TLS, SSL, etc...

7)__APPLICATION LAYER__ - Web browsers and apps that use web interfaces like email, etc. Protocols associated: DHCP, DNS, HTTP, HTTPS, POP3, SMTP, FTP, TELNET, etc...

As we browse a website we start at the PHYSICAL and go to the APP and as it hits the server it is at the APP and goes back down to the PHYSICAL and back through the cycle.

This is an important series of concepts that you must understand in any basic networking. This is NOT a course in networking as we will touch BRIEFLY on these concepts so I would suggest you find a free course on YouTube for networking if you are stuck. I want to get through some basic theory so we can work with C networking apps.