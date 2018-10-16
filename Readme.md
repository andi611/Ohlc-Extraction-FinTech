# Fintech: OHLC Extraction
## The goal of this work is to compute the OHLC (open, high, low, close) prices of 台指期 within a given date based on minute-based trading record, implementation in Python.

## Description
The input file is a csv file recording minute-based trading data.
Download one of the .csv files and open it with MS Excel to see its contents, which should be self-explanatory.
In particular, we only focus on the 商品代號 of "TX", which is "台指期".
It is likely that we will have several transactions within a given minute. 
We can assume all the transactions listed within a given second is based on chronological order. 
As a result,
If several transactions occur in the very first minute of the day, then the price of the first transaction within the minute is the "open" price.
If several transactions occur in the very last minute of the day, then the price of the last transaction within the minute is the "close" price.
The entries containing double dates in 到期月份 are ignored directly.


## Usage:
```
"python3 ohlcExtract.py input.csv" 
```
This should print out the vector of ohlc in a line, with elements separated by a space.

Here are some test cases:
```
Daily_2018_08_20.csv ==> 10687 10715 10652 10671
Daily_2018_08_31.csv ==> 10975 11024 10953 11022
Daily_2018_09_28.csv ==> 11011 11039 10921 10955
Daily_2018_10_01.csv ==> 10968 11018 10966 11006
```