<h1>Part 4 - Debugging "Hello World"</h1><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking_c-_arm64</p><p>In the last lesson we spent a good deal of time really understanding what is going on inside our binary.  This laid the groundwork for an easy hack.</p><p>Let's fire up radare2 in write mode.</p><pre spellcheck="false">radare2 -w ./0x01_asm_64_helloworld
</pre><p>Let's auto analyze.</p><pre spellcheck="false">aaa
</pre><p>Seek to main.</p><pre spellcheck="false">s main
</pre><p>View disassembly.</p><pre spellcheck="false">v
</pre><div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQF_AB5hVPpF-g/article-inline_image-shrink_1500_2232/0/1606475269047?e=1614211200&amp;v=beta&amp;t=lNqLA2rqeTf2PQlaUw4d9ABGKMz6PG-lddmClxoAP_o"/></div><p>You can right click and <strong>Open image in new tab </strong>to get an expanded view.</p><p>We see the memory addresses as they are on disk as we are not running the binary as we discussed in the last lesson.</p><p>We see that at <strong>0xb48</strong> we very easily find our string.</p><p>Let's get back to the terminal view.</p><pre spellcheck="false">q
</pre><p>Let's verify the string.</p><pre spellcheck="false">[0x000009e4]&gt; ps @0xb48
Hello World!
[0x000009e4]&gt;

</pre><p>Let's hack the string.</p><pre spellcheck="false">[0x000009e4]&gt; w Hacked World @0xb48
</pre><p>Let's verify the hack.</p><pre spellcheck="false">[0x000009e4]&gt; ps @0xb48
Hacked World
[0x000009e4]&gt;
</pre><p>Let's quit radare2.</p><pre spellcheck="false">q
</pre><p>Now let's run our binary again!</p><pre spellcheck="false">./0x01_asm_64_helloworld
Hacked World
</pre><p>We see that we very easily hacked the binary.  These lessons will help you understand how an attacker creates a workflow so you can learn how to anticipate and better reverse engineer.</p><p>In our next lesson we will work with simple I/O.</p>