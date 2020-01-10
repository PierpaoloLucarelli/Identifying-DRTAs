import numpy as np
import csv
import math
from apta import APTA

accepted = []
rejected = []
t_min = math.inf
t_max = 0
SIGMA = 0

with open('data/test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
    	accept = row[-1]
    	row = row[:-1]
    	newRow = []
    	for timedString in row:
    		timedString_ = timedString.split("-")
    		if(int(timedString_[1]) > t_max):
    			t_max = int(timedString_[1])
    		if(int(timedString_[1]) < t_min):
    			t_min = int(timedString_[1])
    		if(int(timedString_[0]) > SIGMA):
    			SIGMA = int(timedString_[0])
    		newRow.append(timedString_)
    	if(accept=='1'):
    		accepted.append(newRow)
    	else:
    		rejected.append(newRow)
S = {}
S["accepted"] = accepted
S["rejected"] = rejected
SIGMA = np.arange(SIGMA)

apta = APTA(SIGMA, 0)
apta.learn(S,t_min,t_max)


################## QUESTIONS ##################

# 1) What do you pickas the starting state
# 2) Do we assume that each symbol causes a change in state? Can it not be that an symbol makes the state stay in same place?