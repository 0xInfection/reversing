# Part 17 - ROR Instruction

For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Over the next few tutorials we are going to write a very basic x86 Operating System to which we will use QEMU which is a full system emulator or OS emulator. You could also install VirtualBox and ultimately convert our boot loader to an ISO if you so choose.

At the very core of a computer booting is what we refer to as the boot loader. The boot loader physically reads the first sector or sector 0 from your HD or other media to ultimately bootstrap an OS.

When the computer boots it reads the first sector which is exactly 0x200 bytes (hex) or 512 bytes in decimal.

The system that is reading this boot loader is what is referred to as BIOS which is a basic input output system and it loads in 16-bit mode. It does this to be compatible with older processors. Modern processors immediately switch to what we refer to as UEFI which is a more sophisticated IO system however we will focus on the very basics here with BIOS.

Next week we will discuss what exactly goes on when BIOS reads the boot sector.