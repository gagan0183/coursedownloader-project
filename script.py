import os, os.path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("url")
parser.add_argument("totalnumber")
args = parser.parse_args()
if not os.path.exists(args.path):
	os.makedirs(args.path)
os.chdir(args.path)
count=0
totalnumber=int(args.totalnumber)
url=args.url
print(args.totalnumber + ' ' + url)
path = os.path.abspath(".")
count = len([name for name in os.listdir(path) if name.endswith('.mp4')])
while count < totalnumber:
	path = os.path.abspath(".")
	count = len([name for name in os.listdir(path) if name.endswith('.mp4')])
	count += 1
	print(count)
	try:
		os.system('youtube-dl --username "gagan.bhullar988@gmail.com" --password "ARIHANT_90" --verbose --playlist-start {} --sleep-interval 90 {}'.format(count, url))
	finally:
		print('error')