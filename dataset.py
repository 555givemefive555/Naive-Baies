import re
import pandas as pd

Dataset = ['Привет, как дела', 'Продам гараж', 'Продам носки',
           'Ты пойдешь?', 'Купите китайскую подставку', 'Здарова, брат']
labels = [0, 1, 1, 0, 1, 0]
ind = 0


def dataset_processing(Dataset, labels):
    Word = []
    Labels = []
    Frequency_in_spam = []
    Frequency_in_notspam = []
    for i in range(len(Dataset)):
        temp = re.split(r'[,? ]', Dataset[i].lower())
        temp1 = []
        for j in range(len(temp)):
            if temp[j]:
                temp1.append(temp[j])
        temp = temp1
        for j in range(len(temp)):
            if temp[j] not in Word:
                Word.append(temp[j])
                Labels.append(labels[i])
                Frequency_in_spam.append(labels[i])
                Frequency_in_notspam.append(1-labels[i])
            else:
                ind = Word.index(temp[j])
                Frequency_in_spam[ind] += labels[i]
                Frequency_in_notspam[ind] += 1-labels[i]
    Words = {'Word': Word,
             'Labels': Labels,
             'Frequency_in_spam': Frequency_in_spam,
             'Frequency_in_notspam': Frequency_in_notspam
             }
    df = pd.DataFrame(Words)
    return df


df = dataset_processing(Dataset, labels)
df.to_csv('dataset.csv', index = False)