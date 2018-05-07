import pandas
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
script_dir = os.path.abspath(__file__)
data_dir = script_dir.replace('scripts/wc.py', 'data/twitterdata/') # dataset folderpath getter

#add filter list

def  stats(file):
	count = 0
	f = open(data_dir+file)
	wct = '';
	for line in f:
		parts = line.split(', ')
		wct += str() + " "
	plt.imshow(WordCloud().generate(wct));
	plt.savefig(file.split('.')[0]+'wc.png');
	f.close();
	

	

if __name__ == '__main__':
	#stats() filename here