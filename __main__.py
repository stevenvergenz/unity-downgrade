import sys, yaml, glob
from pathlib import Path
import transforms

def main(args):

	root = Path(args[-1])
	for pathname in root.glob('**/*'):

		filename = str(pathname)

		if pathname.is_dir():
			continue

		elif filename.endswith('.mat'):
			print('Material: '+filename)
			rewriteMaterial(filename)
		
		elif filename.endswith('.unity'):
			print('Scene: '+filename)

		elif filename.endswith('.png.meta') or filename.endswith('.jpg.meta'):
			print('Tex Meta: '+filename)
			rewriteTexMeta(filename)


def rewriteMaterial(filename):

	with open(filename, 'r') as fp:
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
	
	answer = None
	while answer not in ['','y','n']:
		answer = input('Overwrite {0}? [y/N] '.format(filename))

	if answer == 'y':
		with open(filename, 'w') as fp:
			fp.write(origHeader+newBody)


def rewriteTexMeta(filename):

	with open(filename, 'r') as fp:
		rawinput = fp.readlines()

	data = yaml.load(''.join(rawinput))
	transforms.transformTexMeta(data)
	output = yaml.dump(data)

	answer = None
	while answer not in ['','y','n']:
		answer = input('Overwrite {0}? [y/N] '.format(filename))

	if answer == 'y':
		with open(filename, 'w') as fp:
			fp.write(output)


if __name__ == '__main__':
	main(sys.argv)