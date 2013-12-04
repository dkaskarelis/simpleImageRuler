simpleImageRuler
================

A program to measure things in photos

Please see screenshot.png for what you can expect. 

S.I.R. requires:

Python 2.7
PySide 1.1
Qt 4.8

installed on your computer.


How to use
----------

1. Load a photo (.jpg or .png) which contains some sort of scale or ruler <br>
2. Press CAL to start calibration, drag the mouse over a known length, and give the length value as input
3. Switch to "line mode" and start measuring whatever you want
4. Or switch to "path mode" and do likewise. A path is stopped by pressing the right mouse button. 


Limitations
-----------

Labels are currently available only in German language.

License
------

GPL 2 

Start
-----

```SimpleImageRuler.py [de|en]```

To translate in an other language, edit in file complete.pro your language qt_xx.ts. The xx is your code.

```pylupdate4 complete.pro```

Translate the .ts file

```lrelease complete.pro```


