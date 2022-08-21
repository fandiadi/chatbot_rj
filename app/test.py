nums1 = [1, 5, 9, 11]
for num in nums1:
    print(num)

print('---')

num2 = 1
while num2 < 10:
    print(num2)
    num2 += 1  # berarti num = num + 1

print('---')

# menghasilkan 1,2,3
num3 = 1
while True:
    print(num3)
    num3 += 1
    if num3 >= 4:
        break

print('---')

# menghasilkan 1,2,3,4,5,6,7,8,9,10 lalu mencetak "num sudah mencapai 10"
num4 = 1
while(num4 <= 10):
    print(num4)
    num4 += 1
else:
    print("num sudah mencapai %d" % (num4))
# Prints out 1,2,3,4,5,6,7,8,9,10,11,12,13,14
for i in range(1, 15):
    if(i % 15 == 0):
        break
    print(i)
else:
    print("ini tidak akan dicetak karena perulangan dihentikan oleh break bukan karena kesalahan kondisi")
