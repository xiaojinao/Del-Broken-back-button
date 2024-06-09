# Del-Broken-back-button
My backspace key is broken, and I’m using this program to remap it to the ‘Delete’ key or another key as a replacement.

First off, make sure you’ve got PyInstaller installed on your computer. If it’s not on there yet, you can sort that out by running
```pip install pyinstaller```   in the terminal. 

There’s a minor issue; when the tray icon’s path isn’t set properly, closing the program causes it to exit directly. Only when the tray icon is correctly set can it be minimized to the tray.

These are the libraries required for running the program.
```pip install keyboard```
```pip install PyQt5```
