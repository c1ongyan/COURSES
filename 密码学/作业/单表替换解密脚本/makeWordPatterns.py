#将所有单词的模式(例如all是(0.1.2))统计出来，得到模式到字母的一对多的映射

import pprint  #pprint 美化输出

#思路：1.遍历单词，将单个单词算出模式，然后放入模式映射单词的字典中
#2.算出模式的函数的思路：创建当个单词字母映射数字的字典和排好模式的列表，最后用join输出成固定格式

def getPattern(word):
#返回单词模式
	word=word.upper()
	wordList=[] #排好模式的列表
	wordZd={} #字母映射数字的字典
	num=0 

	for i in word:
		if i not in wordZd:
			wordZd[i]=str(num)
			num+=1
		wordList.append(wordZd[i])

	return '.'.join(wordList)

def main():
#找到所有单词的模式，并在字典中储存，返回模式映射单词的字典
	allPattern={}

	file=open('dictionary.txt','r')
	allWords=file.read().split() #读出所有单词，并分片成列表形式
	file.close()

	for i in allWords:
		pattern=getPattern(i)
		if pattern not in allPattern: 
			allPattern[pattern]=[i]
		else:
			allPattern[pattern].append(i)

	file=open('wordPatterns.py','w')
	file.write('allPatterns=')
	file.write(pprint.pformat(allPattern))
	file.close()

if __name__ == '__main__':
	main()






