# print(type(24))
# print(type(24.3))

# print('It\'s cloudy day')
# print('LOFTBLOG'[4])
# print('LOFTBLOG'[4:8])
# print('LOFTBLOG'[:5])
# print('LOFTBLOG'[5:])

# print(type(True))
# print(type(False))
# print(3==4)

# shoppinglist =30
# if (shoppinglist == 15):
# 	print('Nce choice , bro')
# elif (shoppinglist ==20):
# 	print('It\'s okey , bro')
# elif (shoppinglist == 30):
# 	print('Just for workout , bro')
# else:
# 	print ('Okey , let me have this adidas')

# value = 3
# if (value == 1):
# 	print('I love u')
# elif (value == 2):
# 	print('I hate u too')
# elif (value == 3):
# 	print('Have a good day')
# else:
# 	print('bye bye')
# digit = 100
# while digit <= 100:
# 	print(str(digit)+ ' Ok')
# 	digit = digit * 2
# print(str(digit) + 'more than 100!')
# arr = [1,4,6,3,5,10,2]
# sum=0
# for i in arr:
# 	if i == 10 or i == 6 or i == 2: 
# 		continue
# 		# break
# 	sum+=i;
# print(sum)

weekdays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
sum=0
for x in weekdays: 
	if x ==6 or x==7 or x==13 or x==14 or x==20 or x==21 or x==27 or x==28:
		continue
	sum+=x;
print(sum)

name = 'Naruto'
print(name)

gachiList = ['bar','mars','sun','saturn','eujfvurjv8jr','erikf9ejkrfke0rkf0ekrf09ker0fk','firfk9kdfkerkfeirf9id8v7ht68y4vh73urf98u3rf3','fioerjfoijer9fj9erjf9jedjf9ejd9fjeijfrhefh']
gachimuchilist = ['bar','casino','carting',gachiList,]
print(gachimuchilist[3][1])
byblik = [gachimuchilist,gachiList]
print(byblik[0][3])

productMiniList = ['lemonade','cocaCola']
productList = ['apple','milk','cheese', productMiniList,'tea']
print(productList[3][1])
def greeting():
	print('Hello it\'s a Python function')
greeting()

def height(m,cm):
	total = (m * 100) + cm
	print(total, ' cm tall')
height(1,70)
def weight(kg,g):
	total = (kg * 1000) + g
	print(total, 'g fat')
weight(88,5)

def calc(a,b):
	total = a+b
	return total
summ = calc(9954444685769,97895579579569)
print(summ)

print(42//2)
print(42.4//2)
print(7==7 and 6==7)
print(6<7 and 7==7)
print(7==9 or 4==5)
