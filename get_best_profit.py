#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# IMPORTS
#
import argparse
import requests
#import re
#import json
#import os
#import xlsxwriter
#from xlsxwriter.utility import xl_rowcol_to_cell, xl_col_to_name
#from openpyxl import load_workbook
#import openpyxl

#
# String messages
#
STR_HELP_MAIN = 'Albion best profit calculator'
STR_HELP_ITEM_NAME = 'Item name'

#
# Formulas
#
# Fee = FeePercentage * ProductValue * 5 / 100</li><li>Profit = (ProductPrice - ResourcesCosts + (ResourcesCosts / 100 * ReturnRate) - Fee) * CraftAmount

def parse_args():

    # Create the main parser object to parse sys.argv
    parser = argparse.ArgumentParser(prog=__name__, description=STR_HELP_MAIN)

    # Path of xlsx file
    parser.add_argument('-in', '--item_name',
                        required=True,
                        help=STR_HELP_ITEM_NAME,
                        type=str)
    return parser.parse_args()

class AlbionItens(object):
    # api-endpoint
    __CHART = 'https://www.albion-online-data.com/api/v1/stats/Charts/'
    __PRICE = 'https://www.albion-online-data.com/api/v2/stats/Prices/'
    __VIEW = 'https://www.albion-online-data.com/api/v2/stats/View/'
  
    def __init__(self, item_name):
        self.current_item_name = item_name
    
    def get_best_profit(self):
        return self.__get_item_price(self.current_item_name)

    def __get_item_price(self, item_name):
        url = self.__PRICE + item_name
        r = requests.get(url = url)
        data = r.json()
        
        return data


#
# MAIN CODE
#
# Execute only if the context is the main
if __name__ == '__main__':

    # Get arguments
    args = parse_args()

    # Get best profit

    profit = AlbionItens(args.item_name)
    print(profit.get_best_profit())