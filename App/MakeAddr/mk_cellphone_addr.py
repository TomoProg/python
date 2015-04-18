# -*- encode:utf-8 -*-

import os
import sys
import random

career_list = ['au', 'docomo', 'softbank']
domain_dict = { career_list[0]:'@ezweb.ne.jp', 
				career_list[1]:'@docomo.ne.jp', 
				career_list[2]:'@softbank.ne.jp' }

def main(argc, argvs):
	""" Program Main """

	if CheckArgs(argc, argvs) is False:
		print("Usage: python3 %s CareerName" % argvs[0])
		print("CareerName is [au] or [docomo] or [softbank]")
		sys.exit(1)

	domain = domain_dict[argvs[1]]

	MakeCellPhoneAddr(domain)


def CheckArgs(argc, argvs):
	""" Check Command Line """

	if argc != 2:
		return False
	if argvs[1] in career_list:
		return True
	else:
		return False

def MakeCellPhoneAddr(domain):
	""" Make Cellphone Address """

	make_list = []
	char_list = "1234567890abcdefghijklmnopqrstuvwxyz_-"

	for i in range(100000):
		user_name = ""
		user_name_num = random.randint(10,24)
		for j in range(user_name_num):
			random_char = random.choice(char_list)
			user_name += random_char
		make_list.append(user_name + domain + '\n')

	fd = open("cellphone_addr.txt", "w")
	for address in make_list:
		fd.write(address)
	fd.close()
	
if __name__ == "__main__":
	argvs = sys.argv
	argc = len(argvs)
	main(argc, argvs)
