# -*- coding: utf-8 -*- #
"""*********************************************************************************************"""
#   FileName     [ ohlcExtract.py ]
#   Synopsis     [ Compute the OHLC (open, high, low, close) prices of 台指期 within a given date based on minute-based trading record. The input file is a csv file recording minute-based trading data. ]
#   Author       [ Ting-Wei Liu (Andi611) ]
#   Copyright    [ Copyleft(c), NTUEE, NTU, Taiwan ]
"""*********************************************************************************************"""


###############
# IMPORTATION #
###############
import sys
import numpy as np
import pandas as pd
import datetime as dt


#####################
# COMPUTE THIRD WED #
#####################
def compute_third_wed(y,m):
	day = 21 - (dt.date(y, m, 1).weekday() + 4) % 7		# find the third weekday of the month, mon=0, sun=6
	return dt.date(y,m,day)


########
# MAIN #
########
"""
	main function
"""
def main():

	#---file handling---#
	try: file = str(sys.argv[1])
	except: raise ValueError('You must enter a file path!')
	# import os
	# if not os.path.isfile(file): raise ValueError('Illegal file path!')


	#---read data---#
	df = pd.read_csv(file, 
					encoding='big5',
					dtype=str,
					low_memory=True,
					skiprows=[0],
					na_values=['.'],
					names=['Date', 'P_ID', 'Due_month', 'Time', 'Price', 'Amount', 'Close_month_price', 'Far_month_price', 'Open_price'])
	date = df.Date.values
	p_id = df.P_ID.values
	due_month = df.Due_month.values
	time = df.Time.values
	price = df.Price.values
	del df
	assert len(date) == len(p_id) == len(due_month) == len(time) == len(price)


	#---compute date---#
	for i, d in enumerate(date):
		date[i] = d.strip()
	date = np.amax(date)
	
	month = int(date[0:6])
	third_wed = int(str(compute_third_wed(int(date[0:4]), int(date[4:6]))).split('-')[-1])
	if int(date[6:]) > third_wed:
		month += 1


	#---parse data---#
	data = []
	for idx in range(len(p_id)):
		if str(p_id[idx].strip()) == 'TX':
			try:
				if int(due_month[idx].strip()) == month:
					if int(time[idx].strip()) >= 84500 and int(time[idx].strip()) <= 134500:
						data.append(int(price[idx]))
			except:
				pass


	#---compute OHLC---#
	open_p = data[0]
	high_p = np.amax(data)
	low_p = np.amin(data)
	close_p = data[-1]
	print(open_p, high_p, low_p, close_p)


if __name__ == '__main__':
	main()

