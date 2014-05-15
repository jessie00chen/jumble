#!/usr/local/bin/python
import sys

def make_dict(str):
	word = {}
	for i in str:
		try:
			word[i] = word[i]+1
		except KeyError:
			word[i] = 1			
	return word	

def jumble_me(dic, dic_path):
	try:
		with open(dic_path) as f:
			for line in f:
				new_dic = dic.copy()	
				line = line.rstrip()
				valid = 1
				for chr in line:
					try:
						new_dic[chr] = new_dic[chr]-1
						if new_dic[chr] < 0:
							valid = 0
							break
					except KeyError:
						valid = 0
						break

				if valid == 1:
					print line
	except IOError:
		print "Error: File doesn't exist:" + dic_path
		return 0

if __name__ == '__main__':
	try:
		input_string = sys.argv[1]
		dict_path = sys.argv[2]
	except:
		print "Insufficient input, try again"
		sys.exit()

	dic = make_dict(input_string)


	jumble_me(dic, dict_path)

# => chmod +x jumble.py
#10:48:54-jeschen@~/Desktop/jumble ./jumble.py 1 adf
#Error: File doesn't exist:adf
#10:48:57-jeschen@~/Desktop/jumble ./jumble.py 1
#Insufficient input, try again
# 10:38:01-jeschen@~/Desktop/jumble ./jumble.py abracadabra english-words.10
# a
# bad
# bar
# car
# card
# 10:38:08-jeschen@~/Desktop/jumble ./jumble.py apple english-words.10
# a
# apple
# plea
# 10:38:11-jeschen@~/Desktop/jumble ./jumble.py dog english-words.10
# do
# dog
# go 

