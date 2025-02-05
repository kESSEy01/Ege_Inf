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

# region 34546(решуегэ)
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

#region 18266 (kege)
# def f(x, A):
#     l1 = x & 57 == 0
#     l2 = x & 23 == 0
#     l3 = x & A != 0
#     return l1 or (l2 <= l3)
# for A in range(300):
#     flag = True
#     for x in range(1000):
#         if not(f(x,A)):
#             flag = False
#     if flag:
#         print(A)
#         break
#endregion

#region 18175 (kege)
# def f(x,A):
#     l1 = x%7 != 0
#     l2 = x%13 == 0
#     l3 = x > A - 40
#     return ((l1 and l2) <= l3) == 1
# for A in range(500):
#     flag = True
#     for x in range(1000):
#         if not(f(x, A)):
#             flag = False
#     if flag:
#         print(f"FRIENDLY THUG {A} NGG")
#endregion

#region хз
# def f(x, y, A):
#     return (x - y >= 39) or (y <= x) or (y >= A - 20)
# for A in range(100):
#     flag = True
#     for x in range(1,300):
#         if not(flag):
#             break
#         for y in range(1,300):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag:
#         print(A)
#endregion

#region 18044 (kege)
# def f(x, amin, amax):
#     l1 = 32 <= x <= 68
#     l2 = 54 <= x <= 76
#     l3 = not(amin <= x <= amax)
#     return not(l1 or l2) == l3
# s = []
# for amin in range(300):
#     for amax in range(amin, 300):
#         flag = True
#         for i in range(-1000,1000):
#             x = i/2
#             if not(f(x, amin, amax)):
#                 flag = False
#         if flag:
#             print(amax-amin+1)
#             s.append(amax-amin+1)
# print(min(s))
#endregion

#region 17528 (kege)
# def f(x, amin, amax):
#     l1 = amin <= x <= amax
#     l2 = 75 <= x <= 118
#     l3 = 25 <= x <= 73
#     return (l1 and not(l2)) <= (l3 or l2)
# s = []
# for amin in range(500):
#     for amax in range(amin, 500):
#         flag = True
#         for x in range(500):
#             if not(f(x, amin, amax)):
#                 flag = False
#         if flag:
#             s.append(amax-amin)
# print(max(s))
#endregion

#region 34546 (kege)
# def f(x, A):
#     l1 = x%A != 0
#     l2 = x%14 == 0
#     l3 = x%4 != 0
#     return l1 <= (l2 <= l3)
# for A in range(1, 300):
#     flag = True
#     for x in range(1, 30000):
#         if not(f(x, A)):
#             flag = False
#     if flag:
#         print(A)
#endregion

#region 16262 (kege)
# def f(x, y, A):
#     return ((A < x) or (x**2 - 7 * x + 10 > 0)) and ((A >= y) or (y**2 + 7 * y + 12 > 0))
# s = 0
# for A in range(-300,300):
#     flag = True
#     for x in range(-500, 500):
#         if not(flag):
#             break
#         for y in range(-500, 500):
#             if not(f(x, y, A)):
#                 flag = False
#     if flag:
#         s+=1
#         print(s)
#endregion

#region 15330 (kege) (x∈C)→((¬(x∈A)∧(x∈B))→¬(x∈C))
# def f(x, amin, amax):
#     l1 = 47 <= x <= 115
#     l2 = not(amin <= x <= amax)
#     l3 = 24 <= x <= 90
#     l4 = not(l1)
#     return l1 <= ((l2 and l3) <= l4)
# s = []
# for amin in range(300):
#     for amax in range(amin, 300):
#         flag = True
#         for x in range(-1000, 1000):
#             if not(f(x, amin, amax)):
#                 flag = False
#         if flag:
#             s.append(amax - amin)
# print(min(s))
#endregion

#region vidosik
# from ipaddress import *
# k = 0
# net = ip_network('172.16.168.0/255.255.248.0')
# for ip in net:
#     s = bin(int(ip))[2:]
#     if s.count('1') % 5 != 0:
#         k += 1
# print(k)
#endreion

#region 19748 (kege)
# from ipaddress import *
# ip1 = '157.220.185.237/23'
# ip2 = '157.220.184.230/23'
#находим маску из двух адресов
# print(bin(185)[2:])
# print(bin(184)[2:])
# net1 = ip_network(ip1, 0)
# net2 = ip_network(ip2, 0)
# k = 0
# print(net1)
# for ip1 in net1:
#     print(ip1)
#     s1 = bin(int(ip1))[2:]
#     print(s1)
#     if s1.count('1') == 15:
#         k += 1
# print(k)
#endregion

#region 19245 (kege)
# from ipaddress import *
# net = ip_network('218.194.82.148/255.255.255.192', 0)
# for ip in net:
#     s = bin(int(ip))[2:]
#     l = str(ip)
#     print(l.replace('.', ''))
#
#
# 21819482190
# 21819482190
#endregion

#region 11243 (решуегэ)
# s = '1' + '9' * 98
# while ('19' in s) or ('299' in s) or ('3999' in s):
#     s = s.replace('19', '2', 1)
#     s = s.replace('299', '3', 1)
#     s = s.replace('3999', '1', 1)
# print(s)
#endregion

#region 19244 (kege)
# for n in range(3, 10000):
#     s = '1' + '2' * n
#     while ('12' in s) or ('322' in s) or ('222' in s):
#         if '12' in s:
#             s = s.replace('12', '2', 1)
#         if '322' in s:
#             s = s.replace('322', '21', 1)
#         if '222' in s:
#             s = s.replace('222', '3', 1)
#     sum = 0
#     for i in s:
#         sum = sum + int(i)
#     if sum == 15:
#         print(n)
#         break
#endregion

#region 18862 (kege)
# from ipaddress import *
# # k = 0
# # net = ip_network('172.140.68.0/255.255.248.0', 0)
# # for ip in net:
# #     s = bin(int(ip))[2:]
# #     if s.count('0') > 15:
# #         k += 1
# # print(k)
#endregion

#region 18615 (kege)
# from ipaddress import *
# mask = 0
# for mask in range(33):
#     net = ip_network(f'143.131.211.37/{mask}', 0)
#     k = 0
#     for ip in net:
#         s = bin(int(ip))[2:]
#         if s.count('1') == 10:
#              k += 1
#         if k > 15:
#             break
#     if k == 15:
#         print(mask)
#         break
#endregion

#region 18487 (kege) rot ebal
# from ipaddress import *
# net = ip_network('192.214.A.184/255.255.255.224', 0)
# k = 0
# A = 0
# for ip in net:
#     s = bin(int(ip))[2:]
#     if s.count('1') == 15:
#     k += 1
#     if k > 15:
#         break
#     if k == 15:
#     print()
#     break
#endregion

#region Вариант №17467093

#region №1
# print('№1: в пизду его')
#endregion
#region №2
# print('№2')
# print('x y z w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if (not(x <= w) or (y == z) or y) == 0:
#                     print(x, y, z ,w)
#endregion

#endregion

#region Макс

#region №12 yesss
# s = '0' + '1'*12 + '2'*15 + '3'*17
# while '01' in s or '02' in s or '03' in s:
#     s = s.replace('01', '20', 1)
#     s = s.replace('02', '120', 1)
#     s = s.replace('03', '302', 1)
# print(s.count('1'))
#endregion

#region №13 huynya kakaya-to
# from ipaddress import *
# for m in range(33):
#     ip1 = '231.32.255.131'
#     ip2 = '255.255.240.0'
#     net1 = ip_network(ip1, 0)
#     net2 = ip_network(ip2, 0)
#     if net1 != net2:
#         print(bin(int(net1.netmask))[2:])
#endregion

#region №16 unreal
# def f(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 1:
#         return 1
#     if n > 3:
#         return f(n - 3) + f(n - 2) + f(n - 1)
# print(f(9))
#endregion

#endregion

#region 18955 (kege)
from ipaddress import *
ip1 = '200.154.190.12'
ip2 = '200.154.184.0'
net1 = ip_network(ip1, 0)
net2 = ip_network(ip2, 0)
k = 0
for ip1 in net1:
    s = bin(int(ip1))[2:]
    while s.count('1') and k < 33:
        k += 1
print(k)