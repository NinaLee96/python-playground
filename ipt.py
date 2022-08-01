#           5/1    5/5    5/8
# META.     100    200    
# GOOG.             50   100
# AMZ.      300    100   200
#===============================
# Total.    400    350   500

# Input = [[("5/1", 100), ("5/5", 200)], 
# 	   [("5/5", 50), ("5/8", 100), 
# 	   [("5/1", 300), ("5/5", 100), ("5/8", 200)]

# Output = [("5/1", 400), ("5/5", 350), ("5/8", 500)]

# { "5/1": 100, "5/5": 200 }

import collections

# input = [[("5/1", 100), ("5/5", 200)], 
# 	   [("5/5", 50), ("5/8", 100)], 
# 	   [("5/1", 300), ("5/5", 100), ("5/8", 200)]]
input = [[("5/1", 100)], 
	   [("5/5", 50), ("5/8", 100)], 
	   [("5/1", 300), ("5/5", 100)]]

def get_total(lists):
    all_dates = set()
    hashtable = collections.defaultdict(set)

    for l in lists:
        for i in range(len(l)):
            date, _ = l[i]
            all_dates.add(date)            
    
    dates = sorted(all_dates)
    
    for i, l in enumerate(lists):
        for date, val in l:
            hashtable[i].add((date, val))

    temp_dates = dates
    for i in range(len(lists)):
        list_dates_vals = hashtable[i]
        for date_vals in list_dates_vals:
            date, vals = date_vals
            if date in temp_dates:
                temp_dates.remove(date)

        for d in temp_dates:
            hashtable[i].add((d, vals))
        temp_dates = dates
            
    result_table = collections.defaultdict(list)
    for val in hashtable.values():
        for pair in val:
            date, price = pair
            result_table[date].append(price)
    output = []
    for key, val in result_table.items():
        total = sum(val)
        output.append((key, total))
    return output
print(get_total(input))