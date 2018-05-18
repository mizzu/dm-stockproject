import pandas
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import json
import re

from wordcloud import WordCloud
script_dir = os.path.abspath(__file__)
data_dir = script_dir.replace('scripts/wcgen.py', 'data/Twitter_Data/') # dataset folderpath getter
save_dir = script_dir.replace('scripts/wcgen.py', 'data/wcimgs/') # dataset folderpath getter


#add filter list
dates = ["April27", "April28", "April29", "April30", "May1", "May2", "May3", "May4", "May5", "May6"]
filters = ["httpsco", "https", "rt"];

def  stats(stock):
	count = 0
	for dl in dates:
		f = open(data_dir+stock+"_"+dl+".txt", 'r')
		wct = '';
		for line in f:
			jdata = json.loads(line)
			strr = jdata["text"].encode("utf-8").lower();
			for fil in filters:
				strr = strr.replace(fil, "");
			wct += " " + strr;
		plt.imshow(WordCloud().generate(wct));
		plt.savefig(save_dir+stock+"/"+stock+"_"+dl+"_wc.png");
		f.close();
	

	

if __name__ == '__main__':
	stats("Facebook") #stock here
	stats("Amazon")
	stats("Nvidia")