import json
from datetime import date
import requests
import os

class RatioObtainer:
    base = None
    target = None

    #Constants
    BASE_CURRENCY_PARAM = "base_currency"
    TARGET_CURRENCY_PARAM = "target_currency"
    DATE_PARAM = "date_fetched"
    RATIO_PARAM = "ratio"
    RATIOS_FILE_PATH = "ratios.json"
    
    def __init__(self, base, target):
        self.base = base
        self.target = target

    #Helpers
    def check_if_file_exists_and_not_empty(self):
        return os.path.isfile(self.RATIOS_FILE_PATH) and os.stat(self.RATIOS_FILE_PATH).st_size != 0
    
    def get_today_date_formated(self):
        return date.today().strftime('%Y-%m-%d')
    
    def check_if_base_and_target_identical(self, ratio):
        return ratio[self.BASE_CURRENCY_PARAM] == self.base and ratio[self.TARGET_CURRENCY_PARAM] == self.target
    
    def was_ratio_saved_today(self):
        exists = False
        if self.check_if_file_exists_and_not_empty():
            f = open(self.RATIOS_FILE_PATH, "r")
            ratios = json.load(f)
            for ratio in ratios:
                if self.check_if_base_and_target_identical(ratio) and ratio[self.DATE_PARAM] == self.get_today_date_formated():
                    exists = True
                    return True
                            
        if (not exists):
            return False 
         
        

    def fetch_ratio(self):
        url = 'https://api.exchangerate.host/latest'
        response = requests.get(url,  params={"base": self.base, "symbols": self.target})
        data = response.json()

        self.save_ratio(data["rates"][self.target])
        

    def save_ratio(self, ratioVal):
        exists = False
        
        if self.check_if_file_exists_and_not_empty():
            f = open(self.RATIOS_FILE_PATH, "r")
            ratios = json.load(f)
            
            for ratio in ratios:
                if self.check_if_base_and_target_identical(ratio):
                    exists = True
                    
                    ratioDoc = {
                        self.BASE_CURRENCY_PARAM : self.base,
                        self.TARGET_CURRENCY_PARAM : self.target,
                        self.DATE_PARAM : self.get_today_date_formated(),
                        self.RATIO_PARAM : ratioVal
                    }
                    
                    ratios.remove(ratio)
                    ratios.append(ratioDoc)
                    output = open(self.RATIOS_FILE_PATH, "w")
                    output.write(json.dumps(ratios, indent=4))
                    output.close()
                    break

            if not exists:
                ratios.append(
                    {
                        self.BASE_CURRENCY_PARAM : self.base,
                        self.TARGET_CURRENCY_PARAM : self.target,
                        self.DATE_PARAM : date.today().strftime('%Y-%m-%d'),
                        self.RATIO_PARAM : ratioVal
                    }
                )
                output = open("ratios.json", "w")
                output.write(json.dumps(ratios, indent=4))
                output.close()
        else:
            ratioDoc = [
                {
                    self.BASE_CURRENCY_PARAM : self.base,
                    self.TARGET_CURRENCY_PARAM : self.target,
                    self.DATE_PARAM : date.today().strftime('%Y-%m-%d'),
                    self.RATIO_PARAM : ratioVal
                }
            ]
            output = open("ratios.json", "a")
            output.write(json.dumps(ratioDoc, indent=4))
            output.close()
                    
        

    def get_matched_ratio_value(self):
        f = open("ratios.json", "r")
        ratios = json.load(f)
        for ratio in ratios:
            if ratio[self.BASE_CURRENCY_PARAM] == self.base and ratio[self.TARGET_CURRENCY_PARAM] == self.target:
                return ratio["ratio"]
        
        
