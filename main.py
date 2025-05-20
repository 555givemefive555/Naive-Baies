import re
import pandas as pd
import time

df = pd.read_csv('dataset.csv')

def create_probability(request):
    a = 1
    PS = 1
    PNS = 1

    Spam = list(df.Frequency_in_spam.values)
    Not_Spam = list(df.Frequency_in_notspam.values)
    Words = list(df.Word.values)

    for i in range(len(request)):
        if request[i] in Words:
            ind = Words.index(request[i])
            PSi = (Spam[ind]+a)/(sum(Spam)+len(Words)*a)
            PNSi = (Not_Spam[ind]+a)/(sum(Not_Spam)+len(Words)*a)
        else:
            PSi = (a)/(sum(Spam)+len(Words)*a)
            PNSi = (a)/(sum(Not_Spam)+len(Words)*a)
        PS *= PSi
        PNS *= PNSi
    return PS, PNS


APS = sum(df.Labels.values) / len(df.Labels.values)
APNS = (len(df.Labels.values) - sum(df.Labels.values)) / len(df.Labels.values)

def add_text(request, label):
    request = request_processing(request)
    for j in range(len(request)):
        if request[j] not in df.Word.values:
            df.loc[len(df.Word.values)] = [request[j], label, 1-label]
        else:
            ind = df.Word.values.index(request[j])
            df.Frequency_in_spam.values[ind] += label
            df.Frequency_in_notspam.values[ind] += 1-label
    return 'Text was added in Dataset'
    
def request_processing(request):
    request = re.split(r'[,? ]', request.lower())
    temp = []
    for i in range(len(request)):
        if request[i]:
            temp.append(request[i])
    return temp

def checking(request):
    request = request_processing(request)
    # print(request)
    PS, PNS = create_probability(request)
    PS = (PS * APS)
    PNS = (PNS * APNS)
    # print(PNS, PS)
    S = PS + PNS
    PS = PS / S
    PNS = PNS / S
    return(PS, PNS)

while True:
    print('')
    print('Choose a number:')
    print('1. Add text to the dataset')
    print('2. Check the text for SPAM')
    print('3. View dataset')
    print('4. Load Dataset')
    print('5. Save Dataset')
    print('Write"q" for exit')
    print('')
    print('Input: ', end = '')
    time.sleep(1)
    choice = input()
    if choice == '1':
        print('')
        print('Write the text:')
        time.sleep(1)
        request = input()
        print('')
        print('Write number of the class')
        print('1. Not spam')
        print('2. Spam')
        print('')
        print('Input: ', end = '')
        time.sleep(1)
        label = input()
        if label in ['1', '2']:
            print('')
            print(add_text(request, int(label)-1))
            print('')
        else:
            print('')
            print('Wrong input')
            print('')
            continue
    elif choice == '2':
        print('')
        print('Write the text:')
        time.sleep(1)
        request = input()
        PS, PNS = checking(request)
        print('')
        print('Spam - ', PS.round(2)*100, '%')
        print('Not spam - ', PNS.round(2)*100, '%')
        print('')
    elif choice == '3':
        print(df)
        time.sleep(1)
    elif choice == '4':
        print('')
        print('Write name of file')
        print('')
        print('Input: ', end = '')
        name = input()
        time.sleep(1)
        df = pd.read_csv(name)
        print('')
        print('Dataset was loaded')
        print('')
    elif choice == '5':
        print('')
        print('Write name of file')
        print('')
        print('Input: ', end = '')
        name = input()
        time.sleep(1)
        df.to_csv(name, index = False)
        print('')
        print('Dataset was saved')
    elif choice == 'q' or request == 'Q':
        break
    else:
        print('')
        print('Wrong input')
        print('')
        continue
    time.sleep(3)
    
    
