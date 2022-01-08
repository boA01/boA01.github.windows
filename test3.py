from PIL import Image

def Cal_S():
  im = Image.open("i1.png")

  i=0
  width, height = im.size
  print(width, height)

  for x in range(0, width, 5):
    for y in range(0, height, 5):
      if im.getpixel((x,y))==(250, 0, 0):
        i+=25
  return i/(width*height)

print(Cal_S())