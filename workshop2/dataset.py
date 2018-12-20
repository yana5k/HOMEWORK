"""
I Варіант. Дано структуру даних:
smth = [
	{
		'name':'Bob',
		'age':20,
		'marks':{
				'Math':98,
				'Python':100
				}
	},
	{
		'name':'Boba',
		'age':19,
		'marks':{
				'Physics':98
				}
	},
	{
		'name':'Boban',
		'age':22,
		'marks':{
				}
	}
]
1. Написати рекурсивну функцію, що виводить вік найстаршого студента.
def maxAge(smth):
#some magic
return max_age
2. Написати функцію, що студенту з іменем name додає дисципліну disc з оцінкою
mark
def addMark(smth, name, disc, mark):
#some magic
3. Написати функцію, повертає список імен студентів
def getNames(smth):
#some magic
return [.....]
"""


smth = [
	{
		'name':'Bob',
		'age':20,
		'marks':{
				'Math':98,
				'Python':100
				}
	},

	{
		'name':'Boba',
		'age':19,
		'marks':{
				'Physics':98
				}
	},

	{
		'name':'Boban',
		'age':22,
		'marks':{
				}
	}
]

def maxAge(smth):
	'''smth -- list of dictionaries, each one corresponds to a different student
	Calculates the biggest age of all students, returns it.
	In each recursion level two ages are compared, the less one is deleted
	from smth. Thus in each level smth decreases, until its length
	becomes 1. That element which remains contains the biggest age.
	It is necessary to make a copy of smth at the first function call,
	otherwise the global variable smth will be changed.'''

	# stop signal -- max_age is found
	if len(smth) == 1:
		return smth[0]['age']

	if smth[0]['age'] > smth[1]['age']:
		del smth[1]
	else:
		del smth[0]

	return maxAge(smth)

print(maxAge(smth.copy()))


def addMark(smth, name, disc, mark):
	'''smth -- list of dictionaries
	name -- student's name
	disc -- name of school subject
	mark -- number of points at this subjects
	Adds to the student information about subject and mark.
	Doesn't return anything.'''
	for student in smth:
		if student['name'] == name:
			student['marks'][disc] = mark
	return

addMark(smth, 'Boban', 'Math', 80)
print(smth)


def getNames(smth):
	'''smth -- list of dictionaries
	Creates a list of all students' names, returns it.'''
	names = []
	for student in smth:
		names.append(student['name'])
	return names

print(getNames(smth))