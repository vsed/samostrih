from ffmpy import FFmpeg
from PIL import Image, ImageFont, ImageDraw
from os.path import exists
import saslib, subprocess
import numpy as np
from itertools import chain
import time

def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + round(float(s), 2)

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

def ff_correction(ambl=0, grma=0):
    r = 0.0
    g = 0.0
    b = 0.0

    if ambl < 0:
        b = abs(ambl / 200)
    if ambl > 0:
        r = ambl / 200
        g = ambl / 266.66666
    if grma < 0:
        g += abs(grma / 200)
    if grma > 0:
        r += grma / 200
        b += grma / 200

    c = (max(r, g, b) / 2)
    rr = round(r - c, 2)
    gg = round(g - c, 2)
    bb = round(b - c, 2)
    return rr, gg, bb


def render(name="Sermon Title", name_fontsize=90, verse="Verse", intro_length=3, overlay=2, input_video="sample.mp4",
           video_start="00:00:00", video_end="00:00:10", amber_blue=0, green_magenta=0):
    # VARIABLES:
    verse_fontsize = int(name_fontsize * 0.62)
    text_color = 'rgb(60, 60, 60)'

    resolution = '1920:1080'
    fps = 29.97

    video_start_sec = get_sec(video_start)
    video_end_sec = get_sec(video_end)
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
        intro = FFmpeg(executable="ffmpeg",
                       inputs={intro_file_pic: '-loop 1 -t ' + str(intro_length)},
                       outputs={intro_file_vid: '-y -vf fps=29.97 -crf 0'}
                       )
        intro.run()

    ###################### END OF INTRO

    ###################################
    # VIDEO SECTION:

    input_opts = "-ss " + video_start

    rgb = ff_correction(amber_blue, green_magenta)
    r = str(rgb[0])
    g = str(rgb[1])
    b = str(rgb[2])
    cbopts = "rs=" + r + ":gs=" + g + ":bs=" + b
    cbopts += ":rm=" + r + ":gm=" + g + ":bm=" + b
    cbopts += ":rh=" + r + ":gh=" + g + ":bh=" + b

    # output_opts = '-y -vf scale=' + resolution + ',fps=' + str(fps)
    # output_opts = '-filter_complex "gltransition=duration=1:offset=2:source=fade.glsl " -y'
    output_opts = '-an \
    -filter_complex "\
    [0:v]trim=start=0:end=' + str(round(intro_length - overlay, 2)) + ',setpts=PTS-STARTPTS[firstclip]; \
    [1:v]colorbalance=' + cbopts + '[corrected]; \
    [corrected]trim=start=' + str(overlay) + ':end=' + str(video_end_sec - video_start_sec) + ',setpts=PTS-STARTPTS[secondclip]; \
    [0:v]trim=start=' + str(round(intro_length - overlay, 2)) + ':end=' + str(intro_length) + ',setpts=PTS-STARTPTS[fadeoutsrc]; \
    [1:v]colorbalance=' + cbopts + '[corrected]; \
    [corrected]trim=start=0:end=' + str(overlay) + ',setpts=PTS-STARTPTS[fadeinsrc]; \
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
                   global_options="-y",
                   inputs={intro_file_vid: None, input_video: input_opts},
                   outputs={'output.mp4': output_opts}
                   )
    print(video.cmd)
    video.run()
    # video.run_ffmpeg_command()
    print("Rendering Finished")


def preview(input_video="sample.mp4",video_start="00:01:00",
            amber_blue=0, green_magenta=0):

    video_start_sec = get_sec(video_start)
    rgb = ff_correction(amber_blue, green_magenta)
    r = str(rgb[0])
    g = str(rgb[1])
    b = str(rgb[2])
    cbopts = "rs=" + r + ":gs=" + g + ":bs=" + b
    cbopts += ":rm=" + r + ":gm=" + g + ":bm=" + b
    cbopts += ":rh=" + r + ":gh=" + g + ":bh=" + b
    input_opts = "-ss " + video_start
    output_opts = "-vframes 1 -vf colorbalance=" + cbopts
    frame = FFmpeg(executable="ffmpeg",
                   global_options="-y",
                   inputs={input_video: input_opts},
                   outputs={'output.bmp': output_opts}
                   )
    print(frame.cmd)
    frame.run()
