def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    aaa = divmod(number, base)
    if aaa[0] == 0:
        return str(aaa[1])
    else:
        return int(str(dec_to_base(aaa[0], base)) + str(aaa[1]))
