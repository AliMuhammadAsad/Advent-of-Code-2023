data = list(open('inp11.txt').read().splitlines())
cols = set()
rows = set()
gals = []
for (yy, row) in enumerate(data):
    for (xx, ch) in enumerate(row):
        if ch == '#':
            cols.add(xx)
            rows.add(yy)
            gals.append((xx, yy))

for age in (2, 1000000):
    tot = 0
    for ii in range(len(gals)):
        for jj in range(ii + 1, len(gals)):
            x1, y1 = gals[ii]
            x2, y2 = gals[jj]
            
            xs = set(range(min(x1, x2), max(x1, x2)))
            d = len(xs - cols) * age + len(xs & cols)
            ys = set(range(min(y1, y2), max(y1, y2)))
            d += len(ys - rows) * age  + len(ys & rows)
            tot+=d
    print(tot)