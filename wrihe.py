from datetime import datetime


def Writetext(quantity,total):
    stamp = datetime.now()
    stamp = stamp.replace(year=stamp.year+543)
    stamp = stamp.strftime('%Y/%m/%d - %H:%M:%S')
    filename = 'data.txt'
    with open(filename,'a',encoding='utf-8') as file:
        file.write('\nวันที่-เวลา: {} หมาปิ้งจำนวน : {} ตัว ราคาทั้งหมด : {} บาท'.format(stamp,quantity,total))

# Writetext(100,1000)
# Writetext(200,1000)
# Writetext(400,1000)