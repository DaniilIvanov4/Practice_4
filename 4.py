start = int(input('Стартовое количество: '))
yvel = float(int(str(input("Среднесуточное увеличение: ")).replace('%',""))/100)
kolvo = int(input("Количество дней для размножения: "))
print("День","Популяция",sep="     ")
print("1",start,sep="     ")
popylatyon = start+(start*yvel)
for i in range(2,kolvo+1):
    print(i,popylatyon,sep="     ")
    popylatyon += (popylatyon*yvel)





