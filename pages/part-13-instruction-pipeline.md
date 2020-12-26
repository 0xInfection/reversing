# Part 13 - Instruction Pipeline

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

The processor works with three separate phases which are:

1)__Fetch Phase__ – The control unit grabs the instruction from memory and loads it into the instruction register.

2)__Decode Phase__ – The control unit configures all of the hardware within the processor to perform the instruction.

3)__Execute Phase__ – The processor computes the result of the instruction or operation.

When the processor processes instruction 1 we refer to it as being in the fetch phase.&nbsp;When the processor processes instruction 2, instruction 1 goes into the decode phase and instruction 2 goes into the fetch phase.&nbsp;When the processor processes instruction 3, instruction 2 goes into the decode stage and instruction 1 goes into the execute stage.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="https://media-exp1.licdn.com/dms/image/C4E12AQFTBw1u9zr2_Q/article-inline_image-shrink_1000_1488/0/1520148744958?e=1614211200&amp;v=beta&amp;t=4CLn6lQiCIMVYZFGy1Nj5_0ZDeXVP8EN_0PvIYOqYes"/></div>

Keep in mind, if a branch instruction occurs, the pipeline might be flushed and start over again with a fresh set of cycles.

You now have a strong basis and background of ARM Assembly and how it works regarding its load and store capability between memory and the respective registers and the basics of how the instruction set flows.

Next week we will dive into our first C++ program!