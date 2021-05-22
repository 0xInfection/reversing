## Part 17 - "ABSOLUTE POWER CORRUPTS ABSOLUTELY!", The Tragic Tale Of Input...

"But I am just here to learn Reverse Engineering I am really not interested in the non-sexy coding part, I just want the Reverse Engineering challenge and be a superstar!"

Ahh the naivety of the non-Jedi. For much they have to learn or perhaps unlearn to really learn!

I take not a shot at programming books and courses that teach how to capture STDIN from users in a simplistic manner like 'scanf' however I rather challenge YOU to consider a proper approach.

We are dealing with a microcontroller. It is THE target of Ransomware Authors, State Agents and all sorts of unsavory parties. WE must FIRST take TIME to understand how to properly handle input regarding a microcontroller.

I have taken the liberty to construct a proper input function for your examination.

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

<pre spellcheck="false"></pre>

"Woah I thought we were taking it slow!" The time has come to properly start to understand how to be a Jedi when designing effective software. The TIME has come to take the time to properly digest a REAL input validation function.

I want you to take the time and digest this function so that we can review it in the next lesson.

In our next lesson we will properly break down this work of genius to properly understand and craft and ultimately Reverse Engineer in our coming future!