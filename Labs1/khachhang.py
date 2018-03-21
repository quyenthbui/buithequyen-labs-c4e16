from pymongo import MongoClient

from matplotlib import pyplot

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db['customers']

so_luong = customers.find()

count_qc = 0

count_tm = 0

count_sk = 0

for ref in so_luong:
    if ref['ref'] == 'ads':
        count_qc += 1
    elif ref['ref'] == 'wom':
        count_tm += 1
    else:
        count_sk += 1

print('''Số lượng:
quảng cáo : {0}
truyền miệng : {1}
sự kiện : {2}
'''.format(count_qc, count_tm, count_sk))

labels = ["quảng cáo", "truyền miệng", "sự kiện"]
values = [count_qc, count_tm, count_sk]

pyplot.pie(values, labels=labels, shadow=True, autopct='%.2f%%')
pyplot.suptitle('percentage of each reference', fontsize=16)
pyplot.axis('equal')
pyplot.show()
