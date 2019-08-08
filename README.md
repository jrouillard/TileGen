# TileGen
Isometric tileset generator 

Entry.png:

<img src="https://github.com/jrouillard/TileGen/blob/master/entry.png?raw=true" width=300>


Result:

<img src="https://github.com/jrouillard/TileGen/blob/master/result.png?raw=true" width=400>

Works with any size as long as you respect the 2:1 ratio


## How to install

You will need python 3, and the Pillow imaging library for python and numpy

to install those packages:

```
  pip install Pillow
  pip install numpy
```

## How to run

  go into the folder, change entry.png by your tiles
  
  run
  
```
  python ./tileCreate.py
```

## Options

There is a "frames" flag if you need to generate more than 2 tiles
Simply stick your additional tiles to your entry.png

```
  python ./tileCreate.py --frames {number of additional frames}
```


