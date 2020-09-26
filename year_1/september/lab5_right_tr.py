# Defend

x1, y1 = map(int, input(">>> x1, y1 (int, int): ").split())
x2, y2 = map(int, input(">>> x2, y2 (int, int): ").split())
x3, y3 = map(int, input(">>> x3, y3 (int, int): ").split())

v1, v2, v3 = (x1, y1, "v1"), (x2, y2, "v2"), (x3, y3, "v3")
vertices = (v1, v2, v3)

# sides as vectors:
#       x:int,     y:int
# begin function v_new
point1, point2 = v1, v2
res = (point1[0] - point2[0], point1[1] - point2[1], (point1, point2))
# end function
s1 = res
# begin function v_new
point1, point2 = v3, v1
res = (point1[0] - point2[0], point1[1] - point2[1], (point1, point2))
# end function
s2 = res
# begin function v_new
point1, point2 = v2, v3
res = (point1[0] - point2[0], point1[1] - point2[1], (point1, point2))
# end function
s3 = res

s1 = (s1[0] ** 2 + s1[1] ** 2) ** 0.5
s2 = (s2[0] ** 2 + s2[1] ** 2) ** 0.5
s3 = (s3[0] ** 2 + s3[1] ** 2) ** 0.5
if (
    (s1 ** 2 + s2 ** 2 - s3 ** 2) < 10e-8
    or (s2 ** 2 + s3 ** 2 - s1 ** 2) < 10e-8
    or (s1 ** 2 + s3 ** 2 - s2 ** 2) < 10e-8
):
    print("Triangle is right!")
else:
    print("Triangle is wrong!")
