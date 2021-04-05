## Part 8 - int

Today we are going to work with the int data type which are nothing more than whole numbers. They can be signed or unsigned as well.

Let's work with a simple example. __0x04\_int.c__ as follows.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; int x = 40;&nbsp;

&nbsp; &nbsp; printf("%d\n", x);&nbsp;
&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Here we simply have our standard IO function followed by our infinite loop. We simply assign _40_ to the int data type _x_ and print it using the _%d_ format modifier and sleep for _1_ second.

Let's make a new dir&nbsp;__0x04\_int__&nbsp;and add our&nbsp;__CMakeLists.txt__&nbsp;file in it.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x04_int
&nbsp; 0x04_int.c
)

pico_enable_stdio_usb(0x04_int 1)

pico_add_extra_outputs(0x04_int)

target_link_libraries(0x04_int pico_stdlib)
</pre>

Next we need to copy the&nbsp;__pico\_sdk\_import.cmake__&nbsp;file from the external folder in the&nbsp;__pico-sdk__&nbsp;installation to the&nbsp;__0x04\_int__&nbsp;project folder.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Finally we are ready to build.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Then simply copy the&nbsp;__.uf2__&nbsp;file to the drive.

<pre spellcheck="false">cp 0x04_int.uf2 /Volumes/RPI-RP2
</pre>

Then we need to locate the USB drive so you can do the following.

<pre spellcheck="false">ls /dev/tty.
</pre>

Press tab to find the drive and then in my case I will use&nbsp;__screen__&nbsp;to connect.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

You should see a an _40_ being printed every second.

<pre spellcheck="false">40
40
40
40
40
40
40
40
40
40
40
40
</pre>

In our next lesson we will debug.