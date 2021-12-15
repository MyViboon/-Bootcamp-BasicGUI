from tkinter import*
from tkinter import ttk,messagebox
from datetime import datetime
import csv
########################################
def timestamp(thai=True):
    if thai:
        stamp = datetime.now()
        stamp = stamp.replace(year=stamp.year+543)
        stamp = stamp.strftime('%Y/%m/%d - %H:%M:%S')
    else:
        stamp = datetime.now().strftime('%Y/%m/%d - %H:%M:%S')

    return stamp    

def Writetext(quantity,total):
    # stamp = datetime.now() #ก่อนใช้ฟังชี่น timestamp
    # stamp = stamp.replace(year=stamp.year+543)
    # stamp = stamp.strftime('%Y/%m/%d - %H:%M:%S')
    stamp = timestamp()
    filename = 'data.txt'
    with open(filename,'a',encoding='utf-8') as file:
        file.write('\nวันที่-เวลา: {} หมาปิ้งจำนวน : {} ตัว ราคาทั้งหมด : {} บาท'.format(stamp,quantity,total))

def WriteCSV(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

def ReadCSV():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

def sumdata():
    # ฟังชั่นนี้ใช้สำหรับรวมค่าที่ได้จาก CSV ไฟล์สรุปออกมาเป็น 2 อย่าง
    result = ReadCSV()
    sumlist_quan = []
    sumlist_total =  []
    for d in result:
        sumlist_quan.append(int(d[1]))
        sumlist_total.append(int(d[2]))
    sumquan = sum(sumlist_quan)
    sumtotal = sum(sumlist_total)

    return (sumquan,sumtotal)


########################################
GUI = Tk()
GUI.geometry('600x570')
GUI.title('โปรแกรมคำนวนหมา V.0.0.1')
GUI.config(background='#a9f58e')

file = PhotoImage(file='dog.png').subsample(1)
MG = Label(GUI,image=file,background='#a9f58e')
MG.pack(pady=40)

L1 = ttk.Label(GUI,text='โปรแกรมขายหมาปิ้ง',font=('Angsana New',30,'bold'),foreground='blue',background='#a9f58e')
L1.pack()

L2 = ttk.Label(GUI,text='กรอกจำนวนข้อมูลหมาปิ้ง(ตัว)',font=('Angsana New',16),background='#a9f58e')
L2.pack()

V_quantity = StringVar()
E1 = ttk.Entry(GUI,textvariable=V_quantity,font=('impact',20))
E1.pack()

#=============================================================================================================

def Caculate(event=None):
    quantity = V_quantity.get()
    price = 1000
    cal = int(quantity) * price
    print(cal)

    # Writetext(quantity,cal)
    data = [timestamp(), quantity,cal]
    WriteCSV(data)

    title = 'ยอดลูกค้าที่ต้องจ่าย'
    text =  'หมาปิ้งจำนวน {} ตัว  ราคาทั้งหมด : {:,} บาท'.format(quantity,cal)
    messagebox.showinfo(title,text)

    V_quantity.set('')
    E1.focus()

B1 = ttk.Button(GUI,text= 'คำนวน',command=Caculate)
B1.pack(pady=20,ipadx=30,ipady=20)

E1.bind('<Return>',Caculate)

def Summarydata(event):
    sm = sumdata()
    title = 'ยอดสรุปรวมทั้งหมด'
    text =  'จำนวนที่ขายได้ : {:,} บาท  \nยอดขาย : {:,} บาท'.format(sm[0],sm[1])
    messagebox.showinfo(title,text)

GUI.bind('<F1>',Summarydata)
GUI.bind('<F2>',Summarydata)

E1.focus()
GUI.mainloop()