from numpy import *
import numpy as np
import csv
from gensim.models import word2vec, Word2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
from GradyFunction import functionStringdivided
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras.models import Sequential

DataNoneMotifs = []
DataMotifs = []
motifstrs = [""]
Nonemotifstrs = [""]
resultPatterns1 = []
resultPatterns2 = []
PatternsArray = []
Variant = 'CNN'


#########################################################FUNCTIONS####################
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
    ###########################################


#    /////// Read Dataset, input:Paths
Sequences = []
with open('Sequences.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        Sequences.append(row)

for x in range(0, len(Sequences)):
    temp = listToString(Sequences[x])
    DataNoneMotifs.append(temp)

# // Load Weights
Weights = []
with open('WeightsOfPatterns.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        Weights.append(row)

# ////////////////////////////////////////////////////
print(Sequences)
for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 2):
        PatternsArray.append(x[i:i + 3])

for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 3):
        PatternsArray.append(x[i:i + 4])

for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 4):
        PatternsArray.append(x[i:i + 5])

for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 5):
        PatternsArray.append(x[i:i + 6])

for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 6):
        PatternsArray.append(x[i:i + 7])

#######################################
# // Break Patterns
strresult = []
for stri in PatternsArray:
    if len(stri) > 5:
        strresult.append(functionStringdivided(listToString(stri)))
    else:
        strresult.append(listToString(stri))

# // Match Weights of Patterns
weightsPattern = []
i = 0
for s in PatternsArray:
    for w in Weights:
        if s == w[0]:
            temp = []
            temp.append(w[1])
            temp.append(w[2])
    weightsPattern.append(temp)
print(len(weightsPattern))
print(len(strresult))


print(Sequences)
for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 2):
        PatternsArray.append(x[i:i + 3])

for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 3):
        PatternsArray.append(x[i:i + 4])

for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 4):
        PatternsArray.append(x[i:i + 5])

for s in range(0, len(DataNoneMotifs)):
    x = DataNoneMotifs[s]
    for i in range(0, len(x) - 5):
        PatternsArray.append(x[i:i + 6])
