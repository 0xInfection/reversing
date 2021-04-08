## Part 2 - Hello World

Today we are going to cover the basic setup for creating our own projects on the Raspberry Pi Pico.

Inside of our __pico__ folder lets create a __0x02\_pico\_hello\_world__ folder alongside of the __pico-sdk__ and __pico-example__ folders.

<pre spellcheck="false">mkdir 0x02_pico_hello_world
cd 0x02_pico_hello_world
</pre>

Let's create our vim __0x02\_hello\_world.c__ file.

<pre spellcheck="false">vim 0x02_hello_world.c
</pre>

Let's add the following.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{	
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp;   printf("Hello world!\n");

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
    
  return 0;
}
</pre>

We first handle the logic to init all standard input and output.

<pre spellcheck="false">&nbsp; &nbsp; stdio_init_all();
</pre>

Finally we print _"Hello world!"_ every 1 second to the standard output in an infinite loop.

<pre spellcheck="false">&nbsp; &nbsp; while(1)&nbsp;
&nbsp; &nbsp; {
&nbsp; &nbsp;   printf("Hello world!\n");

&nbsp; &nbsp; &nbsp; sleep_ms(1000);
&nbsp; &nbsp; }
</pre>

We then upon success _return 0_ to indicate success as our _main_ function is an int. It is not technically required but good practice.

<pre spellcheck="false">    return 0;
</pre>

Working with __cmake__ significantly helps in the build process for our projects. We first need to make a __CMakeLists.txt__ file.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable(0x02_hello_world
  0x02_hello_world.c
)

pico_enable_stdio_usb(0x02_hello_world 1)

pico_add_extra_outputs(0x02_hello_world)

target_link_libraries(0x02_hello_world pico_stdlib)
</pre>

Next we need to copy the __pico\_sdk\_import.cmake__ file from the external folder in the __pico-sdk__ installation to the __0x02\_hello\_world__ project folder.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Finally we are ready to build.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

This will produce a number of files and the ones we are going to focus on are the __.elf__ file when it comes to debugging and hacking which is the full program output, possibly including debug information and the __.uf2__ file which is the program code and data in a UF2 form that you can drag-and-drop on to the RP2040 board when it is mounted as a USB drive.

I took the time to wire up a reset button on the Pico so that I do not have to keep unplugging in the USB and pressing the BOOTSEL every time I need to re-flash so here is the schematic of such.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616317867358.jpg"/></div>

To flash press the external button and while it is still pressed, press the BOOTSEL on the board, then release the BOOTSEL and finally release the external button.

Then simply copy the __.uf2__ file to the drive.

<pre spellcheck="false">cp 0x02_hello_world.uf2 /Volumes/RPI-RP2
</pre>

Then we need to locate the USB drive so you can do the following.

<pre spellcheck="false">ls /dev/tty.
</pre>

Press tab to find the drive and then in my case I will use __screen__ to connect.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Hooray! You should see, "Hello world!" to the standard output every second.

In our next lesson we will debug the __.elf__ binary in __Radare2__.