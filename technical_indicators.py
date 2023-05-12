# a list of technical indicators that can be added to
# depending how it is called a *.csv or a pandas df
import pandas as pd
import numpy as np

# TODO Move all indicators to a separate file
def add_stochastic_oscillator(df, periods=14):
    # REF: 
    copy = df.copy()
    
    high_roll = copy["High"].rolling(periods).max()
    low_roll = copy["Low"].rolling(periods).min()
    
    # Fast stochastic indicator
    num = copy["Close"] - low_roll
    denom = high_roll - low_roll
    copy["%K"] = (num / denom) * 100
    
    # Slow stochastic indicator
    copy["%D"] = copy["%K"].rolling(3).mean()
    
    return copy

def add_obv(df):
    copy = df.copy()
    # https://stackoverflow.com/a/66827219 (super code brah )
    copy["OBV"] = (np.sign(copy["Close"].diff()) * copy["Volume"]).fillna(0).cumsum()
    return copy

def add(indicator, input):
    # indicator technical indicator function to add
    # *.csv input file path to add to
    print(f'Adding {indicator} to: {input}')
    df = pd.read_csv(input)
    print(df.head(2))

    df = indicator(df)
    print(df.tail(2))

    df.to_csv('lake1/CL=F/TEMP-table0_bronze.csv')


    return

def main(indicator, input):
    add(indicator, input)
    return

main(add_obv, 'lake1/CL=F/table0_bronze.csv')