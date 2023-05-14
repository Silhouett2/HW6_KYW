import random
import csv 

# result=[0]*6 #오 이런것도 되네 


print('주사위를 100회 던집니다.')

dice100 =[]
dice1000 = []
dice10000 = []
dice100000 = []



f = open('random.csv', 'w', newline = "",encoding='UTF8')
writer = csv.writer(f)

# write the header


# write the data
# writer.writerow(data)


def randomdicenum(n) :
    

    globals()["dice{}".format(n)] = []
    dicen = globals()["dice{}".format(n)]
    for i in range(n):
        dicen.append(random.randint(1,6))
    

    return dicen

dice_n = randomdicenum(100)
writer.writerow(dice_n)
dice_n = randomdicenum(1000)
writer.writerow(dice_n)
dice_n = randomdicenum(10000)
writer.writerow(dice_n)
dice_n = randomdicenum(100000)
writer.writerow(dice_n)

f.close()

def main():
    print(" ")
if __name__ == '__main__':
    main()


