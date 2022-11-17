# list

subway = [10, 20, 30]
print(subway.index(10))  # 1

subway.append(40) # [10, 20, 30, 40]
subway.pop() # [10, 20, 30]

# 리스트 내 값이 몇개 있는 지 확인
subway.append(10) # [10, 20, 30, 10]
subway.count(10) # 2

num_list = [5, 2, 4, 3]
num_list.sort()
print(num_list) # [2, 3, 4, 5]

num_list.reverse()
print(num_list) # [5, 4, 3, 2]

num_list.clear()
print(num_list) # []

num_list = [1, 2, 3, 4, 5]
mix_list = [10, 20, 30]
num_list.extend(mix_list)  # [1, 2, 3, 4, 5, 10, 20, 30]

# dictionary
dic = {1 : 'text'}  # key : 1, value : text
print(dic[1]) # text
print(dic[3]) # error

print(1 in dic) # True
print(3 in dic) # False

del dic[1] # {}
print(dic.keys()) # key만 출력
print(dic.values()) # value만 출력
print(dic.items()) # key, value 모두 출력

print(dic.clear()) # {}

# tuple
menu = ("aaa", "bbb")

(name, age, hobby) = ('aaa', 20, 'game')

# set
my_set = {1, 2, 3, 4, 3} # {1, 2, 3, 4}
my_set.add(5) # {1, 2, 3, 4, 5}
my_set.remove(5) # {1, 2, 3, 4}

set_ex1 = set(['aaa', 'bbb'])
set_ex2 = {'aaa'}
print(set_ex1 & set_ex2) # 'aaa'
print(set_ex2.intersection(set_ex1)) # 'aaa'

print(set_ex1 | set_ex2) # {'aaa', 'bbb'}
print(set_ex2.union(set_ex1)) # 'aaa'

print(set_ex1 - set_ex2) # 'bbb'
print(set_ex2.difference(set_ex1)) # 'aaa'


menu = {'aaa', 'bbb', 'ccc'} # SET
menu = list(menu) # list
menu = tuple(menu) # tuple
menu = set(menu) # set