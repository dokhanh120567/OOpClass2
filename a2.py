for chu in 'quantrong':#Lặp chữ cái trong từ
	print('chu cai hien tai:', chu)

chuoi = ['Anh','Chi','Em']#Lặp chữ cái trong chuỗi
for tu in chuoi:
    print("Have a nice day", tu)
A =[1,2,3,21,3232]#Tính tổng các số trong dãy
tong = 0
for a in A:
	tong= tong +a
print("Tong cac so la:", tong)
#hàm range
print(range(9))
print(list(range(9)))
print(list(range(2,5)))
print(list(range(0,15,4)))
for tu in range(len(chuoi)):
	print("Em yeu",chuoi[tu])
#if, else, for
B=[0,2,23,24]
for b in B:
	print(b)
else:
	print("Da het so")
#lặp dãy từ 0 đến 10 
for num in range(11,30): 
#lặp trên các thừa số của một số trong dãy 
  for i in range(2,num): 
#xác định thừa số đầu tiên (phép chia có số dư bằng 0) 
    if num%i == 0: 
       j=num/i #ước lượng thừa số thứ 2
       print ('%d bằng %d * %d' % (num,i,j)) 
       break #dừng vòng for hiện tại, chuyển đến số tiếp theo trong vòng for đầu tiên 
  else: # phần else trong vòng lặp 
    print (num, 'là số nguyên tố') 
     