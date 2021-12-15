import csv

def WriteCSV(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)



# d = ['2021-09-11 10:15:10',50,5000]

# WriteCSV(d)

def ReadCSV():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        #print(list(fr))
        data = list(fr)
    return data

def sumdata():
    # ฟังชั่นนี้ใช้สำหรับรวมค่าที่ได้จาก CSV ไฟล์สรุปออกมาเป็น 2 อย่าง
    result = ReadCSV()
    print('ทดสอบ :',result)
    sumlist_quan = []
    sumlist_total =  []
    for d in result:
        sumlist_quan.append(int(d[1]))
        print('ทดสอบ2',sumlist_quan)
        sumlist_total.append(int(d[2]))
    sumquan = sum(sumlist_quan)
    sumtotal = sum(sumlist_total)

    return (sumquan,sumtotal)

    #------------ แบบสั้นให้เขียน for loop ใส่ใน list---------------
    # sumlist_quan = sum([int(d[1]) for d in result])
    # sumlist_total = sum([int(d[2]) for d in result])
    
    # return (sumlist_quan,sumlist_total)

    

result =  sumdata()
print(result)


# #sumquan2 = sum([int(d[1]) for d in result])
# print(sumquan2)