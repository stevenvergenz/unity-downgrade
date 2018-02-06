import sys, yaml
import transformer

def main(args):

	with open(args[-2], 'r') as fp:
		rawdata = fp.readlines()

	data = yaml.load(''.join(rawdata))

	data.transform()

	print(yaml.dump(data))


if __name__ == '__main__':
	main(sys.argv)