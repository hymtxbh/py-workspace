# Configurable variables. You may need to tweak these to be compatible with
# the server-side, but the defaults work in most cases.
from unicode_rightmove import unsigned_right_shitf
hexcase = 0;  # hex output format. 0 - lowercase; 1 - uppercase
b64pad = "";  # base-64 pad character. "=" for strict RFC compliance
chrsz = 8;  # bits per input character. 8 - ASCII; 16 - Unicode
intlenbit = 32  # intlen

hex_md5 = lambda s: binl2hex(core_md5(str2binl(s), len(s) * chrsz))

# Convert an array of little-endian words to a hex string.
def binl2hex(binarray):
    if hexcase == 1:
        hex_tab = "0123456789ABCDEF"
    else:
        hex_tab = "0123456789abcdef"
    str = ""
    i = 0
    while i < len(binarray) * 4:
        str += hex_tab[(binarray[i >> 2] >> ((i % 4) * 8 + 4)) & 0xF] + hex_tab[
            (binarray[i >> 2] >> ((i % 4) * 8)) & 0xF]
        i += 1
    return str


# Convert a string to an array of little-endian words
# If chrsz is ASCII, characters >255 have their hi-byte silently ignored.
def str2binl(str):
    bin = {}
    mask = (1 << chrsz) - 1
    i = 0
    while i < len(str) * chrsz:
        ind = i >> 5
        sdv = i % intlenbit
        str_c = ord(str[int(i / chrsz)]) & mask
        bin[ind] = bin.get(ind, 0) | str_c << sdv
        i += chrsz
    return bin


# Add integers, wrapping at 2^32. This uses 16-bit operations internally
def safe_add(x, y):
    lsw = (x & 0xFFFF) + (y & 0xFFFF)
    msw = (((x & (2 ** intlenbit - 1)) >> 16) + ((y & (2 ** intlenbit - 1)) >> 16) + (lsw >> 16)) & (2 ** intlenbit - 1)
    return ((msw << 16) | (lsw & 0xFFFF)) & (2 ** intlenbit - 1)


# Bitwise rotate a  number to the left.
rol = lambda num, cnt: \
    ((num << cnt % intlenbit) & (2 ** intlenbit - 1)) \
    | (((num & (2 ** intlenbit - 1)) >> (intlenbit - cnt % intlenbit)) & (2 ** intlenbit - 1))

# These functions implement the four basic operations the algorithm uses.
md5_cmn = lambda q, a, b, x, s, t: safe_add(rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
md5_ff = lambda a, b, c, d, x, s, t: md5_cmn((b & c) | ((~b) & d), a, b, x, s, t)
md5_gg = lambda a, b, c, d, x, s, t: md5_cmn((b & d) | (c & (~d)), a, b, x, s, t)
md5_hh = lambda a, b, c, d, x, s, t: md5_cmn(b ^ c ^ d, a, b, x, s, t)
md5_ii = lambda a, b, c, d, x, s, t: md5_cmn(c ^ (b | (~d)), a, b, x, s, t)


# Calculate the MD5 of an array of little-endian words, and a bit length
def core_md5(x, l):
    #  append padding
    x[l >> 5] |= 0x80 << ((l) % 32)
    x[(unsigned_right_shitf(l + 1, 9) << 4) + 14] = l  # todo 9 >>>
    a, b, c, d, i = 1732584193, -271733879, -1732584194, 271733878, 0

    while i < len(x):
        olda, oldb, oldc, oldd = a, b, c, d

        a = md5_ff(a, b, c, d, x.get(i + 0, 0), 7, -680876936)
        d = md5_ff(d, a, b, c, x.get(i + 1, 0), 12, -389564586)
        c = md5_ff(c, d, a, b, x.get(i + 2, 0), 17, 606105819)
        b = md5_ff(b, c, d, a, x.get(i + 3, 0), 22, -1044525330)
        a = md5_ff(a, b, c, d, x.get(i + 4, 0), 7, -176418897)
        d = md5_ff(d, a, b, c, x.get(i + 5, 0), 12, 1200080426)
        c = md5_ff(c, d, a, b, x.get(i + 6, 0), 17, -1473231341)
        b = md5_ff(b, c, d, a, x.get(i + 7, 0), 22, -45705983)
        a = md5_ff(a, b, c, d, x.get(i + 8, 0), 7, 1770035416)
        d = md5_ff(d, a, b, c, x.get(i + 9, 0), 12, -1958414417)
        c = md5_ff(c, d, a, b, x.get(i + 10, 0), 17, -42063)
        b = md5_ff(b, c, d, a, x.get(i + 11, 0), 22, -1990404162)
        a = md5_ff(a, b, c, d, x.get(i + 12, 0), 7, 1804603682)
        d = md5_ff(d, a, b, c, x.get(i + 13, 0), 12, -40341101)
        c = md5_ff(c, d, a, b, x.get(i + 14, 0), 17, -1502002290)
        b = md5_ff(b, c, d, a, x.get(i + 15, 0), 22, 1236535329)

        a = md5_gg(a, b, c, d, x.get(i + 1, 0), 5, -165796510)
        d = md5_gg(d, a, b, c, x.get(i + 6, 0), 9, -1069501632)
        c = md5_gg(c, d, a, b, x.get(i + 11, 0), 14, 643717713)
        b = md5_gg(b, c, d, a, x.get(i + 0, 0), 20, -373897302)
        a = md5_gg(a, b, c, d, x.get(i + 5, 0), 5, -701558691)
        d = md5_gg(d, a, b, c, x.get(i + 10, 0), 9, 38016083)
        c = md5_gg(c, d, a, b, x.get(i + 15, 0), 14, -660478335)
        b = md5_gg(b, c, d, a, x.get(i + 4, 0), 20, -405537848)
        a = md5_gg(a, b, c, d, x.get(i + 9, 0), 5, 568446438)
        d = md5_gg(d, a, b, c, x.get(i + 14, 0), 9, -1019803690)
        c = md5_gg(c, d, a, b, x.get(i + 3, 0), 14, -187363961)
        b = md5_gg(b, c, d, a, x.get(i + 8, 0), 20, 1163531501)
        a = md5_gg(a, b, c, d, x.get(i + 13, 0), 5, -1444681467)
        d = md5_gg(d, a, b, c, x.get(i + 2, 0), 9, -51403784)
        c = md5_gg(c, d, a, b, x.get(i + 7, 0), 14, 1735328473)
        b = md5_gg(b, c, d, a, x.get(i + 12, 0), 20, -1926607734)

        a = md5_hh(a, b, c, d, x.get(i + 5, 0), 4, -378558)
        d = md5_hh(d, a, b, c, x.get(i + 8, 0), 11, -2022574463)
        c = md5_hh(c, d, a, b, x.get(i + 11, 0), 16, 1839030562)
        b = md5_hh(b, c, d, a, x.get(i + 14, 0), 23, -35309556)
        a = md5_hh(a, b, c, d, x.get(i + 1, 0), 4, -1530992060)
        d = md5_hh(d, a, b, c, x.get(i + 4, 0), 11, 1272893353)
        c = md5_hh(c, d, a, b, x.get(i + 7, 0), 16, -155497632)
        b = md5_hh(b, c, d, a, x.get(i + 10, 0), 23, -1094730640)
        a = md5_hh(a, b, c, d, x.get(i + 13, 0), 4, 681279174)
        d = md5_hh(d, a, b, c, x.get(i + 0, 0), 11, -358537222)
        c = md5_hh(c, d, a, b, x.get(i + 3, 0), 16, -722521979)
        b = md5_hh(b, c, d, a, x.get(i + 6, 0), 23, 76029189)
        a = md5_hh(a, b, c, d, x.get(i + 9, 0), 4, -640364487)
        d = md5_hh(d, a, b, c, x.get(i + 12, 0), 11, -421815835)
        c = md5_hh(c, d, a, b, x.get(i + 15, 0), 16, 530742520)
        b = md5_hh(b, c, d, a, x.get(i + 2, 0), 23, -995338651)

        a = md5_ii(a, b, c, d, x.get(i + 0, 0), 6, -198630844)
        d = md5_ii(d, a, b, c, x.get(i + 7, 0), 10, 1126891415)
        c = md5_ii(c, d, a, b, x.get(i + 14, 0), 15, -1416354905)
        b = md5_ii(b, c, d, a, x.get(i + 5, 0), 21, -57434055)
        a = md5_ii(a, b, c, d, x.get(i + 12, 0), 6, 1700485571)
        d = md5_ii(d, a, b, c, x.get(i + 3, 0), 10, -1894986606)
        c = md5_ii(c, d, a, b, x.get(i + 10, 0), 15, -1051523)
        b = md5_ii(b, c, d, a, x.get(i + 1, 0), 21, -2054922799)
        a = md5_ii(a, b, c, d, x.get(i + 8, 0), 6, 1873313359)
        d = md5_ii(d, a, b, c, x.get(i + 15, 0), 10, -30611744)
        c = md5_ii(c, d, a, b, x.get(i + 6, 0), 15, -1560198380)
        b = md5_ii(b, c, d, a, x.get(i + 13, 0), 21, 1309151649)
        a = md5_ii(a, b, c, d, x.get(i + 4, 0), 6, -145523070)
        d = md5_ii(d, a, b, c, x.get(i + 11, 0), 10, -1120210379)
        c = md5_ii(c, d, a, b, x.get(i + 2, 0), 15, 718787259)
        b = md5_ii(b, c, d, a, x.get(i + 9, 0), 21, -343485551)

        a, b, c, d = safe_add(a, olda), safe_add(b, oldb), safe_add(c, oldc), safe_add(d, oldd)
        i += 16

    return {0: a, 1: b, 2: c, 3: d}


sArr = ["123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"];
# test md5 abc === "900150983cd24fb0d6963f7d28e17f72"

for s in sArr:
    print(hex_md5(s))
