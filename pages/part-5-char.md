## Part 5 - char

Today we will begin our coverage of the C data types. We will start with char. A char is the smallest addressable unit of the machine that can contain basic character set. It is an integer type and can be either can be either signed or unsigned.

Let's make a new dir __0x03\_char__ and add our __CMakeLists.txt__ file in it.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x03_char
&nbsp; 0x03_char.c
)

pico_enable_stdio_usb(0x03_char 1)

pico_add_extra_outputs(0x03_char)

target_link_libraries(0x03_char pico_stdlib)
</pre>

Next we need to copy the&nbsp;__pico\_sdk\_import.cmake__&nbsp;file from the external folder in the&nbsp;__pico-sdk__&nbsp;installation to the&nbsp;__0x03\_char__&nbsp;project folder.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Let's create our C file __0x03\_char.c__ and roll...

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; char x = 'x';
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; &nbsp; printf("%c\n", x);

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; return 0;
}
</pre>

Finally we are ready to build.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Then simply copy the&nbsp;__.uf2__&nbsp;file to the drive.

<pre spellcheck="false">cp 0x03_char.uf2 /Volumes/RPI-RP2
</pre>

Then we need to locate the USB drive so you can do the following.

<pre spellcheck="false">ls /dev/tty.
</pre>

Press tab to find the drive and then in my case I will use&nbsp;__screen__&nbsp;to connect.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

You should see a an "x" being printed every second.

<pre spellcheck="false">x
x
x
x
x
x
</pre>

Next lesson we will debug char.