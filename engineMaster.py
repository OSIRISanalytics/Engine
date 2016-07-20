# Load Utilities
import utilities
import params
from multiprocessing import Process
import time

# Test 1 


# test1 = utilities.getOdds("Soccer","Pinnacle","TB882982", "Stanimal3#")
# test2 = utilities.getOdds("Soccer","Pinnacle","TB882982", "Stanimal3#")


# # Test 2
if __name__ == '__main__':
	main_process, child_process = Pipe()
	pin_request = Process(target = utilities.getOdds, args =("Soccer","Pinnacle","TB882982", "Stanimal3#"))
	bet_request = Process(target = utilities.getOdds, args =("Soccer","Pinnacle","TB882982", "Stanimal3#"))
	test1 = p1.start()
	test2 = p2.start()
	p1.join()
	p2.join()



