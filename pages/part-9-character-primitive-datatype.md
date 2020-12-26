<h1>Part 9 - Character Primitive Datatype</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking_c-_arm64</p><p>Today we are going to debug our very simple character primitive datatype.</p><p>To begin let's open up our binary in Radare2.</p><pre spellcheck="false">radare2 ./0x03_asm64_char_primitive_datatype
</pre><p>Let's take advantage of Radare2's auto analysis feature.</p><pre spellcheck="false">aaa
</pre><p>The next thing we want to do logically is fire up the program in debug mode so it maps the raw machine code from disk to a running process.</p><pre spellcheck="false">ood
</pre><p>Now that we have a running instance we can seek to the main entry point of the binary.</p><pre spellcheck="false">s main
</pre><p>Let us take an initial examination by doing the following.</p><pre spellcheck="false">v
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEwJmfQwzZC0w/article-inline_image-shrink_1500_2232/0/1608824475984?e=1614211200&amp;v=beta&amp;t=s84yCn_ILyB6H1GODseJ9xgBAD_iBEOV_ByuZQAPDRU"/></div><p>You can right click and <strong>Open image in new tab </strong>to get an expanded view.</p><p>We can see that at <em>0x5576bff9ec</em> we are moving <em>0x63</em> or ascii <em>'c'</em> into the <em>w0</em> register.</p><p>Let's set a breakpoint at <em>0x5576bff9ec</em> and verify the contents.</p><pre spellcheck="false">[0x5576bff9e4]&gt; db 0x5576bff9ec
[0x5576bff9e4]&gt; dc
hit breakpoint at: 0x5576bff9ec
[0x5576bff9ec]&gt; dr w0
0x00000001
[0x5576bff9ec]&gt; ds
[0x5576bff9ec]&gt; dr w0
0x00000063
[0x5576bff9ec]&gt;

</pre><pre spellcheck="false"></pre><p>This is very simple but let's break it down.  We set our breakpoint and continued.  We looked inside the register w0 and saw that the value is 0x01. </p><p>We then stepped once and looked again to see that 0x63 was successfully moved into w0 as now we see it does in fact contain 0x63.</p><p>If we dc again we see it echoed to the stdout as expected.</p><pre spellcheck="false">[0x5576bff9ec]&gt; dc
c
(10845) Process exited with status=0x0
</pre><pre spellcheck="false">[0x7f9727503c]&gt;
</pre><p>In our next lesson we will hack the char to another value of our choice.</p><p><br/></p>