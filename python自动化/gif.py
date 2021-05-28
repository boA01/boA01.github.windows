import os
import imageio

path = os.getcwd()
png_list =list(i for i in os.listdir() if i[-3:]=='png')

png_list.sort(key = lambda x: x[:-4])

for png in png_list:
    image_path = os.path.join(path, png)
    frames.append(imageio.imread(image_path))

gif_path = os.path.join(path,"new.gif")
imageio.mimsave(gif_path, frames, "GIF", duration=DURATION)
