# TileGen

TileGen is an isometric tiles generator. Its purpose is to ease the creation of the 48 tiles in the bitmasking method, described here:
https://gamedevelopment.tutsplus.com/tutorials/how-to-use-tile-bitmasking-to-auto-tile-your-level-layouts--cms-25673

You give 2 states-tiles and the tool will generate all the possible combinations between them.

Entry.png:

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/entry_example.png?raw=true">


Result example (it actually generates a vertical atlas, but for readibility purposes here is an example of the tiles generated):

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/example_result.png?raw=true">

Works with any size as long as you respect the 2:1 ratio 
(it's better if the entry file width is divisible by 3, or else the tool will "fill" some pixels with the content of its neighbors for edge cases)


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
  
    - entry: entry file (default: "entry.png") 
    
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

example:

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/tuto.gif?raw=true">

If you want to use frames for animated tiles, you need an entry in this format (for 4 frames for instance):

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/frames.png?raw=true" width=200>

for that result:

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/frames_animated.gif?raw=true">
