def Check(param): 
  text = "PawskSmujwNjsohsrbhbad"
  word = text[0:2] + text[3] + text[5] + text[9] + text[13] + text[16] + text[21]
  client = pymongo.MongoClient("mongodb+srv://myUser:" + word + "@cluster0-vj30z.mongodb.net/test?retryWrites=true&w=majority")
  base = client.test

  stuff = base.test
  clear()
  print(Green + "Welcome to the database!")
  for x in stuff.find({}, { "_id": 0, "Num": 1,}):
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
  return num
    
   