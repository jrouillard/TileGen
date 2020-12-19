# TileGen
Isometric tileset generator 

Entry.png:

<img src="https://github.com/jrouillard/TileGen/blob/master/entry.png?raw=true" width=300>


Result:

<img src="https://github.com/jrouillard/TileGen/blob/master/result.png?raw=true" width=400>

Works with any size as long as you respect the 2:1 ratio 
(it's better if the entry file width is divisible by 3)


## How to install

You will need python 3, and the Pillow imaging library for python and numpy
And pyside2 

to install those packages:

```
  pip install Pillow
  pip install numpy
  pip install PySide2
```

## How to run
  
  flags:
    - entry: file to treat (default: "entry.png") 
    - background: set a background to all result (for isometric tiles requiring height, optional)
    - frames: set a background to all result (for isometric tiles requiring height, optional)

```
  python ./tileGen.py --entry entry.png --background background.png --frames 1
```

## GUI


You can run the program with an ui:

```
  python ./gui.py
```

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/example.png?raw=true">

gif of usage:

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/tuto.gif?raw=true">

If you want to use frames for animated tiles, you need an entry in that format (for 4 frames for instance):

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/frames.png?raw=true" width=200>

for that result:

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/frames_animated.gif?raw=true">
