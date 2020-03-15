
"""
A simple eisometric tile generator
"""


import argparse
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
import numpy as np


def treat_frame(factor, background, imleft, imright):

    imgleftwidth, imgleftheight = imleft.size
    control = imleft.copy()
    imleft = imleft.resize((imgleftwidth * factor, imgleftheight * factor), resample=Image.NEAREST)
    imright = imright.resize((imgleftwidth* factor, imgleftheight * factor), resample=Image.NEAREST)
    imcropwidth, imcropheight = imleft.size
    size = (imcropwidth, imcropheight)
    debug = imleft.copy()

    coord = [
        (round(0.5 * imcropwidth), round(imcropheight * 1)), # 0
        (round(4/6 * imcropwidth), round(imcropheight * 5/6)), # 1
        (round(5/6 * imcropwidth), round(imcropheight * 4/6)), # 2
        (round(1   * imcropwidth), round(imcropheight * 0.5)), # 3
        (round(5/6 * imcropwidth), round(imcropheight * 2/6)), # 4
        (round(4/6 * imcropwidth), round(imcropheight * 1/6)), # 5
        (round(0.5 * imcropwidth), 0), # 6
        (round(2/6 * imcropwidth), round(imcropheight * 1/6)), # 7
        (round(1/6 * imcropwidth), round(imcropheight * 2/6)), # 8
        (round(0   * imcropwidth), round(imcropheight * 0.5)), # 9
        (round(1/6 * imcropwidth), round(imcropheight * 4/6)), # 10
        (round(2/6 * imcropwidth), round(imcropheight * 5/6)), # 11
        (round(0.5 * imcropwidth), round(imcropheight * 4/6)), # 12
        (round(4/6 * imcropwidth), round(imcropheight * 0.5)), # 13
        (round(0.5 * imcropwidth), round(imcropheight * 2/6)), # 14
        (round(2/6 * imcropwidth), round(imcropheight * 0.5)), # 15
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

    positionsbbox = [
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

    ls1 = get_pixels(imleft, square1, False, debug)
    ls2 = get_pixels(imleft, square2withoffset, (0, -1), debug)
    ls3 = get_pixels(imleft, square3, False, debug)
    ls4 = get_pixels(imleft, square4withoffset, (-3, -1), debug)
    ls5 = get_pixels(imleft, square5, False, debug)
    ls6 = get_pixels(imleft, square6withoffset, (0, 0), debug)
    ls7 = get_pixels(imleft, square7, False, debug)
    ls8 = get_pixels(imleft, square8withoffset, (-3, 0), debug)
    ls9 = get_pixels(imleft, square9, False, debug)

    rs1 = get_pixels(imright, square1, False, False)
    rs2 = get_pixels(imright, square2, False, False)
    rs3 = get_pixels(imright, square3, False, False)
    rs4 = get_pixels(imright, square4, False, False)
    rs5 = get_pixels(imright, square5, False, False)
    rs6 = get_pixels(imright, square6, False, False)
    rs7 = get_pixels(imright, square7, False, False)
    rs8 = get_pixels(imright, square8, False, False)
    rs9 = get_pixels(imright, square9, False, False)

    all_directions = [
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
    result_imgs = []
    for direction in all_directions:
        result_imgs.append(
            paste_background(
                fix_pixels(
                    create_square(direction, size, positionsbbox, factor),
                    control),
                background))

    return result_imgs

def treat_image(path, bg, frames):
    im = Image.open(path)
    background = None
    if bg:
        background = Image.open(bg)
    imgwidth, imgheight = im.size
    original_h = imgheight
    original_w = int(imgwidth/(2*frames))
    factor = 3

    if (imgheight * 4 * frames != imgwidth):
        raise Exception('Error, not a good ratio')

    imcopy = im.copy()
    imright = imcopy.crop((imgwidth/2, 0, imgwidth, imgheight))
    imleft = imcopy.crop((0, 0, imgwidth/2, imgheight))

    frames_list = []
    for index in range(0, frames*2, 2):
        w = int(imgwidth/(2 * frames))
        imleft = imcopy.crop((index * w, 0, (index + 1) * w, imgheight))
        # imleft.save('debug/debug_left_' + str(index) + '.png')
        imright = imcopy.crop(((index + 1) * w, 0, (index + 2) * w, imgheight))
        # imright.save('debug/debug_right_' + str(index) + '.png')
        frames_list.append(treat_frame(factor, background, imleft, imright))
    return frames_list, frames, background, (original_w, original_h)

def create_demo_images(frames, frames_number, background, size, size2):
    result = []

    for i in range(frames_number):
            
        demo = Image.new('RGBA', (size2[0], size2[1]))

        if not background:
            background = Image.new('RGBA', (1, 1))
        rows = [
            [frames[i][5], frames[i][13], background, background, background, background],
            [frames[i][9], frames[i][47], frames[i][5], frames[i][13], background, background],
            [background, frames[i][8], background, frames[i][23], background, background],
            [background, frames[i][21], frames[i][1], frames[i][2], background, background],
            [frames[i][5], frames[i][14], frames[i][2], background, background, background],
            [frames[i][16], frames[i][34], background, frames[i][13],  background, background],
            [frames[i][1], frames[i][7], frames[i][26], frames[i][6], background, background],
            [background, frames[i][4], background, frames[i][15], background, background],
            [background, background, frames[i][13], frames[i][6], background, background],
            [background, frames[i][14], background, frames[i][2], background, background],
            [frames[i][5], frames[i][19], frames[i][18], background, background, background],
            [frames[i][3],frames[i][3], frames[i][2], background, background, background],
        ]
        for y in range(-1, 11):
            for x in range(0,5):
                if y%2 == 0 :
                    demo.paste(rows[y+1][x], (int(x * size[0] ), int(y*(size[1]/2))), rows[y+1][x])
                else:
                    demo.paste(rows[y+1][x], (int(x * size[0] - size[0] / 2), int(y*(size[1]/2))), rows[y+1][x])
        result.append(ImageQt(demo))
    return result

def fix_pixels(image, control):
    pix = image.load()
    pix_control = control.load()

    control_width, control_height = control.size  # Get the width and hight of the image for iterating over
    bad_pix = []
    for x in range(control_width):
        for y in range(control_height):
            if (pix[x, y][3] != pix_control[x, y][3]):
                bad_pix.append((x, y))

    for px in bad_pix:
        for x in range(px[0]-1, px[0]+2, 1):
            if (x >= control_width or x < 0):
                continue
            for y in range(px[1]-1, px[1]+2, 1):
                if (y >= control_height or x < 0):
                    continue
                if (pix[x, y][3] != 0):
                    pix[px[0], px[1]] = pix[x, y]

    return image

def save_result(frames, filename):
    imgwidth, imgheight = frames[0][0].size

    result_final = Image.new('RGBA', (len(frames) * imgwidth, len(frames[0]) * (imgheight)))

    for index, frame in enumerate(frames):
        for i, img in enumerate(frame):
            result_final.paste(img, (index * imgwidth, i*(imgheight)), img)

    result_final.save(filename)

def create_square(squares, size, positionsbbox, factor):
    result = Image.new('RGBA', size)
    for i, square in enumerate(squares):
        result.paste(
            square.image,
            (positionsbbox[i][0] + square.get_offset()[0], positionsbbox[i][1] + square.get_offset()[1]),
            square.image)

    imgwidth, imgheight = result.size
    result = result.resize((round(imgwidth / factor), round(imgheight/factor)), resample=Image.NEAREST)
    return result


class PixelLosange():
    def __init__(self, image, bbox, offset):
        self.image = image
        self.bbox = bbox
        self.offset = offset
    def get_coords(self):
        return (self.bbox[0], self.bbox[1])
    def get_offset(self):
        return self.offset

def get_pixels(img, coords, offset, debug):
    im_array = np.asarray(img)
    mask_im = Image.new('L', (im_array.shape[1], im_array.shape[0]), 0)
    ImageDraw.Draw(mask_im).polygon(coords, outline=1, fill=1)

    if debug:
        ImageDraw.Draw(debug).polygon(coords, outline=(255, 255, 255, 255), fill=0)

    mask = np.array(mask_im)
    new_im_array = np.empty(im_array.shape, dtype='uint8')

    new_im_array[:, :, :3] = im_array[:, :, :3]

    # transparency (4th column)
    new_im_array[:, :, 3] = mask*255
    new_im = Image.fromarray(new_im_array, "RGBA")

    pixels = list(new_im.getdata())
    new_pixels = []
    for item in pixels:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_pixels.append((0, 0, 0, 0))
        else:
            new_pixels.append(item)
    new_im.putdata(new_pixels)
    bbox = new_im.convert("RGBa").getbbox()

    result = new_im.crop(bbox)
    offset = offset if offset else (0, 0)
    return PixelLosange(result, bbox, offset)

def paste_background(img, background):
    if background:
        bgcopy = background.copy()
        bgcopy.paste(img, (0, 0), img)
        return bgcopy
    return img

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("-f", "--frames", default=1, help="number of frames")
    ARGS = PARSER.parse_args()
    framesTreated, _, _, _ = treat_image("entry.png", "background.png", int(ARGS.frames))
    save_result(framesTreated, "result.png")
