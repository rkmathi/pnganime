import sys
import Image

def __hdiff(img1, img2):
    _img1, _img2 = Image.open(img1), Image.open(img2)
    __img1, __img2 = _img1.load(), _img2.load()
    hdiff, ans, maxsame = {}, 0, 0

    #for h in range(-16, 17):
    for h in range(-5, 0):
        hdiff[h] = 0
        for x in range(_img1.size[0]):
            for y in range(_img1.size[1]):
                try:
                    if __img1[x, y] == __img2[x, y+h]:
                        hdiff[h] = hdiff[h] + 1
                except IndexError:
                    pass

    for k, v in hdiff.items():
        if v > maxsame:
            ans, maxsame  = k, v

    return ans


def __gen2diff(img1, img2):
    _img1, _img2 = Image.open(img1), Image.open(img2)
    __img1, __img2 = _img1.load(), _img2.load()
    _ans = Image.new('RGBA', (_img1.size[0], _img1.size[1]))
    __ans = _ans.load()
    _h = __hdiff(img1, img2)

    for x in range(_img1.size[0]):
        for y in range(_img1.size[1]):
            try:
                if __img1[x, y] != __img2[x, y+_h]:
                    __ans[x, y] = __img2[x, y]
            except IndexError:
                __ans[x, y] = __img2[x, y]

    return _ans


def create_diff(img1, img2, cd1, cd2, suffix):
    ans = __gen2diff(cd1+str(img1)+suffix, cd2+str(img2)+suffix)
    ans.convert('RGBA').save("%s%s-%s.png" % (sys.argv[5], img1, img2))


def create_all(fst, end, cd1, cd2, digit):
    d = str(0) * digit
    for i in range(fst, end):
        directory1 = "%s%s" % (cd1, d)
        directory2 = "%s%s" % (cd2, d)
        create_diff(i, i+1, directory1, directory2, ".png")
        print("%d end!" % i)


if __name__ == '__main__':
    create_all(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], 8)

    """
    key  = Image.open("miku2/00000582.png")
    back = Image.open("1-un-diff/000581_.png")
    fore = Image.open("1-un-comp/581-582.png")
    key.paste(back, (0, 0), back)
    key.paste(fore, (0, 0), fore)
    #key.show()
    key.convert('RGBA').save("hoge1.png")
    """