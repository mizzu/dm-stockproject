import pandas
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import json
import re
from pattern.en import sentiment
from pattern.en import positive

from wordcloud import WordCloud
script_dir = os.path.abspath(__file__)
data_dir = script_dir.replace('scripts/scores.py', 'data/Twitter_Data/') # dataset folderpath getter
save_dir = script_dir.replace('scripts/scores.py', 'data/scores/') # dataset folderpath getter


dates = ["April27", "April28", "April29", "April30", "May1", "May2", "May3", "May4", "May5", "May6"]
filters = ["https co", "https", "RT"];

def  scores(stock):
	print stock;
	for dl in dates:
		c = open(save_dir+stock+dl+"scores.txt", "w")
		p_sent = 0;
		n_sent = 0;
		f = open(data_dir+stock+"_"+dl+".txt", 'r')
		for line in f:
			jdata = json.loads(line)
			if(sentiment(jdata['text'])[0] > 0):
				c.write(("{1," + "\"" + jdata['text'].encode('utf-8') + "\"" +"}\n"))
			if(sentiment(jdata["text"])[0] < 0):
				c.write(("{0," + "\"" + jdata['text'].encode('utf-8') + "\"" +"}\n"))
		f.close();
		c.close();
	

	

if __name__ == '__main__':
	scores("Facebook") #stock here
	scores("Amazon")
	scores("Nvidia")