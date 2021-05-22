## Part 18 - "FOR 800 YEARS HAVE I TRAINED JEDI!", The FORCE That IS Input...

"The year is 2021 and seven months, the average price of a gallon of gas within the United States is $7.51 a gallon. Four other U.S. Pipelines were compromised with Ransomware and the Five Eyes discovered a compromised network within one of the water supplies within a major metropolitan U.S. City."

"Intelligence sources have located the HQ of the 'Dark Eyes' organization behind the malware attacks and utilize a Pico Microcontroller as the controller inside a drone which is gearing up to strike this facility and knock out their communications to avoid the attack on our water supply."

"The attack coordinates are '61.013693050912785, 99.19670587477269' to which the Drone Operator enters in, '61.013693050912785, 9e.19670587477269', which is 'Mir Mines, Russia'. They launch the drone and it detonates at, '61.013693050912785, 9.19670587477269', which is 'Nord-Aurdal Municipality, Norway'."

"Panic ensues however DHS was able to secure the water supply network before Ransomware was able to encrypt their network and within twelve hours the network was fully secured."

Ok...

I wanted to take the time to really show the absolute CRITICALITY of designing software with proper input handling. Using 'scanf' or other techniques which do not properly handle every keystroke can lead to a situation like the one outlined above.

Let's review our input function...

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include "pico/stdlib.h"

#define ZERO 0x30
#define NINE 0x39
#define PERIOD 0x2e
#define CAPITAL_A 0x41
#define LOWER_CASE_Z 0x7a
#define BACKSPACE 0x08
#define DEL 0x7f

void input(char type, char* p_usb_char, char* p_usb_string, const int* p_USB_STRING_SIZE)
{
  *p_usb_char = '\0';
  *p_usb_char = getchar_timeout_us(0);
  if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
  {
    if(p_usb_string[0] != '\0')
    {
      printf("\b");
      printf(" ");
      printf("\b");
      p_usb_string[strlen(p_usb_string)-1] = '\0';
    }
  }
  if(type == 'f')
  { 
    char* period;
    while((*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE) || *p_usb_char == PERIOD)
    {
      if(*p_usb_char == PERIOD)
        period = strchr(p_usb_string, '.');
      if(period == NULL) 
      {
        if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
        {
          putchar(*p_usb_char);
          strncat(p_usb_string, p_usb_char, 1);
        }
        *p_usb_char = '\0';
      }
      else
        break;
    }
  }
  else if(type == 'd')
  { 
    while(*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE)
    {
      if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
      {
        putchar(*p_usb_char);
        strncat(p_usb_string, p_usb_char, 1);
      }
      *p_usb_char = '\0';
    }
  }
  else if(type == 's')
  { 
    while(*p_usb_char &gt;= CAPITAL_A &amp;&amp; *p_usb_char &lt;= LOWER_CASE_Z)
    {
      if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
      {
        putchar(*p_usb_char);
        strncat(p_usb_string, p_usb_char, 1);
      }
      *p_usb_char = '\0';
    }
  }
}
</pre>

Today we are going to go over exactly what this function is actually doing.

<pre spellcheck="false">void input(char type, char* p_usb_char, char* p_usb_string, const int* p_USB_STRING_SIZE)
</pre>

We begin with the function header. We first are taking a _char_ of _type_ where in our example we will use _'f'_ for handling floating-point numbers. We then have a _char\*_ (pointer) _p\_usb\_char_ which will be init to _'\\0'_ in __main.c__. We then have a char\* p\_usb\_string which we will be init to _'\\0'_ in __main.c__. We then have a _const int\*_ _p\_USB\_STRING\_SIZE_ which will be init to _100_ in __main.c__.

We then create logic to properly handle a delete or backspace button.

<pre spellcheck="false">  if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
  {
    if(p_usb_string[0] != '\0')
    {
      printf("\b");
      printf(" ");
      printf("\b");
      p_usb_string[strlen(p_usb_string)-1] = '\0';
    }
  }
</pre>

We then create logic to handle if the main.c program is expecting ONLY floating-point numbers as in our story above if would have been implemented the drone would not have missed their target.

<pre spellcheck="false">  if(type == 'f')
  { 
    char* period;
    while((*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE) || *p_usb_char == PERIOD)
    {
      if(*p_usb_char == PERIOD)
        period = strchr(p_usb_string, '.');
      if(period == NULL) 
      {
        if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
        {
          putchar(*p_usb_char);
          strncat(p_usb_string, p_usb_char, 1);
        }
        *p_usb_char = '\0';
      }
      else
        break;
    }
  }
</pre>

We see that if someone enters anything other than a _ZERO_ through _NINE_ or a _PERIOD,_ the input will SIMPLY BE REJECTED!

You also see that if there is a _PERIOD_ entered a second one could not be entered either maliciously or by accident. We also handle the amount of input to be less than _100_ properly. We then properly build our string from every properly cleaned keystroke.

Similar logic handles if you are dealing with decimals or strings.

<pre spellcheck="false">  else if(type == 'd')
  { 
    while(*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE)
    {
      if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
      {
        putchar(*p_usb_char);
        strncat(p_usb_string, p_usb_char, 1);
      }
      *p_usb_char = '\0';
    }
  }
  else if(type == 's')
  { 
    while(*p_usb_char &gt;= CAPITAL_A &amp;&amp; *p_usb_char &lt;= LOWER_CASE_Z)
    {
      if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
      {
        putchar(*p_usb_char);
        strncat(p_usb_string, p_usb_char, 1);
      }
      *p_usb_char = '\0';
    }
  }
</pre>

In our next lesson we will implement this in our Pico microcontroller.