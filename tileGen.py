
import argparse
import math
from PIL import Image, ImageDraw
import numpy as np

import math


def treatFrame(id, factor, background, imleft, imright):

    imgleftwidth, imgleftheight = imleft.size
    control = imleft.copy()
    imleft = imleft.resize((imgleftwidth * factor, imgleftheight * factor), resample=0)
    imright = imright.resize((imgleftwidth* factor, imgleftheight * factor), resample=0)
    imcropwidth, imcropheight = imleft.size
    size = (imcropwidth, imcropheight)
    debug = imleft.copy()

    coord = [
      (round(0.5 * imcropwidth), round(imcropheight * 1  )   ), # 0
      (round(4/6 * imcropwidth), round(imcropheight * 5/6)   ), # 1
      (round(5/6 * imcropwidth), round(imcropheight * 4/6)   ), # 2
      (round(1   * imcropwidth), round(imcropheight * 0.5)   ), # 3
      (round(5/6 * imcropwidth), round(imcropheight * 2/6)   ), # 4
      (round(4/6 * imcropwidth), round(imcropheight * 1/6)   ), # 5
      (round(0.5 * imcropwidth), 0   ), # 6
      (round(2/6 * imcropwidth), round(imcropheight * 1/6)   ), # 7
      (round(1/6 * imcropwidth), round(imcropheight * 2/6)   ), # 8
      (round(0   * imcropwidth), round(imcropheight * 0.5)   ), # 9
      (round(1/6 * imcropwidth), round(imcropheight * 4/6)   ), # 10
      (round(2/6 * imcropwidth), round(imcropheight * 5/6)   ), # 11
      (round(0.5 * imcropwidth), round(imcropheight * 4/6)   ), # 12
      (round(4/6 * imcropwidth), round(imcropheight * 0.5)   ), # 13
      (round(0.5 * imcropwidth), round(imcropheight * 2/6)   ), # 14
      (round(2/6 * imcropwidth), round(imcropheight * 0.5)  ), # 15
    ]
    square1 = [
        (coord[6][0], coord[6][1]),
        (coord[5][0], coord[5][1]),
        (coord[14][0], coord[14][1]),
        (coord[7][0], coord[7][1])
    ]
    square2 = [
        (coord[5][0], coord[5][1]),
        (coord[4][0], coord[4][1]),
        (coord[13][0], coord[13][1]),
        (coord[14][0], coord[14][1])
    ]
    square2withoffset = [
        (coord[5][0]+3, coord[5][1]-1),
        (coord[4][0]+3, coord[4][1]-1),
        (coord[13][0], coord[13][1]),
        (coord[14][0], coord[14][1])
    ]
    square3 = [
        (coord[4][0], coord[4][1]),
        (coord[3][0], coord[3][1]),
        (coord[2][0], coord[2][1]),
        (coord[13][0], coord[13][1])
    ]
    square4 = [
        (coord[7][0], coord[7][1]),
        (coord[14][0], coord[14][1]),
        (coord[15][0], coord[15][1]),
        (coord[8][0], coord[8][1])
    ]
    square4withoffset = [
        (coord[7][0]-3, coord[7][1]-1),
        (coord[14][0], coord[14][1]),
        (coord[15][0], coord[15][1]),
        (coord[8][0]-3, coord[8][1]-1)
    ]
    square5 = [
        (coord[14][0], coord[14][1]),
        (coord[13][0], coord[13][1]),
        (coord[12][0], coord[12][1]),
        (coord[15][0], coord[15][1])
    ]
    square6 = [
        (coord[13][0], coord[13][1]),
        (coord[2][0], coord[2][1]),
        (coord[1][0], coord[1][1]),
        (coord[12][0], coord[12][1])
    ]
    square6withoffset = [
        (coord[13][0], coord[13][1]),
        (coord[2][0]+3, coord[2][1]+1),
        (coord[1][0]+3, coord[1][1]+1),
        (coord[12][0], coord[12][1])
    ]
    square7 = [
        (coord[8][0], coord[8][1]),
        (coord[15][0], coord[15][1]),
        (coord[10][0], coord[10][1]),
        (coord[9][0], coord[9][1])
    ]
    square8 = [
        (coord[15][0], coord[15][1]),
        (coord[12][0], coord[12][1]),
        (coord[11][0], coord[11][1]),
        (coord[10][0], coord[10][1])
    ]
    square8withoffset = [
        (coord[15][0], coord[15][1]),
        (coord[12][0], coord[12][1]),
        (coord[11][0]-3, coord[11][1]+1),
        (coord[10][0]-3, coord[10][1]+1)
    ]
    square9 = [
        (coord[12][0], coord[12][1]),
        (coord[1][0], coord[1][1]),
        (coord[0][0], coord[0][1]),
        (coord[11][0], coord[11][1])
    ]

    positionsbbox= [
        (square1[3][0], square1[0][1]),
        (square2[3][0], square2[0][1]),
        (square3[3][0], square3[0][1]),
        (square4[3][0], square4[0][1]),
        (square5[3][0], square5[0][1]),
        (square6[3][0], square6[0][1]),
        (square7[3][0], square7[0][1]),
        (square8[3][0], square8[0][1]),
        (square9[3][0], square9[0][1]),
    ]

    ls1 = getPixels(imleft, square1, False, debug)
    ls2 = getPixels(imleft, square2withoffset, (0, -1), debug)
    ls3 = getPixels(imleft, square3, False, debug)
    ls4 = getPixels(imleft, square4withoffset, (-3, -1), debug)
    ls5 = getPixels(imleft, square5, False, debug)
    ls6 = getPixels(imleft, square6withoffset, (0, 0), debug)
    ls7 = getPixels(imleft, square7, False, debug)
    ls8 = getPixels(imleft, square8withoffset, (-3, 0), debug)
    ls9 = getPixels(imleft, square9, False, debug)

    rs1 = getPixels(imright, square1, False, False)
    rs2 = getPixels(imright, square2, False, False)
    rs3 = getPixels(imright, square3, False, False)
    rs4 = getPixels(imright, square4, False, False)
    rs5 = getPixels(imright, square5, False, False)
    rs6 = getPixels(imright, square6, False, False)
    rs7 = getPixels(imright, square7, False, False)
    rs8 = getPixels(imright, square8, False, False)
    rs9 = getPixels(imright, square9, False, False)

    allDirections = [
        [ls5, ls5, ls5, ls5, ls5, ls5, ls5, ls5, ls5],
        [ls4, ls5, ls6, ls4, ls5, ls6, ls7, ls8, ls9],
        [ls2, ls2, ls3, ls5, ls5, ls6, ls8, ls8, ls9],
        [rs9, ls5, ls6, ls5, ls5, ls6, ls8, ls8, ls9],
        [ls5, ls5, ls6, ls5, ls5, ls6, ls8, ls8, ls9],
        [ls1, ls2, ls2, ls4, ls5, ls5, ls7, ls8, ls8],
        [ls4, ls5, rs7, ls4, ls5, ls5, ls7, ls8, ls8],
        [ls4, ls5, ls5, ls4, ls5, ls5, ls7, ls8, ls8],
        [ls2, ls2, ls2, ls5, ls5, ls5, ls8, ls8, ls8],
        [rs9, ls5, rs7, ls5, ls5, ls5, ls8, ls8, ls8],
        [ls5, ls5, rs7, ls5, ls5, ls5, ls8, ls8, ls8],
        [rs9, ls5, ls5, ls5, ls5, ls5, ls8, ls8, ls8],
        [ls5, ls5, ls5, ls5, ls5, ls5, ls8, ls8, ls8],
        [ls1, ls2, ls3, ls4, ls5, ls6, ls4, ls5, ls6],
        [ls4, ls5, ls6, ls4, ls5, ls6, ls4, ls5, ls6],
        [ls2, ls2, ls3, ls5, ls5, ls6, rs3, ls5, ls6],
        [rs9, ls5, ls6, ls5, ls5, ls6, rs3, ls5, ls6],
        [ls5, ls5, ls6, ls5, ls5, ls6, rs3, ls5, ls6],
        [ls1, ls2, ls2, ls4, ls5, ls5, ls4, ls5, rs1],
        [ls4, ls5, rs7, ls4, ls5, ls5, ls4, ls5, rs1],
        [ls4, ls5, ls5, ls4, ls5, ls5, ls4, ls5, rs1],
        [ls2, ls2, ls2, ls5, ls5, ls5, rs3, ls5, rs1],
        [rs9, ls5, rs7, ls5, ls5, ls5, rs3, ls5, rs1],
        [ls5, ls5, rs7, ls5, ls5, ls5, rs3, ls5, rs1],
        [rs9, ls5, ls5, ls5, ls5, ls5, rs3, ls5, rs1],
        [ls5, ls5, ls5, ls5, ls5, ls5, rs3, ls5, rs1],
        [ls2, ls2, ls3, ls5, ls5, ls6, ls5, ls5, ls6],
        [rs9, ls5, ls6, ls5, ls5, ls6, ls5, ls5, ls6],
        [ls5, ls5, ls6, ls5, ls5, ls6, ls5, ls5, ls6],
        [ls2, ls2, ls2, ls5, ls5, ls5, ls5, ls5, rs1],
        [rs9, ls5, rs7, ls5, ls5, ls5, ls5, ls5, rs1],
        [ls5, ls5, rs7, ls5, ls5, ls5, ls5, ls5, rs1],
        [rs9, ls5, ls5, ls5, ls5, ls5, ls5, ls5, rs1],
        [ls5, ls5, ls5, ls5, ls5, ls5, ls5, ls5, rs1],
        [ls1, ls2, ls2, ls4, ls5, ls5, ls4, ls5, ls5],
        [ls4, ls5, rs7, ls4, ls5, ls5, ls4, ls5, ls5],
        [ls4, ls5, ls5, ls4, ls5, ls5, ls4, ls5, ls5],
        [ls2, ls2, ls2, ls5, ls5, ls5, rs3, ls5, ls5],
        [rs9, ls5, rs7, ls5, ls5, ls5, rs3, ls5, ls5],
        [ls5, ls5, rs7, ls5, ls5, ls5, rs3, ls5, ls5],
        [rs9, ls5, ls5, ls5, ls5, ls5, rs3, ls5, ls5],
        [ls5, ls5, ls5, ls5, ls5, ls5, rs3, ls5, ls5],
        [ls2, ls2, ls2, ls5, ls5, ls5, ls5, ls5, ls5],
        [rs9, ls5, rs7, ls5, ls5, ls5, ls5, ls5, ls5],
        [ls5, ls5, rs7, ls5, ls5, ls5, ls5, ls5, ls5],
        [rs9, ls5, ls5, ls5, ls5, ls5, ls5, ls5, ls5],
        [ls5, ls5, ls5, ls5, ls5, ls5, ls5, ls5, ls5],
        [ls1, ls2, ls3, ls4, ls5, ls6, ls7, ls8, ls9],
    ]
    debug.save("debug.png")
    resultImgs = []
    for direction in allDirections:
        resultImgs.append(pasteBackground(fixPixels(createSquare(direction, size, positionsbbox, factor), control), background))

    return resultImgs

def treatImage(path, bg, frames):
    im = Image.open(path)
    background = Image.open(bg)
    imgwidth, imgheight = im.size
    factor = 3

    if (imgheight * 4 * frames != imgwidth):
        print('Error, not a good ratio')
        return

    imcopy = im.copy()
    imright = imcopy.crop((imgwidth/2, 0, imgwidth, imgheight))
    imleft = imcopy.crop((0, 0, imgwidth/2, imgheight))

    framesList = []
    for index in range(0,frames*2,2):
        w = int(imgwidth/(2 * frames))
        imleft = imcopy.crop((index * w, 0, (index + 1) * w, imgheight))
        # imleft.save('debug/debug_left_' + str(index) + '.png')
        imright = imcopy.crop(((index + 1) * w, 0, (index + 2) * w, imgheight))
        # imright.save('debug/debug_right_' + str(index) + '.png')
        framesList.append(treatFrame(index, factor, background, imleft, imright))
    saveResult(framesList)

def fixPixels(image, control):
    pix = image.load()

    pixControl = control.load()

    controlWidth, controlHeight = control.size  # Get the width and hight of the image for iterating over
    badPix = []
    for x in range(controlWidth):
        for y in range(controlHeight):
            if (pix[x,y][3] != pixControl[x,y][3]):
                badPix.append((x,y))

    for px in badPix:
        fixed = False
        for x in range(px[0]-1, px[0]+2, 1):
            if (x >= controlWidth or x < 0):
                continue
            for y in range(px[1]-1, px[1]+2, 1):
                if (y >= controlHeight or x < 0):
                    continue
                if (pix[x, y][3] != 0):
                    pix[px[0], px[1]] = pix[x, y]

    return image

def saveResult(frames):
    imgwidth, imgheight = frames[0][0].size

    resultFinal = Image.new('RGBA', (len(frames) * imgwidth,len(frames[0]) * (imgheight)))

    for index,frame in enumerate(frames):
        for i, img in enumerate(frame):
            resultFinal.paste(img, (index * imgwidth, i*(imgheight)), img)

    resultFinal.save("atlas.png")

def createSquare(squares, size, positionsbbox, factor):
    result = Image.new('RGBA', size)
    for i, square in enumerate(squares):
        result.paste(
            square.image,
            (positionsbbox[i][0] + square.getOffset()[0], positionsbbox[i][1] + square.getOffset()[1]),
            square.image)

    imgwidth,imgheight = result.size
    result = result.resize((round(imgwidth / factor), round(imgheight/factor)))
    return result


class PixelLosange():
    def __init__(self, image, bbox, offset):
        self.image = image
        self.bbox = bbox
        self.offset = offset
    def getCoords(self):
        return (self.bbox[0], self.bbox[1])
    def getOffset(self):
        return self.offset

def getPixels(img, coords, offset, debug):
    imgwidth, imgheight = img.size
    imArray = np.asarray(img)
    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
    ImageDraw.Draw(maskIm).polygon(coords, outline=1, fill=1)
    if debug:
        ImageDraw.Draw(debug).polygon(coords, outline=(255,255,255,255), fill=0)
    mask = np.array(maskIm)
    newImArray = np.empty(imArray.shape,dtype='uint8')

    newImArray[:,:,:3] = imArray[:,:,:3]

    # transparency (4th column)
    newImArray[:,:,3] = mask*255
    newIm = Image.fromarray(newImArray, "RGBA")

    width, height = newIm.size

    pixels = list(newIm.getdata())
    newPixels = []
    for item in pixels:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newPixels.append((0, 0, 0, 0))
        else:
            newPixels.append(item)
    newIm.putdata(newPixels)
    bbox = newIm.convert("RGBa").getbbox()

    result = newIm.crop(bbox)
    offset = offset if offset else (0,0)
    return PixelLosange(result, bbox, offset)

def pasteBackground(img, background):
    bgwidth, bgheight = background.size
    bgcopy = background.copy()
    bgcopy.paste(img, (0,0), img)
    return bgcopy




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--frames", default=1, help="number of frames")
    args = parser.parse_args()
    treatImage("entry.png", "background.png", int(args.frames))
