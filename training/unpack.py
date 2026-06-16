#Given `t = (1, 2, 3, 4, 5)`, unpack it into variables a, b, *rest.

t = (1, 2, 3, 4, 5)

a, b, *rest = t

print("a =", a)
print("b =", b)
print("rest =", rest)

#Answer:
# a = 1
# b = 2
# rest = [3, 4, 5]