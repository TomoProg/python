#-*- coding:utf-8 -*-

import urllib.request

def GetHTMLString(url):
	""" 指定したURLのHTML文書を取得する """
	try:
		url_data = urllib.request.urlopen(url)
		str_html = url_data.read()
		chara_code = JudgeCharaCode(str_html)
		if chara_code is not None:
			str_html = str_html.decode(chara_code)
		else:
			str_html = None
	except:
		str_html = None

	return str_html

def JudgeCharaCode(str_data):
	""" HTMLの文字コードを判定する """
	chara_code_list = ["utf-8", "cp932", "euc-jp", "iso2022_jp", "shift-jis"]
	flag = False
	for chara_code in chara_code_list:
		try:
			str_data.decode(chara_code)
			flag = True
			break
		except:
			pass

	if flag:
		return chara_code
	else:
		return None

if __name__ == "__main__":
	html = GetHTMLString('http://www.yahoo.co.jp/')
	print(html)
