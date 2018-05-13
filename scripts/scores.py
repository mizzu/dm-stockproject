import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import os
import json
import re
from pattern.en import sentiment

script_dir = os.path.abspath(__file__)
data_dir = script_dir.replace('scripts/scores.py', 'data') # dataset folderpath getter
save_dir = script_dir.replace('scripts/scores.py', 'data/scores/') # dataset folderpath getter


dates = ["April27", "April28", "April29", "April30", "May1", "May2", "May3", "May4", "May5", "May6"]
filters = ["https co", "https", "RT"];

def  scores(stock):
	print stock;
	tn = 0;
	tp = 0;
	pv = []
	nv = []

	for dl in dates:
		c = open(save_dir+stock+dl+"scores.txt", "w")
		p_sent = 0;
		n_sent = 0;
		f = open(data_dir+'/Twitter_Data/'+stock+"_"+dl+".txt", 'r')
		for line in f:
			jdata = json.loads(line)
			if(sentiment(jdata['text'])[0] > 0):
				c.write(("{1," + "\"" + jdata['text'].encode('utf-8') + "\"" +"}\n"))
				p_sent +=1;
			if(sentiment(jdata["text"])[0] <= 0):
				c.write(("{0," + "\"" + jdata['text'].encode('utf-8') + "\"" +"}\n"))
				n_sent +=1;
		tp += p_sent;
		tn += n_sent;
		pv.append(p_sent);
		nv.append(n_sent);
		print dl
		print "Positive = " + str(p_sent);
		print "negative = " + str(n_sent);
		f.close();
		c.close();
	print "Total positive = " + str(tp);
	print "Total negative = " + str(tn);


	npv = np.asarray(pv);
	nnv = np.asarray(nv);
	



	fig, ax = plt.subplots(1) 

	ax.plot(npv, label = 'Positive');
	ax.plot(nnv, label = 'Negative');
	ax.plot
	ax.set_xticks([0,1,2,3,4,5,6,7,8,9])
	ax.set_xticklabels(dates)
	fig.suptitle(stock + " Sentiment Scores");
	fig.legend(loc='upper left')
	plt.savefig(save_dir+stock+"score.png");
	plt.clf()
	

if __name__ == '__main__':
	scores("Facebook") #stock here
	scores("Amazon")
	scores("Nvidia")