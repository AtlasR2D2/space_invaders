def Intersect(lst1, lst2):
    """Takes two lists of 2 tuples containing two elements to represent area coordinates and
    identifies whether there is an intersection"""
    outerlst_1_len = len(lst1)
    outerlst_2_len = len(lst2)

    if outerlst_1_len != outerlst_2_len:
        blnIntersect = False
    else:

        blnIntersect = True
        for i in range(outerlst_1_len):
            if blnIntersect:
                rng1 = lst1[i]
                rng2 = lst2[i]

                if rng1[0] > rng2[0]:
                    LBound_max = rng1[0]
                else:
                    LBound_max = rng1[1]
                if rng1[1] < rng2[1]:
                    UBound_min = rng1[1]
                else:
                    UBound_min = rng2[1]
                # Check both values sit in both ranges
                if float(rng1[0]) <= LBound_max <= float(rng1[1]) and float(rng1[0]) <= UBound_min <= float(rng1[1]) and \
                    float(rng2[0]) <= LBound_max <= float(rng2[1]) and float(rng2[0]) <= UBound_min <= float(rng2[1]):
                    blnIntersect = True
                else:
                    blnIntersect = False
            else:
                pass
    # if blnIntersect:
    #     print(lst1)
    #     print(lst2)
    return blnIntersect
