a = ["박주하", "잠수", "문재성"]
a[0] = "한재성"

print(a)

b = ["박주하", "잠수", "문재성"]
b[0:2] = ["김정현", "Stopmotion Man"]

print(b)

c = ["박주하", "잠수", "문재성"]
c[0:2] = []

print(c)

d = ["박주하", "잠수", "문재성"]
del d[0]

print(d)

e = ["박주하", "잠수", "문재성"]
e.append("시우버")

print(e)