import time

a = int(input("===> MASUKAN NILAI A NYA OM <=== : "))
time.sleep(5)
b = int(input("===> MASUKAN NILAI B NYA OM <=== : "))
time.sleep(5)

print ("|||||||||||||||||||||||||||||")
time.sleep(2)
print ("===> CEK PERSAMAAN NYA NYA : ")
time.sleep(5)
if(a==b):
	print ("NILAI A SAMA DENGAN NILAI B")
	time.sleep(5)
else:
	print ("NILAI A TIDAK SAMA DENGAN NILAI B")
	time.sleep(5)
print ("CEK PERTIDAKSAMAAN NYA : ")
time.sleep(5)
if(a!=b):
	print ("===> NILAI A TIDAK SAMA DENGAN NILAI B")
	time.sleep(5)
else:
	print ("===> NILAI A SAMA DENGAN NILAI B")
	time.sleep(5)
print ("CEK KURANG DARI : ")
time.sleep(5)
if(a<b):
	print ("===> NILAI A KURANG DARI NILAI B")
	time.sleep(5)
else:
	print ("===> NILAI A TIDAK KURANG DARI NILAI B")
	time.sleep(5)
print ("CEK LEBIH DARI ATAU SAMA DENGAN : ")
time.sleep(5)
if(a>b):
	print ("===> NILAI A LEBIH BESAR DARI B")
	time.sleep(5)
else:
	print ("===> NILAI A KURANG  DARI NILAI B")
	time.sleep(5)
print ("SELESAI...")
time.sleep(5)