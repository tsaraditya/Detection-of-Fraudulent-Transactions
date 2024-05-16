#!/usr/bin/env python
# coding: utf-8

# In[10]:



def get_Transaction_data_set():
    
    try:
# initialize an empty dictionary to store transaction data
        Trans = {}
    # to open the Transaction.txt file
        with open('Transaction.txt') as f:
            for line in f:
                # split the line into a list of data items
                data = line.strip().split(":")
                # extract the user ID, transaction ID, description, amount, latitude, longitude, and is_fraudulent status from the data list
                user_id = int(data[0])
                transaction_id = int(data[1])
                description = data[2]
                amount = float(data[3])
                latitude = float(data[4])
                longitude = float(data[5])
                is_fraudulent = data[6].lower() == 'true'

# if the user ID is not already in the dictionary, add it with an empty dictionary as its value
                if user_id not in Trans:
                    Trans[user_id] = {}
               # add the transaction data to the dictionary for the user ID
                Trans[user_id][transaction_id] = {
                    "description": description,
                    "amount": amount,
                    "latitude": latitude,
                    "longitude": longitude,
                    'is_fraudulent': is_fraudulent
                }
 # handling exception file not found errors with a message
    except FileNotFoundError:
        print("The dataset is not found")
# handling exception syntax error with a message
    except SyntaxError:
        print("Manipulation of code is not allowed")
# handling some other exceptions with a message
    except:
        print("Some other error")
         
# Returns the dictionary
    return Trans    
            


# In[ ]:





# In[ ]:




