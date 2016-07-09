# Engine

This folder will contain the scripts that run the Osiris arbitrage model. Calling on code and performing various actions.

Engine archicture as follows:

* engineMaster.py

Is the core py script that makes calls to functions and classes defined else where. Whill contain the looping logic etc.

* utilities.py

Contains the generic utility functions that are called from the engine script. 

* betfair.py

Contains the API logic for Betfair that is needed in the more generic functions (getOdds etc.)

* pinnacleR.py

Sets the key pinnacle API calls (R code) as strings that will be executed by the rpy2 library.

* params.py

Some key control parameters that can be set for the engine script.