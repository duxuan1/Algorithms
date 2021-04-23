def print_lst(a):
	"""
	loop practice
	"""
	for i in range(len(a)):  # i is index here
		print(a[i])

	for i in a:  # i is elements in list a
		print(i)

	i = 0
	while i < len(a):  # i is index
		print(a[i])
		i += 1


def find_key_in_list(a, name):
	"""
	dic = [["peter", 64], ["bob", 53]]
	find peter and return peter's score
	"""
	for i in range(len(a)):
		if a[i][0] == name:
			return a[i][1]
	return -1


def print_dictionary(dic):
	for key in dic:
		print("Key = " + str(key) + " Value = " + str(dic[key]))


class Human:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def add_age(self, value):
		self.age += value


if __name__ == "__main__":
	# int
	# 1, 2, 3
	# float
	# 0.1, 1.0
	# str
	# "a", 'a'

	# list
	a = [1, 2, 3]
	# append into list: a.append(4)
	# insert into list: a.insert(2, 4) [1,2,4(idx=2),3]
	# insert(idx, insert_value)
	# pop: a.pop(2), pop by index
	# remove: a.remove(4), remove by value [1,2,2,2,23], remove the first found value

	# tuple
	t = tuple([1, 2, 3])  # immutable

	# dictionary
	dic = {"peter": 64, "Bob": 53}
	# dictionary store key value pair, {"peter": 64, "Bob": 53}
	# key could be int, float, str, class
	# value could be int, float, str, class, List
	print(dic["peter"])  # find value for specific key
	a = [["peter", 64], ["bob", 53]]
	print(find_key_in_list(a, "peter"))  # find value for specific key in list
	# why dictionary, fast search by key
	dic["cindy"] = 100  # append key value pair in dictionary
	print(dic)
	dic = {"peter": [1, 2, 3], "Bob": [3, 4, 5]}  # append value into value by key
	dic["peter"].append(4)
	print(dic)
	del dic["peter"]  # delete key value pair in dictionary
	print(dic)
	print_dictionary(dic)

	# class construction
	H = Human("cindy", "21")
	print(H.get_age())
