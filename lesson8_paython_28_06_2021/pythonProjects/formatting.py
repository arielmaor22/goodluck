for i in range(1,13):
    print("No. {0:10} squared is {1:3} and cubed is {2:4} ".format(i,i**2,i**3))

data="1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[1:5])
print(data[:-1:5])
######################
flower="blue violet"
print(flower in 'blue')
print(flower == 'blue')
print('blue' in flower)