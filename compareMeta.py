import yaml, sys

def main(fn1, fn2):

	with open(fn1, 'r') as fp1:
		data1 = yaml.load(fp1.read())

	with open(fn2, 'r') as fp2:
		data2 = yaml.load(fp2.read())

	compareObjects(data1, data2)


def compareObjects(obj1, obj2, path=['<root>']):

	descentKeys = []
	for key in set(obj1.keys()) | set(obj2.keys()):

		val1,val2 = obj1.get(key), obj2.get(key)
		if val1 != val2:
			if not isinstance(val1, dict) and not isinstance(val2, dict):
				print('{0}: {1} / {2}'.format('.'.join(path+[key]), val1, val2))
			else:
				descentKeys.append(key)

	for key in descentKeys:
		compareObjects(obj1[key], obj2[key], path+[key])
		

if __name__ == '__main__':
	main(sys.argv[-2], sys.argv[-1])