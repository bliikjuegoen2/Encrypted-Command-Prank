# Miscellaneous Scripts

This repository is a collection of various Python scripts that I have written

## prank.py

This would script would encrypt a piece of code. The behaviour of the original code is preserved when being ran in a script or the Python Shell. I used this script to prank my friends. I would write code that would display a funny message, use the script to encrypt it and then tell them to run the encrypted piece of code on their machine.

### Usage of prank.py  

To encrypt a piece of code just run:

```bash
./prank.py -c "print('Hello World')"
```

more options can be found with `-h`

```bash
./prank.py -h
```

## fix-bootloader.py

I run Arch Linux and sometimes updates would break my system. The most common one is that the Grub bootloader would no longer be recognized my the system. This script automates the repairing of the bootloader.

### Usage of fix-bootloader.py

Just follow the instructions given in the popup box after running the script.


```bash
./fix-bootloader.py
```
