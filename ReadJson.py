import json

def readjson():
    with open('data.json',encoding='utf-8') as file:
        data = json.load(file)
        # print(type(data))
        # print(data[0])
    return data

def writejson(data):
    jsonobject = json.dumps(data,ensure_ascii=False,indent=4)
    with open('fruit.json','w',encoding='utf-8') as file:
        file.write(jsonobject)


data = {'123133':['Banana',100,5],
        '34534': ['Durain',140,45],
        '6654645': ['แมว',140,45],
        '234233': ['แก้วมังกร',123,56]}

writejson(data)
