#region 18119(кегэ)
# def f(n):
#     s = ''
#     while n != 0:
#         s = str(n%3) + s
#         n = n//3
#     return s
# def tsum(q):
#     qsum = 0
#     for i in range(0,len(q)):
#         qsum = int(q[i]) + qsum
#     if qsum%2 == 0:
#         q = '1' + q + '2'
#     else:
#         q = '2' + q + '0'
#     d = int(q, 3)
#     return d
# a = list()
# for i in range(1, 200):
#     res = tsum(f(i))
#     if res>100:
#         a.append(res)
# print(min(a))
#enfregion
#region 18040(кегэ)
# def f(n):
#     dubl_n = n
#     s = ''
#     while n != 0:
#         s = str(n%2) + s
#         n = n//2
#     if dubl_n % 5 == 0:
#         s = s[:3] + s
#     else:
#         s = s + bin(dubl_n%5 * 5)[2:]
#     return int(s, 2)
# for i in range(1, 100000, 2):
#     fi = f(i)
#     if fi < 313:
#         print(i, '   ', fi)
#endregion
#region 17765(кегэ)
# print('x y z w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if not((x == ( w or y)) or ((w <= z ) and (y <= w))):
#                     print(x, y, z, w)
#endregion
#region 13362(из решуегэ)
# x = 125 + 25**3 + 5**9
# print('x =', x)
# def tofive(n):
#     s = ''
#     while n != 0:
#         s = str(n%5) + s
#         n = n//5
#     return s
# f = tofive(x)
# print(f)
# print(f.count('0'))
#endregion
#region 13745(из решуегэ)
# def f(x, y, A):
#     return ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))
# for A in range(300):
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag:
#         print(A)
#endregion
#region 59756(поехали 15 из решуегэ)
# def f(x, y, A):
#     return (x < A) or (y < A) or (y > x - 5) or(y < 2 * x - 15)
# for A in range(500):
#     flag = True
#     for x in range(500):
#         for y in range(500):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag:
#         print(A)
#endregion
#region 34545(решуегэ)
# def f(x, A):
#     return (not(x == A) and (32 <= x <= 92)) <= (12 <= x <= 62)
# amass = list()
# for A in range(1):
#     flag = True
#     for x in range(32, 100):
#         if not(f(x, A)):
#             flag = False
#     if flag:
#         amass.append(A)
#     else:
#         amass.append('')
# print(amass) hueta
#endregion
#region тот же номер^
# s = []
# for amin in range(1,100):
#     for amax in range(1,100):
#         flag = True
#         for x in range(1,100):
#             if ((not(amin <= x <= amax) and (32 <= x <= 92)) <= (12 <= x <= 62))==0:
#                 flag = False
#                 break
#         if flag:
#             s.append(amax-amin+1)
# print(min(s)) zaebis'
#endregion
#region Сашино творенье
# def diz(a,b):
#     s = ''
#     for i in range(len(a)):
#         s = str(bool(a[i]) and bool(b[i])) + s
#     return s
#
# a = bin(14)[2:]
# b = bin(5)[2:]
# alen = len(a)
# blen = len(b)
# diff = abs(alen-blen)
# if (alen > blen):
#     for i in range(diff):
#         b = '0'+b
# else:
#     for i in range(diff):
#         a = '0'+a
# print(diz(a,b))
#endregion
#region какой-то номер
# def f(x, y, A):
#     return (x < A) or (y < A) or (y > x - 5) or(y < 2 * x - 15)
# for A in range(500):
#     flag = True
#     for x in range(500):
#         for y in range(500):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag:
#         print(A)
#endregion
#region 61361(решуегэ)
# def f(x, y, A):
#     return (x + 2 * y > 48) or (y > x) or (x + 3 * y < A)
# for A in range(300):
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag == False:
#         print(A)
#endregion
#region 34546(решуегэ)
# s = []
# for amin in range(1,100):
#     for amax in range(amin, 100):
#         flag = True
#         for x in range(100):
#             if not(((23 <= x <= 58) or (amin <= x <= amax)) <= ((1 <= x <= 39) or (amin <= x <= amax))):
#                 flag = False
#                 break
#         if flag:
#             s.append(amax-amin+1)
# print(min(s))
#endregion
#region 64900(решуегэ)
# def f(x, A):
#     l1 = x & 20777 != 0
#     l2 = x & 12332 == 0
#     l3 = x & A != 0
#     return l1 <= (l2 <= l3)
# for A in range(10**5):
#     flag = True
#     for x in range(10**5):
#         if not f(x, A):
#             flag = False
#     if flag:
#         print(A)
#         break
#endregion
#region 59756(решуегэ)
# def f(x, y, A):
#     return (x < A) or (y < A) or (y > x - 5) or (y < 2 * x - 15)
# for A in range(300):
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag:
#         print(A)
#endregion
#29.01
#region 19247(кегэ)
# def f(x, y, A):
#     return (x - 3 * y < A) or (y > 400) or (x > 56)
# for A in range(300):
#     flag = True
#     for x in range(1, 300):
#         for y in range(1, 300):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag == True:
#         print(A)
#         break
#endregion
#region 18971(kege)
# def f(x, y, A):
#     return (y > 10) or (x * A > y + x) == 1
# for A in range(10000):
#     flag = True
#     for x in range(1,300):
#         for y in range(1,300):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag:
#         print(A)
#         break
#endregion
#region 18930(kege)
# from pickletools import long1
#
# s = []
# for amin in range(1, 6000):
#     for amax in range(amin, 6000):
#         flag = True
#         for x in range(6000):
#             if not((160 <= x <= 250) <= (10 <= x <= 150) or (not(amin <= x <= amax) <= (240 <= x <= 300))):
#                 flag = False
#                 break
#         if flag:
#             s.append(amax - amin + 1)
# print(min(s))
###залупня ебаная
#endregion
#region 18266 (kege) x&57=0 ∨(x&23=0→¬(x&A=0))
def f(x, A):
    l1 = x & 57 == 0
    l2 = x & 23 == 0
    l3 = x & A != 0
    return l1 or (l2 <= l3)
for A in range(300):
    flag = True
    for x in range(1000):
        if not(f(x,A)):
            flag = False
    if flag:
        print(A)
        break