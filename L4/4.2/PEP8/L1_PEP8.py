import math
import unittest


def calculate_sd(d):
    m = calculate_mean(d)
    v = sum([((i - m) ** 2) for i in d]) / len(d)
    return v ** 0.5


def calculate_mean(n):
    return sum(n)/len(n)


def calculate_median(d):
    d.sort()
    n = len(d)
    if n % 2 == 0:
        m1 = d[n//2]
        m2 = d[n//2 - 1]
        m = (m1 + m2)/2
    else:
        m = d[n//2]
    return str(m)


def calculate_quartile(d, q):
    d.sort()
    if(q == 1):
        lm = int(round((len(d) + 1) / 4.0) - 1)
        lq = d[lm]
        return lq
    if(q == 2):
        return calculate_median(d)
    if(q == 3):
        try:
            hm = (len(d) - 1) * 0.75
            uq = d[hm]
            return uq
        except TypeError:
            ceil = int(math.ceil(hm))
            floor = int(math.floor(hm))
            uq = (d[ceil] + d[floor]) / 2
            return uq


def calculate_percentile(d, p, key=lambda x: x):
    d.sort()
    k = (len(d)-1) * p
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(d[int(k)])
    pp0 = key(d[int(f)]) * (c-k)
    pp1 = key(d[int(c)]) * (k-f)
    return pp0+pp1


def convertTo_Roman(n):
    if (n < 1):
        return None
    else:
        romanos = ["I", "IV", "V",
                   "IX", "X", "XL",
                   "L", "XC", "C",
                   "CD", "D", "CM",
                   "M"
                   ]
        decimales = [1, 4, 5,
                     9, 10, 40,
                     50, 90, 100,
                     400, 500, 900,
                     1000
                     ]
        r = []
        itera = 12
        while n:
            d = n // decimales[itera]
            n %= decimales[itera]
            while d:
                r.append(romanos[itera])
                d -= 1
            itera -= 1
        return r


class My_tests(unittest.TestCase):
    data = [1880, 9914, 5528, 4723, 2391, 4551, 8623, 9827,
            3084, 618, 4176, 3621, 5736, 7045, 7208, 2281,
            7243, 5924, 8083, 3234, 6329, 9100, 6648, 5793,
            118, 6587, 1602, 2671, 7934, 9599, 7470, 3952,
            4655, 5911, 4960, 4094, 7628, 2197, 7539, 9677,
            5980, 8893, 3996, 8506, 2394, 3878, 3570, 5102,
            2592, 4216, 6094, 6428, 8218, 6442, 22, 1239, 1329,
            1890, 5971, 5005, 3017, 6068, 3793, 8516,
            1704, 8612, 1799, 7570, 8573, 2596, 3261, 5036,
            3084, 8389, 3417, 5529, 3176, 8680, 4820, 9513,
            6956, 9925, 8161, 6512, 4462, 4993, 6835, 7589,
            3744, 8090, 9415, 7266, 7304, 8924, 6049, 1400,
            974, 5351, 2888, 2072, 1968, 2228, 643, 4688, 8559,
            9520, 1281, 6468, 7903, 1188, 8281, 250, 3227, 9948,
            3093, 6592, 6108, 389, 404, 675, 9485, 8663, 2220,
            8341, 7233, 7143, 4691, 8515, 7685, 7557, 7505, 8193,
            5845, 6418, 6567, 4749, 2025, 2056, 3283, 9230, 4739,
            4247, 256, 7381, 8409, 3754, 7497, 9650, 2157, 6929,
            7029, 2241, 8421, 5755, 3265, 4580, 6164, 827, 8763,
            5487, 6815, 1710, 3179, 8233, 456, 6374, 8124, 9118,
            2660, 1950, 6585, 7101, 8697, 3922, 8850, 9136, 9292,
            8734, 7146, 1968, 2688, 4698, 4299, 258, 9309, 6497,
            8184, 8162, 6389, 2567, 9396, 5664, 7143, 7457, 4676,
            6819, 6042, 4392, 1769, 1691, 2078, 2499, 4807, 2259,
            1428, 5162, 1951, 1337
            ]

    def test_convertTo_Roman(self):
        res = convertTo_Roman(320)
        self.assertEqual("CCCXX", "".join(res))

    def test_convertTo_Roman_fail(self):
        res = convertTo_Roman(-200)
        self.assertEqual(None, res)

    def test_calculate_mean(self):
        res = calculate_mean(self.data)
        self.assertEqual(True, (res > 5000 and res < 6000))

    def test_calculate_percentile(self):
        m = calculate_median(self.data)
        res = calculate_percentile(self.data, 0.75)
        self.assertTrue(float(res) > float(m))

    def test_calculate_percentile_fail(self):
        m = calculate_median(self.data)
        res = calculate_percentile(self.data, 0.75)
        self.assertFalse(float(res) < float(m))

    def test_calculate_sd(self):
        res = calculate_sd(self.data)
        self.assertTrue(float(res) < 3000 and float(res) > 2000)

    def test_calculate_quartile_1(self):
        m = calculate_median(self.data)
        res = calculate_quartile(self.data, 1)
        self.assertTrue(float(res) < float(m))

    def test_calculate_quartile_2(self):
        m = calculate_median(self.data)
        res = calculate_quartile(self.data, 2)
        self.assertTrue(float(res) == float(m))

    def test_calculate_quartile_3(self):
        m = calculate_median(self.data)
        res = calculate_quartile(self.data, 3)
        self.assertTrue(float(res) > float(m))

if __name__ == '__main__':
    unittest.main()