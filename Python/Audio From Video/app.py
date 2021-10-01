# this file can converts video to audio
import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"Python/Audio From Video/Video.mp4")
my_clip.audio.write_audiofile(r"Python/Audio From Video/Output.mp3")
