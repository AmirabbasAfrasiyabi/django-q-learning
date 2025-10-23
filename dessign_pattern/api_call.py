import  json

class Person:
    def __init__(self, name, age,friends):
        self.name = name
        self.age = age
        self.friends = friends

class Person_Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name":obj.name , "age":obj.age , "friends":obj.friends }
        return super().default(obj)

def person_encoder(obj):
    if isinstance(obj, Person):
        return {"name":obj.name , "age":obj.age , "friends":obj.friends }
    return obj

p1 = Person("ahmad",19,[])
p2 = Person("amir",21,[p1])
data=  {
    "profile" :p2,
    "number":100.10
}

# json_data = json.dumps(data,cls=Person_Encoder)
json_data = json.dumps(data,default=person_encoder)
print(json_data)
print(json_data,type(json_data))
data = json.loads(json_data)
print(data['profile'],type(data['profile']))

