def test(a,b):
    print(id(a))
    a = a+a#表示的是 a = [11,22] + [11,22],即a指向了一个新的[11,22,11,22]的地址
    #a += a#表示：直接对a指向的[11,22]进行修改，即a还是指向原来的地方，但是原来的地方里的内容变为[11,22,11,22]
    print(id(a))

'''
A = 100
B = 200

print(id(A))
test(A,B)
print(A)
'''


A = [11,22]
print(id(A))
test(A,33)
print(A)
