import pygame
import sys
import os
import cv2
import glob

#Work in progress...
class Video:

    def __init__(self, name, size):
        self.name = name
        self.count = 0

        try:
            os.mkdir("pngs")
        except:
            files = glob.glob('pngs')
            for f in files:
                os.remove(f)

    def make_frame(self, screen):
        self.count += 1

        pygame.image.save(screen, "pngs\\" + self.name + "%08d.png"%self.count)

        
    def make_mp4(self):
        
        frames_path = os.listdir("pngs")

        frames = []

        for frame_path in frames_path:
            frames.append("pngs\\" + frame_path)

        video = cv2.VideoWriter("video", fourcc="mp4v",fps= 60, frameSize=[1920, 1080])

        for i in range(len(frames)):
            video.write(cv2.imread(frames[i]))

        video.release()
if __name__  == '__main__':
    video = Video((1920,1080))
    video.make_mp4()
        