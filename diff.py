import Image

def create_diff(fst, end, cd, digit):
    for i, cnt in enumerate(range(fst, end)):
        if cnt % 10 == 0:
            diff = generate_diff_img(
                __image_name(cd, cnt, digit),
                __image_name(cd, cnt+1, digit))
            diff.convert('RGBA').save("result/%06d_.png" % (cnt))
            orig = Image.open(__image_name(cd, cnt, digit))
            orig.convert('RGBA').save("result/%06d.png" % (cnt))
        else:
            diff = generate_diff_img(
                __image_name(cd, cnt, digit),
                __image_name(cd, cnt+1, digit))
            diff.convert('RGBA').save("result/%06d_.png" % (cnt))


def generate_diff_img(img1, img2):
    _img1 = Image.open(img1)
    _img2 = Image.open(img2)
    __img1 = _img1.load()
    __img2 = _img2.load()
    _ans = Image.new('RGBA', (_img1.size[0], _img1.size[1]))
    __ans = _ans.load()

    for x in range(_img1.size[0]):
        for y in range(_img1.size[1]):
            if __img1[x, y] != __img2[x, y]:
                __ans[x, y] = __img2[x, y]

    return _ans


def __image_name(path, num, digit):
    format = '%0' + str(digit) + 'd'
    filename = format % num
    return "%s%s.png" % (path, filename)


if __name__ == '__main__':
    #img = generate_diff_img("miku2/00000581.png", "miku2/00000582.png")
    #img.show()
    create_diff(581, 731, "miku2/", 8)
