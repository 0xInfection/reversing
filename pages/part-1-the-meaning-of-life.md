# Part 1 - The Meaning Of Life

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to set up our development environment. We will need the following:

<pre spellcheck="false">Raspberry Pi 4
64GB MicroSD Card
Micro SD Card Reader/Writer
Download 64-bit Kali Linux ARM Image
Download balenaEtcher
Flash Kali Linux ARM Image
Git Clone &amp; Build Radare2 Software
VIM or Nano Text Editor Software
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1606060809296.jpg"/></div>

<iframe allowfullscreen="true" class="center lazy-load" data-delayed-url="https://www.linkedin.com/embeds/publishingEmbed.html?articleId=7727169611615228100" frameborder="0" height="294" src="about:blank" title="Raspberry Pi 4 Model B - 2 GB RAM" width="744"></iframe>

<iframe allowfullscreen="true" class="center lazy-load" data-delayed-url="https://www.linkedin.com/embeds/publishingEmbed.html?articleId=8531784840398647030" frameborder="0" height="124" src="about:blank" title="Kingston Canvas Go! Plus 64GB MicroSD Card with Adapter" width="744"></iframe>

<iframe allowfullscreen="true" class="center lazy-load" data-delayed-url="https://www.linkedin.com/embeds/publishingEmbed.html?articleId=7824989292602458319" frameborder="0" height="326" src="about:blank" title="Iogear GFR204SD SD/MicroSD/MMC Card Reader and Writer - Walmart.com" width="744"></iframe>

<a href="https://images.kali.org/arm-images/kali-linux-2020.4-rpi4-nexmon-64.img.xz" rel="nofollow noopener" target="_blank">__Kali Linux RaspberryPi 2 (v1.2), 3 and 4 (64-Bit) (img.xz)__</a>__ \[__https://www.offensive-security.com/kali-linux-arm-images/\]

<iframe allowfullscreen="true" class="center lazy-load" data-delayed-url="https://www.linkedin.com/embeds/publishingEmbed.html?articleId=7382995876954764581" frameborder="0" height="294" src="about:blank" title="balena - The complete IoT fleet management platform" width="744"></iframe>

<iframe allowfullscreen="true" class="center lazy-load" data-delayed-url="https://www.linkedin.com/embeds/publishingEmbed.html?articleId=7082048844677902563" frameborder="0" height="419" src="about:blank" title="Load Kali Linux on a Raspberry Pi 4 Model B for a Mini Hacking Computer [Tutorial]" width="744"></iframe>

After obtaining all the necessary devices and software please watch the video on how to set up your environment as Null Byte did an amazing job with a step-by-step tutorial which will get you set-up in minutes.

The next step is to git clone and build the Radare2 software as this will we want the latest version as the standard version built into Kali will not be sufficient for our needs.

<iframe allowfullscreen="true" class="center lazy-load" data-delayed-url="https://www.linkedin.com/embeds/publishingEmbed.html?articleId=8901357596711809999" frameborder="0" height="274" src="about:blank" title="radareorg/radare2" width="744"></iframe>

<pre spellcheck="false">cd Documents
git clone https://github.com/radareorg/radare2.git
sys/install.sh
</pre>

Finally we will be using a text editor to build our code. Kali has both the VIM and Nano text editors built-in. We will be using VIM but you are free to use whatever one you are comfortable with.

In our next lesson we will write our first C++ program which will be "Hello World!".