import sys
import Image

if __name__ == "__main__":
    for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
        img = Image.open("%s/%08d.bmp" % (sys.argv[3], i))
        img.convert('RGBA').save("%s/%03d.png" % (sys.argv[4], i))