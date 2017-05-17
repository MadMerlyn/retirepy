# -*- coding: utf-8 -*-
"""
Investment Growth Calculator
@author: MadMerlyn
"""

def Invest(principle, reg_payments, rate, **period):
    """Principle, + regular (monthly) payments, and rate in APR (eg. 0.08)
    for period use either 'years=XX' or 'months=XX'
    --Prints estimated growth schedule based on anticipated rate of return
    --Always prints schedule in years regardless of period selection"""
    p = principle #clone value for growth calculation
    r = rate/12   #reduce APR to MPR

    if 'years' in period:
        period = (period['years']*12)+1
    elif 'months' in period:
        period = period['months']+1
    else:
        period = 361

    results = []
    for t in range(period):
        balance = p*(1-r**(t+1))/(1-r)      #expression for generating interest
        if t != 0:
            p = balance + reg_payments          #maintain total investment cost
            principle = principle + reg_payments  #update principle amount
        growth = p - principle               #calculate total interest
        
        invest_data = { #create dict for graphing
                'period' : t,
                'total' : format(p, '.2f'),
                'invested' : format(principle, '.2f'),
                'interest' : format(growth, '.2f')
                }  
        results.append(invest_data) #append dicts to results table
        if t % 60 == 0 and t != 0:
            print("Balance after", int(t/12), "years:", format(p, '.2f'))
            print("    Total invested:", format(principle, '.2f'))
            print("    Total interest:", format(growth, '.2f'))

    print("Expected annual interest on final balance:")
    print("                   ", format(p*rate, '.2f'))
    
    return results

if __name__ == '__main__':
    principle = int(input('Enter starting principle: '))
    payment = int(input('Enter monthly payments: '))
    rate = float(input('Enter expected APR: '))

    Invest(principle, payment, rate)
