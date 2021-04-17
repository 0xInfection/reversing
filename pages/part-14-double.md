## Part 14 - double

Today we are going to handle the double data type. As we discussed, in the Pico there is no co-processor to handle floating-point numbers as this is handled through a series of functionality through software in the API. This is the same with double-precision.

Let's work with a simple example.&nbsp;__0x06\_double.c__&nbsp;as follows.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; double x = 40.5;

&nbsp; &nbsp; printf("%f\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Very simply we assign a float of&nbsp;_40.5_&nbsp;into&nbsp;_x_&nbsp;and print it with the&nbsp;_%f&nbsp;_format modifier and then sleep for&nbsp;_1_&nbsp;second.

Let's make a new dir&nbsp;__0x06\_double__&nbsp;and add our&nbsp;__CMakeLists.txt__&nbsp;file in it.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x06_double
&nbsp; 0x06_double.c
)

pico_enable_stdio_usb(0x06_double 1)

pico_add_extra_outputs(0x056_double)

target_link_libraries(0x06_double pico_stdlib)
</pre>

Next we need to copy the&nbsp;__pico\_sdk\_import.cmake__&nbsp;file from the external folder in the&nbsp;__pico-sdk__&nbsp;installation to the&nbsp;__0x06\_double__&nbsp;project folder.

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

<pre spellcheck="false">cp 0x06_double.uf2 /Volumes/RPI-RP2
</pre>

Then we need to locate the USB drive so you can do the following.

<pre spellcheck="false">ls /dev/tty.
</pre>

Press tab to find the drive and then in my case I will use&nbsp;__screen__&nbsp;to connect.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

You should see a an&nbsp;_40.5_&nbsp;being printed every second.

<pre spellcheck="false">40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
</pre>

In our next lesson we will debug.