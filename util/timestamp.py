#-*- coding:utf-8 -*-

import datetime

def GetNowYMDHMSStamp():
	""" YYYYMMDDHHMMSS """
	dt = datetime.datetime.now()
	timestamp = dt.strftime('%Y%m%d%H%M%S')
	return timestamp

def GetNowYMDStamp():
	""" YYYYMMDD """
	dt = datetime.datetime.now()
	timestamp = dt.strftime('%Y%m%d')
	return timestamp

def GetNowHMDStamp():
	""" HHMMSS """
	dt = datetime.datetime.now()
	timestamp = dt.strftime('%H%M%S')
	return timestamp

if __name__ == "__main__":
	print(GetNowYMDHMSStamp())
	print(GetNowYMDStamp())
	print(GetNowHMDStamp())
