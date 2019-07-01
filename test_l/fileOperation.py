# coding=UTF-8
import re, os, shutil

def movePdf(fromDir, toDir):
	if fromDir == '':
		return


	for root, dirs, files in os.walk(fromDir):

		for name in files:

			if os.path.splitext(name)[1] == '.pdf':
				shutil.copyfile(os.path.join(root, name), os.path.join(toDir, name))


def convertSwiftEnum():
	with open('/Users/lynn/Desktop/model.txt', 'r') as f:
		for line in f.readlines():

			s = line
			s = s.replace(' ', '')
			#res = re.match(r'^[a-zA-Z_]+<$', line);

			key = re.findall(r'[a-zA-Z_]+', s)

			print('    case %s = "%s"' % (key[0], key[2]))

if __name__ == "__main__":
	fromDir = r'/Volumes/WIN_ZZZ/极客时间/02 重学前端'
	toDir = r'/Users/lynn/Desktop/t'
	movePdf(fromDir, toDir)