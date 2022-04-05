#!/usr/bin/env python3 

from bs4 import BeautifulSoup as bs
from requests import get 
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import csv 
from gtts import gTTS 

url =input('MEDIUM URL:\n')
filename = str(input('ARTICLE NAME:\n'))

#TODO : Working just with the free articles not with the premium articles. Add selenium to work with premium articles 

class Medium:
	def __init__(self, url, filename):
		self.url = url
		self.filename = filename
		return
	
	def save(self): 
		content = get(self.url).content
		bs_obj = bs(content,'lxml')

		#saving the article 
		paragraphs = bs_obj.find_all('p')
		text = [t.text for t in paragraphs]
		article_text = '\n'.join(text)
		with open(f'{self.filename}_article.txt', 'w') as wf:
			print(article_text, file =wf)
		print('article_Saved!')

		#saving the wordlist 
		words = word_tokenize(article_text)
		tags = pos_tag(words)


		en_tag = enumerate(tags)
		with open(f'{self.filename}_wordlist.csv','w') as wf:
			w = csv.writer(wf)
			for t in en_tag:
				w.writerow(t)
		print('wordlist_saved!')

		#save mp3 
		tts_engine = gTTS(article_text,lang='en', slow=True)
		tts_engine.save(f'{self.filename}.mp3')
		print('mp3 saved!')
		return

if __name__ == '__main__':
	md = Medium(url,filename=filename)
	md.save() 