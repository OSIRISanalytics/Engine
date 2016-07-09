Agency = "Pinnacle"
Sport = "Soccer"
uid = "TB882982"
pword = "Stanimal3#"

import pandas as pd
import params
import pinnacleR
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

# Perform some checks on the inputs
try:
	assert Agency in ['Betfair', 'Pinnacle']
	assert Sport in params.sports
except:
	print 'Invalid agency or sport'

rFunc = robjects.r(pinnacleR.pinnacleOdds)


rDF = rFunc(uid,pword,Sport)

pyDF = pandas2ri.ri2py(rDF)

print pyDF
