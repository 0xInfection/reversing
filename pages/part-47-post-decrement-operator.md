## Part 47 – Post-Decrement Operator

This week we will address the post-decrement operator. Let's examine our code.

<pre spellcheck="false"><span class="hljs-meta">#include &lt;iostream&gt;</span>

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span> </span>{
&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">int</span> myNumber = <span class="hljs-number">16</span>;
&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">int</span> myNewNumber = myNumber--;

&nbsp;&nbsp; &nbsp;<span class="hljs-built_in">std</span>::<span class="hljs-built_in">cout</span> &lt;&lt; myNewNumber &lt;&lt; <span class="hljs-built_in">std</span>::<span class="hljs-built_in">endl</span>;
    <span class="hljs-built_in">std</span>::<span class="hljs-built_in">cout</span> &lt;&lt; myNumber &lt;&lt; <span class="hljs-built_in">std</span>::<span class="hljs-built_in">endl</span>;

&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width">
<img src="/imgs/1531481191370.jpg"/>
</div>

 As we compile we see __16__ and __15__ printed out respectively.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width">
<img src="/imgs/1531481259797.jpg"/>
</div>

We see that in this scenario __myNewNumber__ does get decremented as __myNumber-- __takes the value of 16 and reduces it to 15.

Next week we will dive into the Debugging Post-Decrement Operator.