#utf-8
import sqlite3
import json

conn = sqlite3.connect('/Users/hongjinwu/PycharmProjects/IPProxyPool/data/proxy.db')
cursor = conn.cursor()



def store(data):
    with open('/Users/hongjinwu/PycharmProjects/IPProxyPool/data/data.json','w') as json_file:
        json_file.write(json.dumps(data))

def load():
    with open('/Users/hongjinwu/PycharmProjects/IPProxyPool/data/data.json') as json_file:
        data = json.load(json_file)
        return data

if __name__ == "__main__":

    cursor.execute('select ip,port from proxys')
    values = cursor.fetchall()
    jsondata = json.dumps(['proxys',values])
    data = jsondata
    store(data)

    data = load()



cursor.close()
conn.close()