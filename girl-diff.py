import Image

Q = 256

def create_diff(fst, end, cd, digit):
    for cnt in range(fst, end):
        diff = generate_diff_img(
            __image_name(cd, cnt, digit),
            __image_name(cd, cnt+1, digit))
        diff.convert('RGBA').save("girl-diff/%03d.png" % (cnt))

        print("%d end!" % cnt)


def generate_diff_img(img1, img2):
    _img1 = Image.open(img1)
    _img2 = Image.open(img2)
    __img1 = _img1.load()
    __img2 = _img2.load()
    _ans = Image.new('RGBA', (_img1.size[0], _img1.size[1]))
    __ans = _ans.load()

    for x in range(_img1.size[0]):
        for y in range(_img1.size[1]):
            """
            if (((__img1[x, y][0] - __img2[x, y][0]) ** 2 +
                4 * (__img1[x, y][1] - __img2[x, y][1]) ** 2 +
                (__img1[x, y][2] - __img2[x, y][2]) ** 2) > Q):
            """
            if __img1[x, y] != __img2[x, y]:
                __ans[x, y] = __img2[x, y]

    return _ans


def __image_name(path, num, digit):
    format = '%0' + str(digit) + 'd'
    filename = format % num
    return "%s%s.png" % (path, filename)


if __name__ == '__main__':
    create_diff(200, 299, "girl_png/", 3)

    """
    img = generate_diff_img("miku2/00000581.png", "miku2/00000582.png")
    img.show()
    """