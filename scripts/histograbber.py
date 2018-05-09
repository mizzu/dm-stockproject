import pandas
import pandas_datareader.data as web
import datetime
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import json
script_dir = os.path.abspath(__file__)
data_dir = script_dir.replace('scripts/histograbber.py', 'data/stockdata') # dataset folderpath getter



start = datetime.datetime(2018, 4, 27);
end = datetime.datetime(2018,5, 6);


def main():
	stock = "NVDA";
	f = open(data_dir+'/NVIDIA.data', 'w')
	stock_data = web.DataReader(stock, "iex", start,end)
	out = stock_data.to_dict(orient='dict')
	jdata = json.dumps(out)
	f.write(jdata)
	f.close();

	stock = "FB"
	f = open(data_dir+'/Facebook.data', 'w')
	stock_data = web.DataReader(stock, "iex", start, end)
	out = stock_data.to_dict(orient='dict')
	jdata = json.dumps(out)
	f.write(jdata)
	f.close();


	stock = "AMZN"
	f = open(data_dir+'/Amazon.data', 'w')
	stock_data = web.DataReader(stock, "iex", start, end)
	out = stock_data.to_dict(orient='dict')
	jdata = json.dumps(out)
	f.write(jdata)
	f.close();

	#ax = stock_data.plot(figsize=(15, 4), kind='line', y='open', title = "Equifax Breach Stock Open Price", fontsize=8)
	#plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
	#ax.set_xticklabels(stock_data.index)
	#plt.savefig("equifax.png")

if __name__ == '__main__':
    main()