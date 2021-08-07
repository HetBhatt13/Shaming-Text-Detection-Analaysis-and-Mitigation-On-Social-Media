import pandas as pd
import re
passingjudgement=pd.read_csv('Passingjudgement.txt',header = None)
religion=pd.read_csv('religion.txt',header = None)
abusive=pd.read_csv('abusive.txt',header = None)
Comparison=pd.read_csv('Comparison.txt',header = None)
data=pd.read_csv('Clean Tweets.csv')
def check_word(y,user_list):
    if any (str(x).lower() in re.split(r'[;,.\s]\s*',y) for x in user_list):
                          return 'yes'

    else:
                          return "no"

##data['Passingjudgement']=data['Text'].apply(lambda x: check_word(x,Passingjudgement[0]))
##data['religion']=data['Text'].apply(lambda x: check_word(x,religion[0]))
##data['abusive']=data['Text'].apply(lambda x: check_word(x,abusive[0]))
##data['Comparison']=data['Text'].apply(lambda x: check_word(x,Comparison[0]))
##                          
    data.to_csv("check.csv")

    data1=data[['passingjudgement','religion','abusive','Comparison']].apply(pd.Series.value_counts).loc['yes',]

    data1.plot.bar(x=data1.index,y=data.values,rot=0)

ss=check_word("hello friend",religion[0])
print(ss)
