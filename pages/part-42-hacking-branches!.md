# Part 42 - Hacking Branches!

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

We are at the end of the road. This is the final video in the x64 series. The final topic is that of pointers.

What are pointers? Let us start with an example.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQElfECgOwQniw/article-inline_image-shrink_1000_1488/0/1567286671465?e=1614211200&amp;v=beta&amp;t=P9hwVD0-SOAgoyuyfc9zA6pvzJn_2CdJQdtpRGrliik"/></div>

A pointer is nothing more than a memory address. When we compile we will clearly see where lottery\_number lives in mapped memory (this is a running example unlike our unmapped Radare examples).

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE4ab3MJoNpwQ/article-inline_image-shrink_1000_1488/0/1567286745307?e=1614211200&amp;v=beta&amp;t=BwzwocyMZuqDWM1agNeVfDuWToMpqvYTR_XMr2FlPHU"/></div>

Let's add a true pointer to the example:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGmjXZggQeY0w/article-inline_image-shrink_1000_1488/0/1567287725406?e=1614211200&amp;v=beta&amp;t=DMD8tUlZJvEQOZECzQARp4vJDlFfdB8s76tfMRlKsDA"/></div>

We see the same value:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGWLWn4vW7z7A/article-inline_image-shrink_1000_1488/0/1567287787090?e=1614211200&amp;v=beta&amp;t=tCtXkULr1pEzBGb-mfpE_ixZbryWdgg3POw88UxFfhg"/></div>

Let us experiment more:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQHmKYAmZ1SrKA/article-inline_image-shrink_1000_1488/0/1567288396508?e=1614211200&amp;v=beta&amp;t=EI-9Oeh_Op-M5mZ85eB3MO_ZiHU4gNe22qCmOvirBw8"/></div>

We see the pointer address point to a new address:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEileXadTEKIg/article-inline_image-shrink_1000_1488/0/1567288456995?e=1614211200&amp;v=beta&amp;t=eESCAPzwiojC5Zf16AeWURisPNzSrf6O6tHLhG4f9-o"/></div>

Remember pointers are memory addresses of other variables. Let's look at it another way:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGTY-098Ek-PQ/article-inline_image-shrink_1000_1488/0/1567289354121?e=1614211200&amp;v=beta&amp;t=37Z8pF2Z0e9qd45_ok_SOwaVn-g-TWAVnOGPckOy5vw"/></div>

Let us compile:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFYkbOVbAhy-A/article-inline_image-shrink_1000_1488/0/1567289368216?e=1614211200&amp;v=beta&amp;t=nxJ_QalvBscq18nbg9VFQLnD4RBpKyzONk3X3bS-Jnk"/></div>

We deference by doing the following:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFuqLrULBOeXw/article-inline_image-shrink_1000_1488/0/1567289646596?e=1614211200&amp;v=beta&amp;t=BYbnWO0-1nH19bCXTNPVY9_T7GCY3dpoNUbicg9Q8FQ"/></div>

Then we compile:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQE5uQSj5JBsdg/article-inline_image-shrink_1000_1488/0/1567289657671?e=1614211200&amp;v=beta&amp;t=CwWPshPCZ_Od8XZMqR2kEhjA-BUk-uTbxttS62mE1wY"/></div>

We can see the deference pointer is equal to 777.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFQrlTy6SFp_w/article-inline_image-shrink_1000_1488/0/1567290644015?e=1614211200&amp;v=beta&amp;t=woQu0tg95AcY2lBvnemWuoQkCZ6MwFhYsLMPBa0pb-A"/></div>

We can see the example with an array:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQG_6DQa35zDfg/article-inline_image-shrink_1000_1488/0/1567290665083?e=1614211200&amp;v=beta&amp;t=41iH7FHFKVE0ESEra4aliUzXOLOcSK9KWlOZV7Gn6SQ"/></div>

Let's debug:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFWuLAZ-SMRxQ/article-inline_image-shrink_1000_1488/0/1567290786481?e=1614211200&amp;v=beta&amp;t=R-9rM7w_mSSy7YLiGyHpOzycABNOJUZiWzmnGx9HBE4"/></div>

Then we disassemble:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEIcWIYRVEQTg/article-inline_image-shrink_1000_1488/0/1567290800965?e=1614211200&amp;v=beta&amp;t=GZbgqXiQzmpmgu6RPlVWd05NWQ7lEdPp0X8O6UJ2Fjw"/></div>

Let's hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGpZWeAweYoYw/article-inline_image-shrink_1000_1488/0/1567292294462?e=1614211200&amp;v=beta&amp;t=HaLrVGqLDONYlOYYMnSuMD2FIHqCUjVM1uEO2vpa_00"/></div>

Let's re-examine the binary:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQGtTipCX0rHtg/article-inline_image-shrink_1000_1488/0/1567292311387?e=1614211200&amp;v=beta&amp;t=WHrjzp99tq8KxvvbxLEDK4Ep54dtYLKWtUbKX9fMIgE"/></div>

We can see we hacked the value of 3 with 6.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQEcOcMHbAY0YA/article-inline_image-shrink_1000_1488/0/1567292376880?e=1614211200&amp;v=beta&amp;t=yH3fBY16tP0Bny67xBPSBlTcGEHXmGomkfnmgGRuY0c"/></div>

We can see we have made the successful hack.

I hope over the years through the literal hundreds of x86, ARM and x64 tutorials you have a basic knowledge of how to do GOOD to protect critical infrastructures from malicious hands by understanding how the enemy works. Go and do GOOD work!

  