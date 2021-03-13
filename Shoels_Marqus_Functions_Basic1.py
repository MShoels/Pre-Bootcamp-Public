# 1 Prediction
def a():
    return 5
print(a()) // output will print 5

# 2 Prediction
def a():
    return 5
print(a()+a()) // output will print 10

# 3 Prediction
def a():
    return 5
    return 10
print(a()) // output will print 5

# 4 Prediction
def a():
    return 5
    print(10)
print(a())    // output will print 5

# 5 Prediction
def a():
    print(5)
x = a()
print(x) // output will print 5, None

# 6 Prediction
def a(b, c):
    print(b+c)
print(a(1, 2) + a(2, 3)) // output will print 3, 5

# 7 Prediction
def a(b, c):
    return str(b)+str(c)
print(a(2, 5)) // output will print 25

# 8 Prediction
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())      // output will print 100, 10

#9 Prediction
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))  // output will print 7, 14, 21

#10 Prediction
def a(b,c):
    return b+c
    return 10
print(a(3,5))  // output will print 8

#11 Prediction
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)   // output will print 500, 500, 300, 500

#12 Prediction
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)  // output will print 500, 500, 300, 500

#13 Prediction
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)    // output will print 500, 500, 300, 300

#14 Prediction
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()            // output will print 1, 3, 2

#15 Prediction
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)  // output will print 1, 3, 5, 10
