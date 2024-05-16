#!/usr/bin/env python
# coding: utf-8

# In[10]:



# import the get_Transaction_data_set function from the dataset_module
from dataset_module import get_Transaction_data_set

# define a function to calculate the distance between two transactions of the same user
def single_user_Transaction():
    try:
        # get user id and transaction ids as inputs
        user_id = int(input('Enter the user_id: '))
        transaction_id1 = int(input('Enter the transaction id 1: '))
        transaction_id2 = int(input('Enter the transaction id 2: '))
        
        # get the transaction data using the get_Transaction_data_set function
        data = get_Transaction_data_set()
        
        # get the two transactions using user id and transaction ids
        transaction1 = data[user_id][transaction_id1]
        transaction2 = data[user_id][transaction_id2]
        
        # get the latitude and longitude values from the transactions
        x1, y1 = transaction1['latitude'], transaction1['longitude']
        x2, y2 = transaction2['latitude'], transaction2['longitude']
        
        # calculate the distance between the two transactions using the distance formula
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        
        # print the calculated distance
        return print('The distance is', distance)
    
    # handle the possible errors that may occur during the execution of the function
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except KeyError:
        print("Invalid user_id or transaction_id. Please try again.")
    except TypeError:
        print("Invalid transaction data. Please check the data types of latitude and longitude values.")
    except ZeroDivisionError:
        print("Division by zero occurred during distance calculation.")
    except:
        print("Sorry a different kind of Error occurred!!!")

# define a function to calculate the distance between two transactions of different users
def different_user_Transaction():
    try:
        # get user ids and transaction ids as inputs
        user1 = int(input('Enter the user_id 1: '))
        user2 = int(input('Enter the user_id 2: '))
        transaction_id1 = int(input('Enter the transaction id 1: '))
        transaction_id2 = int(input('Enter the transaction id 2: '))
        
        # get the transaction data using the get_Transaction_data_set function
        data = get_Transaction_data_set()
        
        # get the two transactions using user ids and transaction ids
        transaction1 = data[user1].get(transaction_id1)
        transaction2 = data[user2].get(transaction_id2)
        
        # check if the transactions are from the same user, and if so, return an error message
        if not transaction1 or not transaction2:
            return print("Transaction in same user id, please use single_user_Transaction")

        # get the latitude and longitude values from the transactions
        x1, y1 = transaction1["latitude"], transaction1["longitude"]
        x2, y2 = transaction2["latitude"], transaction2["longitude"]
        
        # calculate the distance between the two transactions using the distance formula
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        
        # print the calculated distance
        return print('The distance is', distance)
    
    # handle the possible errors that may occur during the execution of the function
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except KeyError:
        print("Invalid user_id or transaction_id. Please try again.")
    except TypeError:
        print("Invalid transaction data. Please check the data types of latitude and longitude values.")
    except ZeroDivisionError:
        print("Division by zero occurred during distance calculation.")
    except:
        print("Sorry a different kind of Error occured!!!")