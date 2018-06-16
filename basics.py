file = open("US_births_1994-2003_CDC_NCHS.csv", 'r')
text = file.read()

# read the csv file given, format it accordingly, cast string fields
# to int, append these to a final list, return the resulting list
def read_csv(input):
    file = open(input, "r")
    string = file.read()
    line = string.split("\n")
    string_list = line[1:len(line)]
    final_list = []
    for item in string_list:
        int_fields = []
        string_fields = item.split(",")
        for field in string_fields:
            int_fields.append(int(field))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")

# return a dictionary that stores monthly total of births
def month_births(list):
    births_per_month = {}
    for item in list:
        month = item[1]
        births = item[4]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return births_per_month

cdc_month_births = month_births(cdc_list)

# return a dictionary containing the total number of births
# for each unique value in a specific column
def calc_counts(data,column):
    births_for_column = {}
    for item in data:
        key = item[column]
        births = item[4]
        if key in births_for_column:
            births_for_column[key] += births
        else:
            births_for_column[key] = births
    return births_for_column

cdc_year_births = calc_counts(cdc_list,0)
cdc_month_births = calc_counts(cdc_list,1)
cdc_dom_births = calc_counts(cdc_list,2)
cdc_dow_births = calc_counts(cdc_list,3)

'''
print("Yearly births")
print(cdc_year_births)
print("\n")
print("Monthly births")
print(cdc_month_births)
print("\n")
print("Births for each day of month")
print(cdc_dom_births)
print("\n")
print("Births for each day of week")
print(cdc_dow_births)  
'''

# print(cdc_year_births.values())


# calculate the min value for a dictionary given,
# return these in a dictionary
def calc_min(input_dict):
    first_key = list(input_dict.keys())[0]
    min = input_dict[first_key]
    max = input_dict[first_key]
    min_max_dict = {}
    for key, value in input_dict.items():
        if value < min:
            min = value
            min_max_dict["min"] = min
        if value > max:
            max = value
            min_max_dict["max"] = max
    return min_max_dict


print(cdc_year_births)
print(cdc_month_births)
print(cdc_dom_births)
print(cdc_dow_births)
print(calc_min(cdc_year_births))
print(calc_min(cdc_month_births))
print(calc_min(cdc_dom_births))
print(calc_min(cdc_dow_births))
