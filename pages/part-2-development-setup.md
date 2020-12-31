## Part 2 - Development Setup

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/hacking\_c-\_arm64

Today we are going to set up our development environment. We will need the following:

<pre spellcheck="false">Raspberry Pi 4
64GB MicroSD Card
Micro SD Card Reader/Writer
Download 64-bit Kali Linux ARM Image
Download balenaEtcher
Flash Kali Linux ARM Image
OPTIONAL: Video [Load Kali RPI 4]
How To Install VIM
Git Clone &amp; Build Radare2 Software
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1606060809296.jpg"/></div>

__Raspberry Pi 4__

https://www.adafruit.com/product/4292

__64GB MicroSD Card__

https://www.sparkfun.com/products/16498

__Micro SD Card Reader/Writer__

https://www.walmart.com/ip/Iogear-GFR204SD-SD-MicroSD-MMC-Card-Reader-and-Writer/15522266

__Download 64-bit Kali Linux ARM Image__

Kali Linux RaspberryPi 2 (v1.2), 3 and 4 (64-Bit) (img.xz)__ __

https://www.offensive-security.com/kali-linux-arm-images

__Download balenaEtcher__

https://www.balena.io/etcher

__Flash Kali ARM Image__

__OPTIONAL: Video \[Load Kali RPI 4\]__

<a href="https://youtu.be/Jquf9BDm4iU" rel="nofollow noopener" target="_blank">https://youtu.be/Jquf9BDm4iU</a>

__How To Install VIM__

https://www.simplified.guide/ubuntu/install-vim 

After obtaining all the necessary devices and software please watch the video on how to set up your environment as Null Byte did an amazing job with a step-by-step tutorial which will get you set-up in minutes.

The next step is to git clone and build the Radare2 software as this will we want the latest version as the standard version built into Kali will not be sufficient for our needs.

__Git Clone &amp; Build Radare2 Software__

https://github.com/radareorg/radare2

<pre spellcheck="false">cd Documents
git clone https://github.com/radareorg/radare2.git
sys/install.sh
</pre>

Finally we will be using a text editor to build our code. Kali has both the VIM and Nano text editors built-in. We will be using VIM but you are free to use whatever one you are comfortable with.

In our next lesson we will write our first C++ program which will be "Hello World!".