def Save(cur, z):
  import pymongo, dns
  text = "PawskSmujwNjsohsrbhbad"
  word = text[0:2] + text[3] + text[5] + text[9] + text[13] + text[16] +text[21]
  
  client = pymongo.MongoClient("mongodb+srv://Person:"+word+"@cluster0-u4jiy.mongodb.net/test?retryWrites=true&w=majority")
  db = client.test

  data = db.test
  
  result = db.test.replace_one({ "num": str(z) }, { "num": str(cur) }, upsert=True)
def Check(): 
  import pymongo, dns
  text = "PawskSmujwNjsohsrbhbad"
  word = text[0:2] + text[3] + text[5] + text[9] + text[13] + text[16] + text[21]


  client = pymongo.MongoClient("mongodb+srv://Person:"+word+"@cluster0-u4jiy.mongodb.net/test?retryWrites=true&w=majority")
  db = client.test

  data = db.test
  x = 0
  for x in data.find({}, { "_id": 0, "num": 1}):
      u = 0
  x = "'" + str(x) + "'"
  import re
  y = re.sub(r'[^\w\s]','',x)
  lst = [y]
  def convert(lst): 
      return ' '.join(lst).split()
  d = convert(lst)
  num = d[1]
  num = int(num)
  num = num 
  return num
    
   