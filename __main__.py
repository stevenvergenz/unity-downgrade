import sys, yaml
import matfile

def main(args):
	rewriteMaterial(args[-2], args[-1])

def rewriteMaterial(infile, outfile):

	with open(infile, 'r') as fp:
		rawinput = fp.readlines()

	data = yaml.load(''.join(rawinput))
	data.transform()
	output = yaml.dump(data)
	outlines = output.split('\n')
	newBody = '\n'.join(outlines[1:])

	origHeader = ''
	for line in rawinput:
		origHeader += line
		if line[0:3] == '---':
			break
	
	with open(outfile, 'w') as fp:
		fp.write(origHeader+newBody)


if __name__ == '__main__':
	main(sys.argv)