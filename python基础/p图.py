from PIL import Image

def change_size(path, x = 295, y = 413):
    img = Image.open(path)
    out = img.resize((x, y), Image.ANTIALIAS)
    out.save("new.png")

