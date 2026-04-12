import yfinance as yf
import pandas as pd
import numpy as np

def find_crossovers():
    """
    Pobierz dane BTC-USD od 2024-01-01 do 2025-11-20, oblicz 50-dniowa i 200-dniowa srednia kroczaca, 
    zidentyfikuj punkty przeciecia i zwroc liste dat tych przeciec.
    
    Returns:
        list: Lista dat przeciec w formacie 'YYYY-MM-DD'.
    """

    btc_data = yf.download('BTC-USD', start='2024-01-01', end='2025-11-20', auto_adjust=False)

    btc_data['50-day MA'] = btc_data['Close'].rolling(window=50).mean()
    btc_data['200-day MA'] = btc_data['Close'].rolling(window=200).mean()

    diff = btc_data['50-day MA'] - btc_data['200-day MA']
    crossover_mask = (diff.shift(1) * diff < 0) & (~diff.isna())

    crossover_dates = btc_data.index[crossover_mask].strftime('%Y-%m-%d').tolist()
    
    return crossover_dates



def calculate_total_btc_traded():
    """
    Pobierrz dane BTC-USD z okresu 2024-01-01 do 2025-11-20, oblicz liczbe BTC handlowanych w każdym dniu
    oraz zwroc liczbe BTC dla dnia z najwyższym wolumenem.
    
    Returns:
        int: liczba BTC handlowanych w dniu z najwyz�szym wolumene
    """

    btc_data = yf.download('BTC-USD', start='2024-01-01', end='2025-11-20', auto_adjust=False)

    btc_data['BTC_traded'] = btc_data['Volume'] / btc_data['Close']

    max_btc = int(btc_data['BTC_traded'].max())

    return max_btc


if __name__ == '__main__':
    crossover_dates = find_crossovers()
    total_traded = calculate_total_btc_traded()
    
    print(" ".join(crossover_dates))
    print(total_traded)

