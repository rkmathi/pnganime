import Image

def __diff(img1, img2):
    _img1, _img2 = Image.open(img1), Image.open(img2)
    __img1, __img2 = _img1.load(), _img2.load()
    wdiff, hdiff, wans, hans, wsame, hsame = {}, {}, 0, 0, 0, 0

    for w in range(-3, 8):
        wdiff[w] = 0
        for h in range(-10, 10):
            hdiff[h] = 0
            for x in range(_img1.size[0]):
                for y in range(_img1.size[1]):
                    try:
                        if __img1[x, y] == __img2[x+w, y+h]:
                            wdiff[w] = wdiff[w] + 1
                            hdiff[h] = hdiff[h] + 1
                    except IndexError:
                        pass

    for k, v in wdiff.items():
        if v > wsame:
            wans, wsame  = k, v
    for k, v in hdiff.items():
        if v > hsame:
            hans, hsame  = k, v

    print(wans, hans)
    return (wans, hans)


def __gen2diff(img1, img2):
    _img1, _img2 = Image.open(img1), Image.open(img2)
    __img1, __img2 = _img1.load(), _img2.load()
    _ans = Image.new('RGBA', (_img1.size[0], _img1.size[1]))
    __ans = _ans.load()
    _w, _h = __diff(img1, img2)

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
    ans.convert('RGBA').save("girl-comp/%s-%s.png" % (img1, img2))


def create_all(fst, end, cd1, cd2, digit):
    d = str(0) * digit
    for i in range(fst, end):
        directory1 = "%s%s" % (cd1, d)
        directory2 = "%s%s" % (cd2, d)
        create_diff(i, i+1, directory1, directory2, ".png")
        print("%d end!" % i)


if __name__ == '__main__':
    create_all(200, 300, "girl_png/", "girl-diff/", 0)
