getOdds = '''

function(uid, pword, sport) {

	require(pinnacle.API)
	require(plyr)
	require(dplyr)
	require(tidyr)
	require(assertthat)

	AcceptTermsAndConditions(TRUE)
	SetCredentials(uid,pword)

	assert_that(sport == "Soccer")

	Odds = showOddsDF(sportname = sport)

	convertAmerican = function(odds,...) {
	  if (odds > 0 ) {
	    return(odds/100 + 1)
	  } else {
	    return(100/abs(odds) + 1)
	  }
	}

	#Perform some manipulation on the data frame
	keepers = c("StartTime", "SportID", "LeagueID", "LeagueName",
	            "EventID", "lineId","PeriodNumber","HomeTeamName","AwayTeamName",
	            "spreads.hdp","spreads.home","spreads.away","maxSpread",
	            "moneyline.away","moneyline.home","moneyline.draw","maxMoneyline")

	data = Odds %>%
	        filter(LiveStatus != 1, PeriodNumber == 0) %>%
	        select(match(keepers,names(Odds))) %>% 
	        gather("Market_Value","Odds",
	               spreads.home,spreads.away,
	               moneyline.away,moneyline.home,moneyline.draw) %>%
	        mutate(Market_Type = ifelse(grepl("moneyline",Market_Value), "moneyline",
	                                    ifelse(grepl("home",Market_Value),"line.home","line.away")),
	               Market_Value = ifelse(grepl("spreads",Market_Value), spreads.hdp, Market_Value),
	               Market_Size = ifelse(Market_Type == "moneyline", maxMoneyline,maxSpread),
	               Market_Odds = convertAmerican(Odds)) %>%
	        select(-maxSpread, -maxMoneyline,-Odds, -spreads.hdp, -PeriodNumber) 
	        
	#remove any row with na values
	data = data[complete.cases(data),]

	data$Market_Value =  revalue(data$Market_Value,
	                      c("moneyline.home" = "1",
	                      "moneyline.away" = "0",
	                      "moneyline.draw" = "-1"))

	data = data[,c(1:8,10,9,12,11)]

	names(data) = c("start_time","sport_id", "league_id", "league_name", "event_id","line_id","home_team","away_team","market_type","market_value","market_odds","market_size")
	  
	return(data)

}


'''

placeBet = '''





'''
