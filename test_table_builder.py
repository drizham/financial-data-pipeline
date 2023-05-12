import table_builder
from init_observability import init_kensu
init_kensu('table 0 builder') # sets the name of application in Kensu

lake = 'lake1/'
ticker = 'CL=F'
#        lake1/CL=F/interim0/we_2023-01-07.csv
input0 = 'interim0/we_2023-01-14.csv'
#full_path = '/Users/Izham/dev/kensu/financial-data-pipeline/lake1/CL=F/interim0/we_2023-01-14.csv'
table_builder.build0(lake, ticker, input0, 'table0.csv')