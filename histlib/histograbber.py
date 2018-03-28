import pandas
import pandas_datareader.data as web
import datetime
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import json
script_dir = os.path.abspath(__file__)
data_dir = script_dir.replace('histlib/histograbber.py', 'data') # dataset folderpath getter



breachstart = datetime.datetime(2017, 9, 3);
breachend = datetime.datetime(2017,9,20);

intelstart = datetime.datetime(2017, 10, 3);
intelend = datetime.datetime(2018, 3, 1);


sctstart = datetime.datetime(2014, 1, 1);
sctend = datetime.datetime(2018, 1, 1);


amastart = datetime.datetime(2017, 10, 3);
amaend = datetime.datetime(2018, 3, 24);


def main():
	stock = "EFX";
	f = open(data_dir+'/equifaxbreach.data', 'w')
	stock_data = web.DataReader(stock, "iex", breachstart, breachend)
	out = stock_data.to_dict(orient='dict')
	jdata = json.dumps(out)
	f.write(jdata)
	f.close();

	stock = "INTC"
	f = open(data_dir+'/intel.data', 'w')
	stock_data = web.DataReader(stock, "iex", intelstart, intelend)
	out = stock_data.to_dict(orient='dict')
	jdata = json.dumps(out)
	f.write(jdata)
	f.close();

	stock = "SMG"
	f = open(data_dir+'/scottsgro.data', 'w')
	stock_data = web.DataReader(stock, "iex", sctstart, sctend)
	out = stock_data.to_dict(orient='dict')
	jdata = json.dumps(out)
	f.write(jdata)
	f.close();

	stock = "AMZN"
	f = open(data_dir+'/amazon.data', 'w')
	stock_data = web.DataReader(stock, "iex", amastart, amaend)
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