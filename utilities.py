def getOdds(Sport, Agency, Archive = False):

	import pandas as pd
	from rpy2.robjects import pandas2ri

	# Perform some checks on the inputs
	try:
		Agency in ['Betfair', 'Pinnacle']
		Sport in params.sports
	except:
		print 'Invalid agency or sport'

	# Load the Pinnacle API call function
	rFunc = robjects.r(RgetOdds)

	# Load the Betfair API call function
	pyFunc = execfile("FILEPATH TO PYTHON BETFAIR FUNCTION")


	if Agency == 'Befair':

		# Extract Odds from Pinnacle API
		rDF = rFunc(Sport)

		# Convert r dataframe object to a pandas python dataframe
		pyDF = pandas2ri.ri2py(rDF)

		# Are we archiving data to the SQLite DB?   OR
		# Are we returning the data to perform calcs in memory?
		if Archive:
			archiveOdds(Sport, Agency)
		else:
			return pyDF 

	else:

		# Extract Odds from Betfair API
		pyDF = pyFunc(Sport)

		# Same as above
		if Archive:
			archiveOdds(Sport, Agency)
		else:
			return pyDF 


def placePinnacleBet(LeagueID, Period):
	print 'test'


def placeBetfairBet(LeagueID, Period):
	print 'test'
