import pandas as pd 
import re
import nltk
from nltk.probability import FreqDist
from matplotlib import pyplot as plt 
import seaborn as sns


word_count = 15
dataset = pd.read_csv('data.csv')
#print(dataset)

stop_words = ['its','on','time','talaga','that','flask','like','maganda','naman','received','really','buy','but','product',
              'lang','much','may','pa','item','color','no','po','din','was','as','yung','with','of','a','will','seller','at','order','thank','very',
              'ko','ako', 'i', 'na', 'sa', 'to', 'ng', 'ang', 'this', 'so', 'it', 'and', 'the', 'in', 'these', '5', 'is', 'my', 'for', 'you', 'super']

all_words = list()

for index, data in dataset.iterrows():
    words = str(data.comments).split()
    for w in words:
        temp_word = w.lower()
        temp_word = temp_word.encode('ascii', 'ignore').decode('ascii')
        temp_word = temp_word.strip()
        temp_word = re.sub(r'W\+', '', temp_word)
        if temp_word != '' and temp_word not in stop_words:
            all_words.append(temp_word)

new_dataframe = pd.DataFrame(all_words)
new_dataframe = new_dataframe[0].value_counts()

freq_doctor = FreqDist()
for word in new_dataframe:
    freq_doctor[word] += 1

new_dataframe = new_dataframe[:word_count]
sns.barplot(x=new_dataframe.values, y=new_dataframe.index)
plt.title('Most Frequent Word')
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.show()