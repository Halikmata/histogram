import nltk
from nltk.probability import FreqDist
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import re

word_count = 15

# Use the correct path separator for the file path
dataset = pd.read_csv(r"C:\Users\JASON MAVERICK\Downloads\data.csv")

stop_words = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're",
    "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he',
    'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's",
    'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
    'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as',
    'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
    'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
    'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
    'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
    'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm',
    'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn',
    "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
    "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't",
    'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't",
    'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't",
    'ako', 'ka', 'ikaw', 'siya', 'kami', 'kayo', 'sila', 'atin', 'inyo', 'kanila',
    'akin', 'iyon', 'ito', 'iyan', 'doon', 'dito', 'isa', 'dalawa', 'tatlo', 'apat',
    'lima', 'anim', 'pito', 'walo', 'nweve', 'sampu', 'ganito', 'ganyan', 'iyon',
    'kung', 'kaya', 'dahil', 'sapagkat', 'ngunit', 'o', 'at', 'saka', 'gayunpaman',
    'kaya', 'dahil', 'dahilan', 'para', 'upang', 'hindi', 'wala', 'mayroon', 'meron',
    'sa', 'ng', 'ang', 'mga', 'sa', 'ng', 'ang', 'mga', 'na', 'ko', 'din', 'pa', ' ',
    'yung', 'po', 'naman', 'siya', 'lang', 'ay', 'sya', ''
]

all_words = []
for index, data in dataset.iterrows():
    words = str(data.comment).split()
    for w in words:
        temp_word = w.lower()
        temp_word = temp_word.encode('ascii', 'ignore').decode('ascii')
        temp_word = temp_word.strip()
        temp_word = re.sub(r'\W+', '', temp_word)
        if temp_word != '' and temp_word not in stop_words:
            all_words.append(temp_word)

new_dataframe = pd.DataFrame(all_words)
new_dataframe = new_dataframe[0].value_counts()
freq_doctor = FreqDist(all_words)

# Plot in histogram
new_dataframe = new_dataframe[:word_count]
sns.barplot(x=new_dataframe.values, y=new_dataframe.index)
plt.title('Most Frequent Word')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.show()