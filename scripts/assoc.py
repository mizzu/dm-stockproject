import pandas
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import json
import re
import Orange

script_dir = os.path.abspath(__file__)
data_dir = script_dir.replace('scripts/assoc.py', 'data/Twitter_Data/') # dataset folderpath getter
save_dir = script_dir.replace('scripts/assoc.py', 'data/rules/') # dataset folderpath getter

assocfilter = ["Apple", "Amazon", "eBay", "AMZN", "APL", "down", "up", "Match Group",
               "MTCH", "stock", "high", "bull", "bear", "Twitter", "Microsoft", "Amazon Prime",
               "Intel", "INTC", "SNAP", "FB", "Snapchat", "TWTR", "GOOGL", "Google", "(SNAP)",
               "(INTC)", "(SNAP)", "(FB)", "(MSFT)", "Cryptocurrencies", "Cryptocurrency",
               "IBM", "Tesla", "TSLA", "(TSLA)", "Bitcoin", "(BTC)", "BTC", "Ethereum", "ETH", "(ETH)",
               "Fortnite", "inc", "Goldman Sachs", "Blockchain", "Spotify", "SPOT", "(SPOT)", "WhatsApp",
               "AMD", "GPU", "NVIDIA", "Nvidia", "low", "high", "AAPL", "#EthereumBlockchain"
               ]

#add filter list
dates = ["April27", "April28", "April29", "April30", "May1", "May2", "May3", "May4", "May5", "May6"]
filters = ["https co", "https", "RT"];

def  rules(stock):
  for dl in dates:
              
              
                f = open(data_dir+stock+"_"+dl+".txt", 'r')

                fd = open(save_dir+stock+"_"+dl+"Set.basket", 'w')
                fr = open(save_dir+stock+"_"+dl+"Rules.txt", 'w')

                fr.write( "-------------------------\n" )
                fr.write( dl +"\n")
                fr.write( "-------------------------\n" )

                for line in f:
                        contains = [];
                        jdata = json.loads(line)
                        for w in jdata["text"].encode("utf-8").split():
                          for wm in assocfilter:
                            if(w == wm):
                              contains.append(w);
                        if len(contains) != 00:
                          fd.write(",".join(contains).replace("[","").replace("]","")+"\n");

                i = 0;
                raw_data = []
                f.close();
                fd.close();
                                
                data = Orange.data.Table(save_dir+stock+"_"+dl+"Set.basket");

                rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.1)
                fr.write( "%4s %4s  %s\n" % ("Supp", "Conf", "Rule"))
                for r in rules[:]:
                        fr.write( "%4.1f %4.1f  %s\n" % (r.support, r.confidence, r))

            
                f.close();
                fd.close();




  

if __name__ == '__main__':
  rules("Facebook") #stock here
  rules("Amazon")
  rules("Nvidia")
