import pymongo
from bson import ObjectId

# mongodb服务的地址和端口号
mongo_url = "mongodb://localhost:27017"

# 连接到mongodb，如果参数不填，默认为“localhost:27017”
client = pymongo.MongoClient(mongo_url)

#连接到数据库myDatabase
DATABASE = "tfo_journal"
db = client[DATABASE]

#连接到集合(表):myDatabase.myCollection
COLLECTION = "paper"
db_coll = db[COLLECTION ]

COLLECTION = "paper0811"
db_coll2 = db[COLLECTION ]





cur_journal = db_coll2.find({},{ "_id": 1, "authors": 1})

ii=0
for item_journal in cur_journal:
    authors = item_journal['authors']   ###每一篇文章的所有authors
    
    _id=item_journal['_id']
    #print(_id)
    #print('\n')
    #print('-------',authors)
    
    for i in authors:           #针对每一个author查看它的数据
        orgs=i['org']
        #print('=====',orgs)
        #print('该作者在作者列表中的位置%d'%(authors.index(i)))
        site=0              
        for i_org in orgs:      #i_org 遍历每一个author的所有org
            #   authors[authors.index(i)]代表了每一个author(name,org)
            
            
            
            #print(authors[authors.index(i)])
            authors[authors.index(i)]['org'][site]['en']=authors[authors.index(i)]['org'][site]['en'].strip()
            #print(authors[authors.index(i)]['org'][site]['en'])
            #print('*********',i_org)
            #print('该机构在机构列表中的位置%d'%(site))
            site=site+1
            
        
        #for i_org in orgs:
            #print(i_org)
        #print(i['org'][0]['en'])
        #print(i['org'])
        #i['org'][0]['en']=i['org'][0]['en'].strip()
        #print(i['org'][0]['en'])
        #print('\n')
    #print(authors)
    #update_result=db_coll2.update({'_id':{ "$eq" :ObjectId(_id)}},{"$set":{'authors':authors}})
    #print('更新成功吗？',update_result['updatedExisting'])
    #if not update_result['updatedExisting']:
        #print(_id)
        #break
    update_result=db_coll2.update({'_id':{ "$eq" :ObjectId(_id)}},{"$set":{'authors':authors}})
    #print('更新成功吗？',update_result['updatedExisting'])
    

    


















'''
COLLECTION = "paper_copy_1th"
db_coll3 = db[COLLECTION ]

result=db_coll3.find({'_id':{ "$eq" :ObjectId('60b1e76a7eb09a4cd3d15e9a')}},{'_id':1,'journal':1,'volume':1})
for i in result:
    print(i)
update_result=db_coll3.update({'_id':{ "$eq" :ObjectId('60b1e76a7eb09a4cd3d15e9a')}},{"$set":{'volume':'MongoDB11112222222','journal':'1111111'}})
print('更新成功吗？',update_result['updatedExisting'])
result=db_coll3.find({'_id':{ "$eq" :ObjectId('60b1e76a7eb09a4cd3d15e9a')}},{'_id':1,'journal':1,'volume':1})
for i in result:
    print(i)

'''



'''
text = open("C:\\Users\\Wu Xi\Desktop\\0123\爬虫\\wuxi1130.txt", "r", encoding="utf-8-sig")
contents = text.readlines()
text.close()

iii=0

for i in contents:
    i=i.strip()
    
    error_type=i[:8]
    if error_type=='字符串前后有空格':
        _id=i[i.find(': ')+1:i.find('url')]
        _id=_id.strip()
        #print('\n')
        #print(i)
        #print(_id)
    
        result=db_coll2.find({'_id':{ "$eq" :ObjectId(_id)}},{'page_str':1,'page_start':1,'page_end':1})
        for i_result in result:
            #print(i_result)
            
            page_str=i_result['page_str'].strip()
            page_start=i_result['page_start'].strip()
            page_end=i_result['page_end'].strip()
            #print(page_str,page_start,page_end)
        #
        # 
        update_result=db_coll2.update({'_id':{ "$eq" :ObjectId(_id)}},{'$set':{'page_str':page_str,'page_start':page_start,'page_end':page_end}})
        if not update_result['updatedExisting']:#############  检测插入是否失败
            break

''' 
        




