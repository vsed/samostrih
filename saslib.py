def rgb_correction(ab=50, gm=50):
    """
    Returns RGB array for color correction as a tuple.
    It is meant to be used as an image which
    overlays treated picure - still or motion.



    :param ab: Amber/Blue balance, aka warm/cold
                value 0-100
                0 = warmest
                100 = coldest

    :param gm: Green/Magenta balance
                value 0-100
                0 = greenest
                100 = "magentest"
    """
    a = (1, 0.75, 0)
    b = (0, 0, 1)
    g = (0, 1, 0)
    m = (1, 0, 1)

    zero = np.array((0, 0, 0))
    ones = np.array((1, 1, 1))

    warm = zero
    cold = zero
    green = zero
    magenta = zero
    ab_res = zero
    gm_res = zero

    if ab != 50:
        abx = abs(50 - ab) / 2
        if ab > 50:
            warm = np.multiply(a, abx * 5.1)
            ab_res = warm
        else:
            cold = np.multiply(b, abx * 5.1)
            ab_res = cold

    if gm != 50:
        gmx = abs(50 - gm) / 2
        if gm > 50:
            gm -= 50
            green = np.multiply(g, gmx * 5.1)
            gm_res = green
        else:
            magenta = np.multiply(m, gmx * 5.1)
            gm_res = magenta

    basic = np.add(ab_res, gm_res)
    print("basic: ", basic)
    print("gm: ", gm_res, "ab: ", ab_res)
    multiplicator = 255 / np.max(basic)
    if multiplicator <= 0 or multiplicator > 255:
        multiplicator = 1
    print("multiplicator: ", multiplicator)
    data = np.multiply(basic, multiplicator)
    preresult = np.ndarray.tolist(data.astype(int))
    # result = tuple(chain.from_iterable(preresult))
    print("preresult: ", preresult)
    result = tuple(preresult)
    magnitude = 1 / multiplicator / 2
    if ab == 50 and gm == 50:
        magnitude = 0
    return result, magnitude
