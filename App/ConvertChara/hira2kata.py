#-*- coding:utf-8 -*-

import os
import sys

def Hiragana2Katakana(file_name):
	""" ひらがな -> カタカナ変換 """
	chara_dict = {"あ":"ア", "い":"イ", "う":"ウ", "え":"エ", "お":"オ",
					"か":"カ", "き":"キ", "く":"ク", "け":"ケ", "こ":"コ",
					"さ":"サ", "し":"シ", "す":"ス", "せ":"セ", "そ":"ソ",
					"た":"タ", "ち":"チ", "つ":"ツ", "て":"テ", "と":"ト",
					"な":"ナ", "に":"ニ", "ぬ":"ヌ", "ね":"ネ", "の":"ノ",
					"は":"ハ", "ひ":"ヒ", "ふ":"フ", "へ":"ヘ", "ほ":"ホ",
					"ま":"マ", "み":"ミ", "む":"ム", "め":"メ", "も":"モ",
					"や":"ヤ", "ゆ":"ユ", "よ":"ヨ",
					"ら":"ラ", "り":"リ", "る":"ル", "れ":"レ", "ろ":"ロ",
					"わ":"ワ", "を":"ヲ", "ん":"ン",
					"が":"ガ", "ぎ":"ギ", "ぐ":"グ", "げ":"ゲ", "ご":"ゴ", 
					"ざ":"ザ", "じ":"ジ", "ず":"ズ", "ぜ":"ゼ", "ぞ":"ゾ", 
					"だ":"ダ", "ぢ":"ヂ", "づ":"ヅ", "で":"デ", "ど":"ド", 
					"ば":"バ", "び":"ビ", "ぶ":"ブ", "べ":"ベ", "ぼ":"ボ", 
					"ぱ":"パ", "ぴ":"ピ", "ぷ":"プ", "ぺ":"ペ", "ぽ":"ポ", 
					"ぁ":"ァ", "ぃ":"ィ", "ぅ":"ゥ", "ぇ":"ェ", "ぉ":"ォ", 
					"ゃ":"ャ", "ゅ":"ュ", "ょ":"ョ", 
					"っ":"ッ", }
	try:
		r_f = open(file_name, "r")
		w_f = open("katakana_list.txt", "w")
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
