# Load Utilities
import utilities
import params
import time
import pytz
import datetime

# Local Timezone
local = pytz.timezone ("Australia/Melbourne")
time =  datetime.datetime.now().replace(tzinfo = local).strftime("%Y-%m-%d %H:%M:%S")

# # # Loop through and Log odds into the database
while time < "2016-07-29 20:00:00":
	time =  datetime.datetime.now().replace(tzinfo = local).strftime("%Y-%m-%d %H:%M:%S")
	utilities.getOdds("Soccer","Betfair",time,"Tom", Archive = True)
	utilities.getOdds("Soccer","Pinnacle",time,"Tom", Archive = True)
