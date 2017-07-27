def perfectCity(departure, destination):
    final = 0
    cf = []
    df = []
    a = [e for e in departure if isinstance(e, int)]
    b = [e for e in destination if isinstance(e, int)]
    c = [e for e in departure if isinstance(e, float)]
    d = [e for e in destination if isinstance(e, float)]
    print(a)
    print(b)
    print(c)
    print(d)
    if c[0] < 1.0:
        cf.append(1 - c[0])
        i = True
        k = 0
    else:
        cf.append(c[0])
        k = abs(round(c[0] - c[0]))
        i = False
    if d[0] < 1.0:
        df.append(round(1 - d[0],1))
        j = True
        l = 0
    else:
        df.append(d[0])
        l = abs(round(d[0] - d[0]))
        j = False
    print(cf)
    print(df)
    print(abs(a[0]-b[0]))
    print(abs(cf[0] + df[0]))
    print(abs(a[0] - b[0]) + abs(cf[0] + df[0]))
    print(abs(a[0] -  b[0]) + abs(cf[0] + df[0]))
    if i and j:
        if (cf[0] + df[0] < c[0] + d[0]):
            if (k > 0 and l > 0) and (k + l < c[0] + d[0]):
                final = abs(a[0] -  b[0]) + abs(cf[0] - df[0])
            else:
                final = abs(a[0] -  b[0]) + abs(cf[0] + df[0])
        else:
            final = abs(a[0] - b[0]) + abs(c[0] + d[0])
    else:
        final = abs(a[0] - b[0]) + abs(c[0] - d[0])
    return final


