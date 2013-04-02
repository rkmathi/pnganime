import Image
import ImageChops

def generate_diff(img1, img2):
    _img1 = Image.open(img1)
    _img2 = Image.open(img2)
    #return ImageChops.blend(_img1, _img2, 0.5)
    #return ImageChops.difference(_img1, _img2)
    bld = Image.blend(_img1, _img2, 0.5)
    return Image.composite(_img1, _img2, bld)


def image_name(path, num, digit):
    format = '%0' + str(digit) + 'd'
    filename = format % num
    return "%s%s.png" % (path, filename)


def create_diff(fst, end, cd, digit):
    for i in range(fst, end):
        diff = generate_diff(
            image_name(cd, i, digit),
            image_name(cd, i+1, digit))
        diff.convert('RGBA').save("result/%08d-%08d.png" % (i, i+1))


if __name__ == '__main__':
    create_diff(581, 730, "miku2/", 8)
