import random

def Singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@Singleton
class Y:
    def __init__(self, *args, **kwargs):
        print(*args)
        self.value = random.randint(1, 100)


if __name__ == "__main__":
    s1 = Y(3,5,6)
    s2 = Y(9.10,5)

    # print(s1.value , s2.value)# True
    #
    #
    # if id(s1) == id(s2):
    #     print("Singleton works, both variables contain the same instance.")
    # else:
    #     print("Singleton failed, variables contain different instances.")



"""other solution for singleton"""
class singletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Y(metaclass=singletonMeta):
    def __init__(self, *args, **kwargs):
        print("y considerd called")
        print(*args)
        self.value = random.randint(1, 100)

s1 = Y()
s2 = Y()
# print(s1.value , s2.value)# True


"""FACTORY"""
class Person:
    age :int
    name : str

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person {self.name}, age: {self.age}'

    @classmethod
    def create_from_dict(cls, data):
        if data['age'] <18:
            raise Exception('age is too young')
        return Person(data['name'], data['age'])

    @staticmethod
    def create_from_string(*args, **kwargs):
        pass

data = {'name': 'Ahmad', 'age': 19}
person1= Person.create_from_dict(data)
person2 = Person('ali',110)
print(person1,person2)

"""observer"""
# class subscriber:
#     def update(self, data):
#         pass

# class publisher:
#     subscribers = []

#     def subscribe(self, a):
#         self.subscribers.append(a)

#     def notify_subcriber(self,data):
#         for s in self.subscribers:
#             s.update(data)

#     def unsubscribe(self, a):
#         pass

# class SampleSubcriber(subscriber):
#     def update(self, data):
#         print(f'sample subcriber got data: {data}')


# class Sample2Subcriber(subscriber):
#     counter= 0
#     def update(self, data):
#         self.counter +=1
#         print(f'sample2 subcriber got data: {data} --counter: {self.counter}')


# s1 = SampleSubcriber()
# s2 = Sample2Subcriber()

# p = publisher()

# p.subscribe(s1)
# p.notify_subcriber('notify')
# p.notify_subcriber('notify')
# p.notify_subcriber('notify')
# p.notify_subcriber('notify')
# p.subscribe(s2)
# p.notify_subcriber('notify2')
# p.notify_subcriber('notify2')
# p.notify_subcriber('notify2')