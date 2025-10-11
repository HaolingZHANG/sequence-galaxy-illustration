def add(a: str, b: str) \
        -> str:
    if not (a.isdigit() and b.isdigit()):
        raise ValueError("Inputs must be non-negative integer strings")

    i, j = len(a) - 1, len(b) - 1
    carry = 0
    out = []

    while i >= 0 or j >= 0 or carry:
        x = ord(a[i]) - 48 if i >= 0 else 0
        y = ord(b[j]) - 48 if j >= 0 else 0
        s = x + y + carry
        out.append(chr(48 + (s % 10)))
        carry = s // 10
        i -= 1
        j -= 1

    result = "".join(reversed(out))
    k = 0
    while k < len(result) - 1 and result[k] == "0":
        k += 1
    return result[k:]


def mul(a: str, b: str) \
        -> str:
    if not (isinstance(a, str) and isinstance(b, str)):
        raise TypeError("Inputs must be strings")
    if not (a.isdigit() and b.isdigit()):
        raise ValueError("Inputs must be non-negative integer strings")

    # strip leading zeros for normalization
    # noinspection PyShadowingNames
    def strip_leading_zeros(s: str) \
            -> str:
        i = 0
        while i < len(s) - 1 and s[i] == '0':
            i += 1
        return s[i:]

    a = strip_leading_zeros(a)
    b = strip_leading_zeros(b)

    # quick outs
    if a == "0" or b == "0":
        return "0"

    n, m = len(a), len(b)
    res = [0] * (n + m)

    for i in range(n - 1, -1, -1):
        ai = ord(a[i]) - 48
        carry = 0
        for j in range(m - 1, -1, -1):
            bj = ord(b[j]) - 48
            k = i + j + 1
            s = ai * bj + res[k] + carry
            res[k] = s % 10
            carry = s // 10
        res[i] += carry

    i = 0
    while i < len(res) - 1 and res[i] == 0:
        i += 1
    return "".join(chr(48 + d) for d in res[i:])


minimum_length = 26
maximum_length = 34000

count, current = "0", str(20 ** 25)
for length in range(minimum_length, maximum_length + 1):
    current = mul(current, "20")
    count = add(count, current)

print(len(count))  # 44236
