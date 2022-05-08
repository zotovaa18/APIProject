from moviepy.editor import *


def createvideo(str1):
    clips = []

    while True:
        try:
            str1.append((input()))
        except EOFError:
            break

    for filename in os.listdir('media/video'):
        veter = filename.replace('.', '')
        veter = veter.replace('mov', '')
        veter = veter.replace(veter[0], '')
        if veter in str1:
            clips.append(VideoFileClip(filename))
    video = concatenate_videoclips(clips, method='compose')
    video.write_videofile('media/video/ct_01.mp4')


def file_names():
    for filenames in os.listdir('media/video'):
        return filenames


file_names()
