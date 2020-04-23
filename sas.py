from moviepy.editor import * #ImageClip, TextClip, CompositeVideoClip, show, preview
import moviepy.video.fx.all as vfx
import numpy as np
from itertools import chain
import time
# import pygame

# VARIABLES:
name = "Bože, tys můj bůh!"
name_fontsize = 90
verse = "Žalm 63"
verse_fontsize = int(name_fontsize * 0.62)
intro_length = "2.22"

input_video = "sample.mp4"
video_start = 0
resolution = (1920, 1080)
fps = 29.97

##################### pygame:

import pygame, sys
from pygame.locals import *

# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')
# while True: # main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()


#######################

# THIS IS INTRO SECTION:

# Image used as intro background:
intropic = "BCPlogonazev.png"

# Now we turn it into a 5 sec clip:
intro_background = ImageClip(intropic)

# Name and verse of the sermon:
name = TextClip(txt=name, font="Arial", fontsize=name_fontsize, color="gray15")
verse = TextClip(txt=verse, font="Arial", fontsize=verse_fontsize, color="gray15")

# Position of the name and verse text:
# Anchor is x and y coordinates of a point - under which the text will be drawn
anchor = (1342, 744)

# Position of the name calculations:
name_dimensions = name.size
name_offset = (name_dimensions[0] / 2, 0)
name_position = np.subtract(anchor, name_offset)

# Position of the verse, relative to the name position - centered:
verse_dimensions = verse.size
xoffset = int((name_dimensions[0] - verse_dimensions[0]) / 2)
yoffset = int(name_dimensions[1] + 30)
verse_offset = (xoffset, yoffset)
verse_position = np.add(name_position, verse_offset)

preintro = CompositeVideoClip([intro_background, name.set_position(name_position), verse.set_position(verse_position)])
intro = preintro.set_duration(intro_length)
###################### END OF INTRO

###################################
# VIDEO SECTION:

prevideo = VideoFileClip(input_video)
video = prevideo.resize(resolution).set_start(video_start)




###################### END OF VIDEO

###################################
# MIXING SECTION:



final = CompositeVideoClip([intro, video.set_start(intro.end-1).crossfadein(1)])   # .crossfadein(1)



########################## END OF MIXING

########################################
# OUTPUT SECTION:



final.write_videofile("output.mp4", fps=fps, preset="ultrafast", codec="libx264")





########################### END OF OUTPUT

def rgb_correction(ab=50, gm=50):
    """
    Returns RGB array for color correction as a tuple.
    It is meant to be used as an image which
    overlays treated picure - still or motion.



    :param ab: Amber/Blue balance, aka warm/cold
                value 0-100
                0 = warmest
                100 = coldest

    :param gm: Green/Magenta balance
                value 0-100
                0 = greenest
                100 = "magentest"
    """
    a = (1, 0.75, 0)
    b = (0, 0, 1)
    g = (0, 1, 0)
    m = (1, 0, 1)

    zero = np.array((0, 0, 0))
    ones = np.array((1, 1, 1))

    warm = zero
    cold = zero
    green = zero
    magenta = zero
    ab_res = zero
    gm_res = zero

    if ab != 50:
        abx = abs(50 - ab) / 2
        if ab > 50:
            warm = np.multiply(a, abx * 5.1)
            ab_res = warm
        else:
            cold = np.multiply(b, abx * 5.1)
            ab_res = cold

    if gm != 50:
        gmx = abs(50 - gm) / 2
        if gm > 50:
            gm -= 50
            green = np.multiply(g, gmx * 5.1)
            gm_res = green
        else:
            magenta = np.multiply(m, gmx * 5.1)
            gm_res = magenta

    basic = np.add(ab_res, gm_res)
    print("basic: ", basic)
    print("gm: ", gm_res, "ab: ", ab_res)
    multiplicator = 255 / np.max(basic)
    if multiplicator <= 0 or multiplicator > 255:
        multiplicator = 1
    print("multiplicator: ", multiplicator)
    data = np.multiply(basic, multiplicator)
    preresult = np.ndarray.tolist(data.astype(int))
    # result = tuple(chain.from_iterable(preresult))
    print("preresult: ", preresult)
    result = tuple(preresult)
    magnitude = 1 / multiplicator / 2
    if ab == 50 and gm == 50:
        magnitude = 0
    return result, magnitude



fix_rgb, magnitude = rgb_correction(40, 60)
fixx_rgb = fix_rgb
# print("output: ", fix_rgb)
# print(type(fixx_rgb))
# print("magnitude: ", magnitude)

fix_clip = ColorClip((1920, 1080), color=fix_rgb)

# amber = ColorClip((1920, 1080), color=(255, 192, 0))
# blue = ColorClip((300, 300), color=(0, 0, 255))
# magenta = ColorClip((1920, 1080), color=(255, 0, 255))
# green = ColorClip((300, 300), color=(0, 255, 0))
# black = ColorClip((1920, 1080), color=(0, 0, 0))
# gray = ColorClip((1920, 1080), color=(128, 128, 128))


# result.show(0)

#
# blueclip = ImageClip('blue.jpg')
# ex = ImageClip("blue.jpg")
# blueclip2 = blueclip.fx(vfx.colorx, 0.9)
# corrected = CompositeVideoClip([blueclip2, amber.set_opacity(0.13)])
# corrected2 = CompositeVideoClip([corrected, magenta.set_opacity(0.01)])
# corrected3 = corrected2.fx(vfx.lum_contrast, lum=0, contrast=0.3, contrast_thr=126)

# # corrected.show()
# corrected.save_frame(filename="corrected.png")
# corrected2.save_frame(filename="corrected2.png")
# corrected3.save_frame(filename="corrected3.png")
# fix_clip.save_frame(filename="fix.png")
#
#
# cor = ColorClip((1920, 1080), color=(255, 200, 39))
# # cor.save_frame(filename="cor.png")
# mid = blueclip.fx(vfx.colorx, 0.9)
# mid2 = CompositeVideoClip([mid, cor.set_opacity(0.13)])
# final = mid2.fx(vfx.lum_contrast, lum=0, contrast=0.3, contrast_thr=126)
# final.save_frame(filename="final.png")

# run = True
# while run: # main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             run = False

# print("hello")

# result.write_videofile("test.mp4", fps=29.97, ffmpeg_params=['-crf', '22'], codec='libx264')
# result.save_frame(filename='test.png')
