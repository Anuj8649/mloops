from oops_proj import chatbook


#print(obj.__name)
#alter we can use print(obj._chatbook__name)


#getter and setter
#print(obj.get_name())
#bj.set_name("agent x")
#print(obj.get_name())


obj=chatbook()
#print(obj.user_id)
#print(obj.id)
print(obj.id)
chatbook.set_id(10)

obj1=chatbook()
#print(obj1.user_id)
print(obj1.id)

#obj2=chatbook()
#print(obj2.user_id)
#print(obj2.id)