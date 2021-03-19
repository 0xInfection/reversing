## Part 1 - The Why, The How...

It is 2021 and here we are once again covering a new Reverse Engineer course. This course will focus on the C programming language to which we will statically reverse the compiled ARM 32 elf binary utilizing the Radare2 debugger on a Raspberry Pi Pico microcontroller.

What are microcontrollers? We can find them in vehicles, robots, office machines, medical devices, mobile radio transceivers, vending machines and home appliances, among other devices. They are targeted machines designed to control small features of a larger component, without a complex front-end operating system.

We will be writing very basic C programs and then reverse them one at a time in ARM 32 Assembly.

I am going to assume you are working with an Ubuntu Linux distro...

You will first need a Raspberry Pi Pico.

You will need the Radare2 repo.

<pre spellcheck="false">git clone https://github.com/radareorg/radare2.git
cd radare2
cd radare2&nbsp;sys/install.sh
</pre>

You NEED to build from source! The versions that are packaged in Ubuntu and Kali Linux are older and do not have the features we require for our level of reversing.

You will need VIM.

<pre spellcheck="false">sudo apt install vim
</pre>

You will need to update .vimrc file.

<pre spellcheck="false">vim ~/.vimrc
</pre>

Then...

<pre spellcheck="false">set number
set tabstop=2
set noexpandtab
%retab!
syntax on
set syntax=c&nbsp;&nbsp;
</pre>

You will need the Raspberry Pi Pico repo.

<pre spellcheck="false">mkdir pico
cd pico
git clone -b master https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init
cd ..
git clone -b master https://github.com/raspberrypi/pico-examples.git
sudo apt update
sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential&nbsp;
</pre>

Let's build the blink program.

<pre spellcheck="false">cd pico-examples
mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
cd blink
make
</pre>

Copy the __blink.uf2 __file to your Pico.

Congrats you got a blinking C program!

In our next lesson we will create a simple, "Hello, World" program.