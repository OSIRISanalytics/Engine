def getOdds(Sport, User = "Tom",input_time = "Null",Market = 'MATCH_ODDS'):

    import pandas as pd
    import login
    import pytz
    import datetime
    from time import gmtime, strftime
    from betfair import utils
    from betfair import models
    from betfair import exceptions
    from betfair.models import MarketFilter
    from betfair.models import PriceProjection
    from betfair.models import ExBestOffersOverrides
    from betfair.models import MarketData

    if User == "Tom":
        #Tom
        client = login.login('Np2HwoLYyAQk2X6s', 'tombish22','parksandrec19')
    else:
        # Cal
        client = login.login('eTnX7n6jsiaoGA9g', 'calhamd@gmail.com','wyeslsc10')

    # Grab the sports that match the string provided as an argument
    event_types = client.list_event_types(MarketFilter(text_query=Sport))

    # Grab the ID of the requested sport
    sport_id = event_types[0].event_type.id

    # Pull the event details data for the sport and market specified as an argument
    betting_markets = client.list_market_catalogue(MarketFilter(event_type_ids=[sport_id], market_type_codes=[Market]), market_projection =  ['COMPETITION','EVENT','EVENT_TYPE','RUNNER_DESCRIPTION','MARKET_START_TIME'])

    # #Gets the list of market IDs in the Betting Market
    sports_market_ids = []
    for eachMarket in betting_markets:
        sports_market_ids = sports_market_ids + [eachMarket.market_id]

    # #Get the MarketBookResults
    maxpullsize = 100
    index=0
    # print len(sports_market_ids)
    marketbook_result = []
    while index+maxpullsize < len(sports_market_ids):
        marketbook_result = marketbook_result + client.list_market_book([sports_market_ids[index:index+maxpullsize]],PriceProjection(price_data=['EX_BEST_OFFERS'],exBestOffersOverrides=ExBestOffersOverrides(best_prices_depth=1)))
        index=index+maxpullsize
    marketbook_result = marketbook_result + client.list_market_book([sports_market_ids[index:len(sports_market_ids)]],PriceProjection(price_data=['EX_BEST_OFFERS'],exBestOffersOverrides=ExBestOffersOverrides(best_prices_depth=1)))  


    print 'Compiling Dataset'
    market_data = []
    for market in betting_markets:
        next_market_data = MarketData(market,next((x for x in marketbook_result if x.market_id == market.market_id), None))
        market_data.append(next_market_data)


    print 'Creating individual runner data'
    local = pytz.timezone ("Australia/Melbourne")
    runner_data = []
    for mindex, market in enumerate(market_data):
        for rindex, runner in enumerate(market.runners):
            runner_to_add = {'market_id': market.market_id, 
                                'market_name': market.market_name, 
                                'market_start_time': market.market_start_time.replace(tzinfo=pytz.utc).astimezone(local).strftime("%Y-%m-%d %H:%M:%S"),
                                'market_start_time_dt': market.market_start_time.replace(tzinfo=pytz.utc).astimezone(local),
                                #'total_matched':market.total_matched,
                                #'active_runners':market.number_of_active_runners,
                                'status':market.status,
                                #'total_available':market.total_available,
                                #'total_matched':market.total_matched,
                                #'selection_id':market.runner_catalog[rindex].selection_id,
                                'runner_name':market.runner_catalog[rindex].runner_name,
                                'price_selection_id':runner.selection_id,
                                'runner_status':runner.status
                                }
            
            if len(runner.ex.available_to_back)>0:
                runner_to_add.update({                         
                                'available_to_back_price':runner.ex.available_to_back[0].price,
                                'available_to_back_market':runner.ex.available_to_back[0].size
                                })
            if len(runner.ex.available_to_lay)>0:
                runner_to_add.update({                         
                                'available_to_lay_price':runner.ex.available_to_lay[0].price,
                                'available_to_lay_market':runner.ex.available_to_lay[0].size
                                })
            runner_data.append(runner_to_add)


    MarketDf = pd.DataFrame(runner_data)
    
    dt_cutoff = datetime.datetime.now().replace(tzinfo = local) + datetime.timedelta(days=2)

    # Only interested in open markets
    MarketDf.query("status == 'OPEN'", inplace=True)
    
    # Filter markets for those starting in the next 2 days
    MarketDf = MarketDf[(MarketDf.market_start_time_dt <= dt_cutoff)]
    
    #Add a logged time
    MarketDf.loc[:,"log_time"] = input_time
        
    #Reorder the columns and select
    cols = ["log_time","market_start_time","market_id","market_name","runner_name","price_selection_id","available_to_back_price","available_to_back_market","available_to_lay_price","available_to_lay_market"]
    MarketDf = MarketDf.loc[:,cols]
    
    return MarketDf


def placeBet(details):

    print "This function hasn't been built yet"
