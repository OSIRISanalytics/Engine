getOdds = '''

function(sport, user) {

	require(pinnacle.API)
	require(plyr)
	require(dplyr)
	require(tidyr)
	require(assertthat)

	AcceptTermsAndConditions(TRUE)
	if (user == "Tom") {SetCredentials("TB882982","Stanimal3#")}

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
	        gather("Key","Odds",spreads.home,spreads.away,moneyline.away,moneyline.home,moneyline.draw) %>%
	        mutate(Market_Type = ifelse(grepl("moneyline",Key), "moneyline",
	                                    ifelse(grepl("home",Key),"line.home","line.away")),
	               Market_Value = ifelse(grepl("spreads",Key), spreads.hdp,
	                                     ifelse(Key=="moneyline.home",1, ifelse(Key=="moneyline.away",-1,0))),
	               Market_Size = ifelse(Market_Type == "moneyline", maxMoneyline,maxSpread),
	               Market_Odds = convertAmerican(Odds),
	               StartTime = format(as.POSIXct(strptime(StartTime,"%Y-%m-%dT%H:%M:%SZ", tz = "GMT")),tz = "Australia/Melbourne", usetz = TRUE)) %>%
	        select(-maxSpread, -maxMoneyline,-Odds, -spreads.hdp, -PeriodNumber, -Key) %>%
	        select(StartTime:AwayTeamName,Market_Type,Market_Value,Market_Odds,Market_Size) %>%
	        rename(start_time=StartTime,sport_id=SportID,league_id=LeagueID,league_name = LeagueName,
	               event_id=EventID,line_id=lineId,home_team=HomeTeamName,away_team=AwayTeamName)

	names(data) = tolower(names(data))
	data = data[complete.cases(data),]
	data = cbind("time" = rep(Sys.time(), nrow(data)), data)

	return(data)

}


'''

placeBet = '''





'''
