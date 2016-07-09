def archiveOdds(Sport, Agency, df):

	import sqlite3
	import pandas as pd

	if Agency == "Pinnacle":
		table = "odds_pinnacle"
	else:
		table = "odds_betfair"

	con = sqlite3.connect('DB')
	df.to_sql(table,con,if_exists = "append")
	con.close()


def getOdds(Sport, Agency, uid, pword, Archive = False):

	import pandas as pd
	import params
	import pinnacle
	import betfair
	import rpy2.robjects as robjects
	from rpy2.robjects import pandas2ri

	# Perform some checks on the inputs
	try:
		assert Agency in ['Betfair', 'Pinnacle']
		assert Sport in params.sports
	except:
		print 'Invalid agency or sport'

	if Agency == 'Pinnacle':

		# Load the Pinnacle API call function
		getPinnacle = robjects.r(pinnacle.getOdds)

		# Extract Odds from Pinnacle API
		rDF = getPinnacle(uid, pword, Sport)

		# Convert r dataframe object to a pandas python dataframe
		pyDF = pandas2ri.ri2py(rDF)

		# Are we archiving data to the SQLite DB?   OR
		# Are we returning the data to perform calcs in memory?
		if Archive:
			archiveOdds(Sport, Agency, pyDF)
		else:
			return pyDF 

	else:

		# Extract Odds from Betfair API
		pyDF = pyFunc(Sport)

		# Same as above
		if Archive:
			archiveOdds(Sport, Agency, pyDF)
		else:
			return pyDF 


test = getOdds("Soccer","Pinnacle","TB882982", "Stanimal3#")

print test.dtypes

def placePinnacleBet(LeagueID, Period):
	print 'test'


def placeBetfairBet(LeagueID, Period):
	print 'test'
