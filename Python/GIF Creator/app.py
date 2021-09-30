from moviepy.editor import *

clip = (VideoFileClip("Python/GIF Creator/video.mp4"))
# For user size and start-end time use below syntex
# clip = (VideoFileClip("PATH NAME").subclip((START TIME),(END TIME)) .resize(ACCORDING TO THE USER WISH)) 
clip.write_gif("Python/GIF Creator/output.gif")