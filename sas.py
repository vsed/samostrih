from moviepy.editor import ImageClip, TextClip, CompositeVideoClip
import numpy


# Font size:

name_fontsize = 90
verse_fontsize = int(name_fontsize * 0.62)

# THIS IS INTRO SECTION:

# Image used as intro background:
intropic = "BCPlogonazev.png"

# Now we turn it into a 5 sec clip:
intro = ImageClip(intropic).set_duration("5")

# Name and verse of the sermon:
name = TextClip(txt="Bože, tys můj bůh!", font="Arial", fontsize=name_fontsize, color="gray15").set_duration("5")
verse = TextClip(txt="Žalm 63", font="Arial", fontsize=verse_fontsize, color="gray15").set_duration("5")

# Position of the name and verse text:
# Anchor is x and y coordinates of a point - under which the text will be drawn
anchor = (1342, 744)

# Position of the name calculations:
name_dimensions = name.size
name_offset = (name_dimensions[0] / 2, 0)
name_position = numpy.subtract(anchor, name_offset)

# Position of the verse, relative to the name position - centered:
verse_dimensions = verse.size
xoffset = int((name_dimensions[0] - verse_dimensions[0]) / 2)
yoffset = int(name_dimensions[1] + 30)
verse_offset = (xoffset, yoffset)
verse_position = numpy.add(name_position, verse_offset)

# print(offset)



result = CompositeVideoClip([intro, name.set_position(name_position), verse.set_position(verse_position)])

result.write_videofile("test.mp4", fps=29.97, ffmpeg_params=['-crf', '22'], codec='libx264')
# result.save_frame(filename='test.png')
