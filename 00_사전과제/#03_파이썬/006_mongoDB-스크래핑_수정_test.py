from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'매트릭스'},{'_id':False})

target_star=target_movie['star']
print (target_star)
print (type(target_star))

same_movies = list(db.movies.find({'star':target_star}))
print(same_movies)

for movie in same_movies:
    print(movie['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'99'}})