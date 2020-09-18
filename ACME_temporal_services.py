from os import system, name
import random as r
import requests
import secrets as s
import time

traveler_hash = None


def destination_collect():
	""" Collects destination date for within the solar context of Sector ZZ9 Plural Z Alpha. """
	clear()
	print("Please enter all datetimes as integers within the solar context of Sector ZZ9 Plural Z Alpha (Common name: Earth).\n")
	while True:
		try:
			year = int(input("Please input a destination year: "))
		except:
			continue
		if type(year) is not int:
			continue
		else:
			break

	clear()
	print("Please enter all datetimes as integers within the solar context of Sector ZZ9 Plural Z Alpha (Common name: Earth).\n")
	while True:
		try:
			month = int(input("Please input a destination month: "))
		except:
			continue
		if type(month) is not int or month < 0 or month > 12:
			continue
		else:
			break

	clear()
	print("Please enter all datetimes as integers within the solar context of Sector ZZ9 Plural Z Alpha (Common name: Earth).\n")
	while True:
		try:
			day = int(input("Please input a destination day: "))
		except:
			continue
		if type(day) is not int or day < 0 or day > 31:
			continue
		else:
			break

	try:
		x = time.asctime(time.strptime(
			str(year) + "-" + str(month) + "-" + str(day), "%Y-%m-%d"))
	except Exception as err:
		clear()
		print("""A solar flare, supernovae, super massive block hole, or other catastrophic interstellar event along your route of travel precludes travel to this datetime from your current spacetimezone.

You must restart the system and choose another datetime. Goodbye.\n""")
		raise SystemExit

	return x


def system_time():
	""" Displays reported system time. """
	return print("""Reported System Time: %s
Traveler Hash ID: %s\n""" % (time.strftime("%Y-%m-%d ~%H00 Hours", time.localtime()), traveler_hash))


def traveler_hash_verify():
	""" Checks if a traveler hash is present, otherwise generates new TrHash. """
	global traveler_hash
	try:
		localcache = open("time-machine.py.travelerhash", "r")
		traveler_hash = localcache.read()
		return True
	except:
		localcache = open("time-machine.py.travelerhash", "w")
		traveler_hash = s.token_hex(8)
		localcache.write(traveler_hash)
		return False


def clear():
	""" Clears the display buffer. """
	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

	system_time()


def disclaimer():
	""" Presents the Temporal Affairs Office Standard Disclaimer, Temporal Transport Precision Service Level (TTPSL), and confirmation of acceptance of terms. """
	clear()
	x = input("""The Intertemporal Standard Disclaimer and Terms of Use for the Temporal Transport Service is available for review in Section 0x2A of the Temporal Affairs Office in Alpha Centauri. Use of this system constitutes acceptance of those terms.

We can see, from the system you are using, the current date and hour is:

	< < <  %s  > > >

The hour indicated above does not have to be the same as your present terrestrial timezone, but it is imperitive this time is correct within your solar context.

Finally, due to computing limitations, spacetime travel computations using minutes is planned for a future release.

Is this time accurate? (Y/N) """ % time.strftime("%Y-%m-%d ~%H00 Hours", time.localtime())).lower()

	clear()
	y = input("""Given the aforementioned limitations, this system can only be used to return to a point in time in the past to a precision of +/- 25 Hours.

Is this acceptable? (Y/N) """).lower()

	if x == "y" and y == "y":
		clear()
		print("Your responses \"YES\" and \"YES\" to the Intertemporal Standard Disclaimer and Terms of Use are now recorded, and on file, at the Temporal Affairs Office. We salute your bravery and/or honor any desperate motivations for historic time travel. You may not see this screen again; please save a copy for your records.\n")
		return
	else:
		clear()
		print("You did not accept all terms of use. You may not use this system. Goodbye.\n")
		raise SystemExit


def temporal_transport_layer(x):
	""" Spacetime Travel Logic - v0.10.9-RC.12; Due to excessive fatalities implemented Gaussian fuzzing in targeting algorithm to avoid delivering traveler in or near the vicinity of the Rabbit of Caerbannog. """
	dest_time = x
	clear()

	while True:
		yn = input("""Your destination datetime is:

	> > >  %s  < < <

Is this correct (Y/N)? """ % dest_time).lower()
		if yn == "y":
			pass
		else:
			clear()
			print("You must restart the system. Goodbye.\n")
			raise SystemExit

		yn = input(
			"Are you ready to experience the splendors of ACME Temporal Transportation (Y/N)? ")
		if yn == "y":
			break
		else:
			clear()
			print("Bummer. You must restart the system. Goodbye.\n")
			raise SystemExit

	clear()
	print("\nInitiating one-way trip... Please close your eyes and make wibbly-wobbly timey-wimey sounds.")
	travel_time = r.randrange(3, 17)
	time.sleep(travel_time)

	clear()
	if r.randrange(1000) == 42:
		print("""It looks like there was a problem during your transport.

This often results in either transport to the wrong datetime, horrifying physical disfiguration, or nothing at all.

Please check the local datetime and your anatomy. If nothing is out of place in either case then you may attempt to use the Temporal Transportation Service again, but bear in mind subsequent use after this sort of failure results in greatly increased chances of chronic feelings of impending doom.""")
	else:
		print("""Welcome! The local datetime is:

	| | |  %s  | | |

Your trip took %d seconds; which, depending on your frame of reference, is new record!\n""" % (dest_time, travel_time))

	input("Press (nearly) any key to continue.")

	clear()
	print("Temporal Traveler Post-Travel Questionnaire:\n")
	while True:
		try:
			prompt = int(input("On a scale from 1-5, where a rating of 1 is poor and 5 is excellent, how would you rate your experience using ACME Temporal Transporation Services (1-5)? "))
		except:
			continue
		if prompt < 5:
			clear()
			print("%d is an invalid entry. Please try again.\n" % prompt)
			continue
		else:
			break

	clear()
	print("Temporal Traveler Post-Travel Questionnaire:\n")
	while True:
		prompt = input("For the following question, if you are presently unable to maniuplate your input device, blink once for \"YES\" or twice for \"NO\": Have you (1) arrived at the correct datetime destination, AND; (2) arrived with the same or similar anatomy with which you departed? (Y/N)? ").lower()
		if prompt == "y":
			break
		elif prompt == "n":
			clear()
			print("""We're terribly sorry for the inconvenience.

As you'll recall, you previously accepted the terms and conditions listed in the Intertemporal Standard Disclaimer and Terms of Use, specifically Volume 3, Book 14, Chapter 159, Paragraph 265, Item 3:

	\"...you hereby agree to indeminfy and hold harmless ... transportation events resulting in, including but not limited to, delivery to the incorrect datetime or celestial sector, physical disfiguration, and/or timeline modifications resulting in grave misfortune to you.\"\n""")
			input("Press (nearly) any key to continue... ")
			break
		else:
			continue

	clear()
	print("Temporal Traveler Post-Travel Questionnaire:\n")
	while True:
		prompt = input(
			"Do you smell fudge even if there is no fudge? (Y/N)? ").lower()
		if prompt == "y":
			print("\nSEEK IMMEDIATE MEDICAL ATTENTION.\n")
			raise SystemExit
		elif prompt == "n":
			clear()
			print("Thank you for using ACME Temporal Transportation Services. Please remember to update your system time.\n")
			raise SystemExit
		else:
			continue
