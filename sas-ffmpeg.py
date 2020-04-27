from ffmpy import FFmpeg
from PIL import Image, ImageFont, ImageDraw
from os.path import exists
import saslib

import numpy as np
from itertools import chain
import time

# VARIABLES:
name = "Bože, tys můj bůh!"
name_fontsize = 90
verse = "Žalm 63"
verse_fontsize = int(name_fontsize * 0.62)
text_color = 'rgb(60, 60, 60)'
intro_length = 3
overlay = 2

input_video = "sample4.mp4"
video_start = 10
video_end = 13
resolution = '1920:1080'
fps = 29.97


#######################

# THIS IS INTRO SECTION:

# Image used as intro background:
introbg = "BCPlogonazev.png"


intropic = Image.open(introbg)
draw = ImageDraw.Draw(intropic)

# create font object with the font file and specify
# desired size

name_font = ImageFont.truetype('Arial.ttf', size=name_fontsize)
verse_font = ImageFont.truetype('Arial.ttf', size=verse_fontsize)

# Position of the name and verse text:
# Anchor is x and y coordinates of a point - under which the text will be drawn
anchor = (1342, 744)

# Position of the name calculations:
name_dimensions = name_font.getsize(name)
name_offset = (name_dimensions[0] / 2, 0)
name_position = np.subtract(anchor, name_offset)

# Position of the verse, relative to the name position - centered:
verse_dimensions = verse_font.getsize(verse)
xoffset = int((name_dimensions[0] - verse_dimensions[0]) / 2)
yoffset = int(name_dimensions[1] + 30)
verse_offset = (xoffset, yoffset)
verse_position = np.add(name_position, verse_offset)



# draw the message on the background

draw.text(name_position, name, fill=text_color, font=name_font)
draw.text(verse_position, verse, fill=text_color, font=verse_font)

# save the edited image

intro_file_pic = 'intro.png'
intropic.save(intro_file_pic)
intro_file_vid = 'intro.mp4'

if not exists(intro_file_vid):
    intro = FFmpeg(executable="./ffmpeg",
        inputs={intro_file_pic: '-loop 1 -t ' + str(intro_length)},
        outputs={intro_file_vid: '-y -vf fps=29.97 -crf 0'}
    )
    intro.run()

###################### END OF INTRO

###################################
# VIDEO SECTION:

# output_opts = '-y -vf scale=' + resolution + ',fps=' + str(fps)
# output_opts = '-filter_complex "gltransition=duration=1:offset=2:source=fade.glsl " -y'
output_opts = '-y -an \
-filter_complex "\
[0:v]trim=start=0:end=' + str(round(intro_length - overlay, 2)) + ',setpts=PTS-STARTPTS[firstclip]; \
[1:v]colorbalance=bs=.3:rh=0.3[corrected]; \
[corrected]trim=start=' + str(overlay + video_start) + ':end=' + str(video_end) + ',setpts=PTS-STARTPTS[secondclip]; \
[0:v]trim=start=' + str(round(intro_length - overlay, 2)) + ':end=' + str(intro_length) + ',setpts=PTS-STARTPTS[fadeoutsrc]; \
[1:v]colorbalance=bs=.3:rh=0.3[corrected]; \
[corrected]trim=start=' + str(video_start) + ':end=' + str(overlay + video_start) + ',setpts=PTS-STARTPTS[fadeinsrc]; \
[fadeinsrc]format=pix_fmts=yuva420p, \
            fade=t=in:st=0:d=' + str(overlay) + ':alpha=1[fadein]; \
[fadeoutsrc]format=pix_fmts=yuva420p, \
            fade=t=out:st=0:d=' + str(overlay) + ':alpha=1[fadeout]; \
[fadein]fifo[fadeinfifo]; \
[fadeout]fifo[fadeoutfifo]; \
[fadeoutfifo][fadeinfifo]overlay[crossfade]; \
[firstclip][crossfade][secondclip]concat=n=3[output] " -map [output] -preset ultrafast'

# [1:v]eq=brightness=0:saturation=1.5[corrected];\

video = FFmpeg(executable="ffmpeg",
    inputs={intro_file_vid: None, input_video: None},
    outputs={'output.mp4': output_opts}
)

print(video.cmd)

video.run()


###################### END OF VIDEO

###################################
# MIXING SECTION:


#
# final = CompositeVideoClip([intro, video.set_start(intro.end-1).crossfadein(1)])   # .crossfadein(1)



########################## END OF MIXING

########################################
# OUTPUT SECTION:



# final.write_videofile("output.mp4", fps=fps, preset="ultrafast", codec="libx264", logger=None) #, ffmpeg_params=["-x264-params", "sliced-threads=4"])





########################### END OF OUTPUT





# fix_rgb, magnitude = rgb_correction(40, 60)
# fixx_rgb = fix_rgb

# print("output: ", fix_rgb)
# print(type(fixx_rgb))
# print("magnitude: ", magnitude)

# fix_clip = ColorClip((1920, 1080), color=fix_rgb)

# amber = ColorClip((1920, 1080), color=(255, 192, 0))
# blue = ColorClip((300, 300), color=(0, 0, 255))
# magenta = ColorClip((1920, 1080), color=(255, 0, 255))
# green = ColorClip((300, 300), color=(0, 255, 0))
# black = ColorClip((1920, 1080), color=(0, 0, 0))
# gray = ColorClip((1920, 1080), color=(128, 128, 128))
