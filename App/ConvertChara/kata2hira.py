#-*- coding:utf-8 -*-

import os
import sys

def Hiragana2Katakana(file_name):
	""" カタカナ -> ひらがな変換 """
	chara_dict = {  "ア":"あ", "イ":"い", "ウ":"う", "エ":"え", "オ":"お",
					"カ":"か", "キ":"き", "ク":"く", "ケ":"け", "コ":"こ",
					"サ":"さ", "シ":"し", "ス":"す", "セ":"せ", "ソ":"そ",
					"タ":"た", "チ":"ち", "ツ":"つ", "テ":"て", "ト":"と",
					"ナ":"な", "ニ":"に", "ヌ":"ぬ", "ネ":"ね", "ノ":"の",
					"ハ":"は", "ヒ":"ひ", "フ":"ふ", "ヘ":"へ", "ホ":"ほ",
					"マ":"ま", "ミ":"み", "ム":"む", "メ":"め", "モ":"も",
					"ヤ":"や", "ユ":"ゆ", "ヨ":"よ",                     
					"ラ":"ら", "リ":"り", "ル":"る", "レ":"れ", "ロ":"ろ",
					"ワ":"わ", "ヲ":"を", "ン":"ん",                     
					"ガ":"が", "ギ":"ぎ", "グ":"ぐ", "ゲ":"げ", "ゴ":"ご", 
					"ザ":"ざ", "ジ":"じ", "ズ":"ず", "ゼ":"ぜ", "ゾ":"ぞ", 
					"ダ":"だ", "ヂ":"ぢ", "ヅ":"づ", "デ":"で", "ド":"ど", 
					"バ":"ば", "ビ":"び", "ブ":"ぶ", "ベ":"べ", "ボ":"ぼ", 
					"パ":"ぱ", "ピ":"ぴ", "プ":"ぷ", "ペ":"ぺ", "ポ":"ぽ", 
					"ァ":"ぁ", "ィ":"ぃ", "ゥ":"ぅ", "ェ":"ぇ", "ォ":"ぉ", 
					"ャ":"ゃ", "ュ":"ゅ", "ョ":"ょ", 
					"ッ":"っ", }
	try:
		r_f = open(file_name, "r")
		w_f = open("hiragana_list.txt", "w")
	except:
		print("file open error!!")
		sys.exit(1)
	
	for line in r_f:
		line = line.rstrip()
		for chara in line:
			if chara in chara_dict:
				cvt_chara = chara_dict[chara]
				w_f.write(cvt_chara)
			else:
				w_f.write(chara)
		w_f.write("\n")
	
	r_f.close()
	w_f.close()

	print("Success!!")

if __name__ == "__main__":
	args = sys.argv
	argc = len(args)

	if argc != 2:
		print("Usage python3 %s hiragana_file")
		sys.exit(1)

	Hiragana2Katakana(args[1])
