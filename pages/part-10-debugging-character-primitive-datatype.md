<h1>Part 10 - Debugging Character Primitive Datatype</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking_c-_arm64</p><p>Today we hack the char from the last lesson.</p><p>Let's fire up radare2 in write mode.</p><pre spellcheck="false">radare2 -w ./0x03_asm64_char_primitive_datatype
</pre><p>Let's auto analyze.</p><pre spellcheck="false">aaa
</pre><p>Seek to main.</p><pre spellcheck="false">s main
</pre><p>View disassembly.</p><pre spellcheck="false">v
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEtmWlcbps5Xg/article-inline_image-shrink_1500_2232/0/1608839510539?e=1614211200&amp;v=beta&amp;t=6F6vepS7IPvLWC2qFOoHNO77Nhe9HMoVQZon5mmvts4"/></div><p>You can right click and <strong>Open image in new tab </strong>to get an expanded view.</p><p>Let's get back to the terminal view.</p><pre spellcheck="false">q
</pre><p>All we have to do is write assembly to 0x000009ec and specify a new char of our choosing.</p><pre spellcheck="false">[0x000009e4]&gt; wa movz w0, 0x66 @ 0x000009ec
Written 4 byte(s) (movz w0, 0x66) = wx c00c8052
[0x000009e4]&gt;
</pre><p>Let's quit and run the new binary from the terminal.</p><pre spellcheck="false">[0x000009e4]&gt; q
kali@kali:~/Documents/0x03_asm64_char_primitive_datatype$ ./0x03_asm64_char_primitive_datatype
f
</pre><pre spellcheck="false"></pre><p>As you can see we successfully and permanently hacked the binary!  It is very trivial but when you take the last series of lessons together with each new successive lesson you build a real skill-set!</p><p>In our next lesson we will work with the boolean primitive datatype.</p><p><br/></p>