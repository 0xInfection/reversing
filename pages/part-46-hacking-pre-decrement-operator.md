<h1>Part 46 – Hacking Pre-Decrement Operator</h1><p>This week we will address the post-decrement operator. Let's examine our code.</p>
<pre spellcheck="false"><span class="hljs-meta">#include &lt;iostream&gt;</span>

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span> </span>{
    <span class="hljs-keyword">int</span> myNumber = <span class="hljs-number">16</span>;
    <span class="hljs-keyword">int</span> myNewNumber = myNumber--;

    <span class="hljs-built_in">std</span>::<span class="hljs-built_in">cout</span> &lt;&lt; myNewNumber &lt;&lt; <span class="hljs-built_in">std</span>::<span class="hljs-built_in">endl</span>;
    <span class="hljs-built_in">std</span>::<span class="hljs-built_in">cout</span> &lt;&lt; myNumber &lt;&lt; <span class="hljs-built_in">std</span>::<span class="hljs-built_in">endl</span>;

    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
}
</pre>
<div class="slate-resizable-image-embed slate-image-embed__resize-full-width">
<img src="https://media-exp1.licdn.com/dms/image/C4D12AQHIN2-UGuEsiQ/article-inline_image-shrink_1000_1488/0/1531481191370?e=1614211200&amp;v=beta&amp;t=wpwtAxktPX828SRlJ73i93oy4yXNzVWo5i8r_4l4eP0"/>
</div>
<p> As we compile we see <strong>16</strong> and <strong>15</strong> printed out respectively.</p>
<div class="slate-resizable-image-embed slate-image-embed__resize-full-width">
<img src="https://media-exp1.licdn.com/dms/image/C4D12AQG-R4r3ltVZQA/article-inline_image-shrink_1000_1488/0/1531481259797?e=1614211200&amp;v=beta&amp;t=_xQtXQBg0nKFc2QQutmzn1j3RNrHIsisgDQmdqTW794"/>
</div>
<p>We see that in this scenario <strong>myNewNumber</strong> does get decremented as <strong>myNumber-- </strong>takes the value of 16 and reduces it to 15.</p>
<p>Next week we will dive into the Debugging Post-Decrement Operator.</p>
