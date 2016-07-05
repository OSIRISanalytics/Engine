pinnacleOdds = '''

function(uid, pword, sport) {

	library(pinnacle.API)

	AcceptTermsAndConditions(TRUE)
	SetCredentials(uid,pword)

	Odds = showOddsDF(sportname = sport)

	#Perform some manipulation on the data frame

	return(Odds)

}


'''

pinnacleBet = '''





'''
