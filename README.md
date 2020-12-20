# TileGen

TileGen is an isometric tiles generator. Its purpose is to ease the creation of the 48 tiles in the bitmasking method, described here:

https://gamedevelopment.tutsplus.com/tutorials/how-to-use-tile-bitmasking-to-auto-tile-your-level-layouts--cms-25673

You give 2 states-tiles and the tool will generate all the possible combinations between them.

input.png:

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/entry_example.png?raw=true">


Atlas result: (I cropped it because 48 would be too big for the readme):

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/atlas_example.png?raw=true">


Result in a map (in the gui preview):

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/example_result.png?raw=true">

Works with any size as long as you respect the 2:1 ratio 
(it's better if the input tile width is divisible by 3, or else the tool will "fill" some pixels with the content of its neighbors for edge cases)


## How to install

You will need python 3, and the Pillow imaging library for python and numpy
And pyside2 

to install those packages:

```
  pip install Pillow numpy PySide2
```

## How to run
  
  flags:
  
    - input: input file (default: "input.png") 

    - output: output file (default: "result.png") 
    
    - background: set a background to all result (for isometric tiles requiring height, optional)
    
    - frames: set the number of frames

```
  python ./tile_gen.py --input input.png --output result.png --background background.png --frames 1
```

## GUI


You can run the program with an ui:

```
  python ./gui.py
```

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/example.png?raw=true">

example:

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/tuto.gif?raw=true">

If you want to use frames for animated tiles, you need an input in this format (for 4 frames for instance):

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/frames.png?raw=true" width=200>

for that result:

<img src="https://github.com/jrouillard/TileGen/blob/master/doc/frames_animated.gif?raw=true">
