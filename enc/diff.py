""" diff.py

Generate a image from two difference sequential images.

Usage:
    $ python diff.py 0 100 8 miku-in miku-out 128
"""

import sys
import Image

Q = int(sys.argv[6])

def create_diff(fst, end, digit, idir, odir):
    for cnt in range(fst, end):
        diff = generate_diff_img(
            __image_name(idir, cnt, digit),
            __image_name(idir, cnt+1, digit)
        )
        diff.convert('RGBA').save(__image_name(odir, cnt, digit))
        print("%d end!" % cnt)


def generate_diff_img(img1, img2):
    _img1, _img2 = Image.open(img1), Image.open(img2)
    __img1, __img2 = _img1.load(), _img2.load()
    _ans = Image.new('RGBA', (_img1.size[0], _img1.size[1]))
    __ans = _ans.load()

    for x in range(_img1.size[0]):
        for y in range(_img1.size[1]):
            if (((__img1[x, y][0] - __img2[x, y][0]) ** 2 +
               4 * (__img1[x, y][1] - __img2[x, y][1]) ** 2 +
               (__img1[x, y][2] - __img2[x, y][2]) ** 2) >
               Q
            ):
                __ans[x, y] = __img2[x, y]
            else:
                __ans[x, y] = (128, 128, 128, 0)

    return _ans


def __image_name(path, num, digit):
    format = '%0' + str(digit) + 'd'
    filename = format % num
    return "%s/%s.png" % (path, filename)


if __name__ == '__main__':
    create_diff(
        int(sys.argv[1]),   # start name num
        int(sys.argv[2]),   # end name num
        int(sys.argv[3]),   # digit
        sys.argv[4],        # input directory
        sys.argv[5]         # output directory
    )
