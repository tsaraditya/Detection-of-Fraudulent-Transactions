#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# (a)Average transactions of any user and all of the users
#importing the get_Transaction_data_set function from dataset_module

from dataset_module import get_Transaction_data_set

#defining the get_average function

def get_average():
    
    # Getting the transaction data using the get_Transaction_data_set function
    data = get_Transaction_data_set()

    # Asking for user input for the user_id to get average transaction for
    try:
        id = int(input("Enter the user_id: "))
    except ValueError:
        print("User ID must be a valid integer")
        return

    # Creating an empty dictionary to store the average transaction amount for each user
    user_amounts = {}

    # Creating an empty list to store all the transaction amounts for getting total average transaction
    all_amount = []

    # Looping through each user in the transaction data
    for user_id in data:

        # Getting all the transactions for the user
        transactions = data[user_id]

        # Creating an empty list to store the transaction amounts for the user
        amounts = []

        # Looping through each transaction for the user and getting the transaction amount
        for transaction in transactions.values():
            amounts.append(transaction["amount"])

            # Adding the transaction amount to the all_amount list
            all_amount.append(transaction["amount"])

        # If the user has no transactions, adding 0 to the user_amounts dictionary
        if len(amounts) == 0:
            user_amounts[user_id] = 0

        # Calculating the average transaction amount for the user and adding it to the user_amounts dictionary
        else:
            average_amount = sum(amounts) / len(amounts)
            user_amounts[user_id] = average_amount

    # Checking if the user_id entered by the user is valid and getting the average transaction amount for the user
    try:
        ave_user = user_amounts[id]

    # If the user_id is not valid, printing an error message and returning
    except KeyError:
        print("User ID %s does not exist in the transaction data" % id)
        return

    # Calculating the total average transaction amount for all users
    ave_total = sum(all_amount) / len(all_amount)

    # Printing the total average transaction amount
    print("Total Transaction Average is: %f" % ave_total)

    # Checking if the user_id entered by the user is valid and has transactions, getting the average transaction amount for the user
    try:
        ave_user = user_amounts[id]

    # If the user_id is not valid, printing an error message and returning
    except KeyError:
        print("User ID %s does not exist in the transaction data" % id)
        return

    # If the user_id has no transactions, printing an error message and returning
    except ZeroDivisionError:
        print("User ID %s has no transactions" % id)
        return

    # Printing the average transaction amount for the user
    print("The average transactions of user %s is %f" % (id, ave_user))
    return




# (b) A function to return the mode of transactions of any user and that of all users.
# import the function get_Transaction_data_set from the module dataset_module
from dataset_module import get_Transaction_data_set

# define a function mode that returns the mode (most common value) of a list of values
def mode(values):
    # initialize the mode variable to None
    mode = None
    # create an empty dictionary to store the frequency of each value
    freq_dict = {}
    # iterate over each value in the list
    for value in values:
        # if the value is already in the dictionary, increment its frequency
        if value in freq_dict:
            freq_dict[value] += 1
        # otherwise, add it to the dictionary with a frequency of 1
        else:
            freq_dict[value] = 1
        # if the current value has a higher frequency than the current mode, update the mode variable
        if mode is None or freq_dict[value] > freq_dict[mode]:
            mode = value
    # if the mode has a frequency of 1, return None
    if freq_dict[mode] == 1:
        return None
    # otherwise, return the mode
    return mode

# define a function get_mode that retrieves the mode of transaction amounts for a given user
def get_mode():
    # call the get_Transaction_data_set function to retrieve the transaction data
    data = get_Transaction_data_set()
    # prompt the user to enter a user ID and attempt to convert it to an integer
    try:
        id = int(input("Enter the user_id: "))
    # if the user enters an invalid integer, print an error message and return
    except ValueError:
        print("User ID must be a valid integer")
        return
    # create an empty dictionary to store the mode of transaction amounts for each user
    user_amounts = {}
    # create an empty list to store all transaction amounts
    all_amount = []
    # iterate over each user in the transaction data
    for user_id in data:
        # retrieve the transactions for the current user
        transactions = data[user_id]
        # create an empty list to store the transaction amounts for the current user
        amounts = []
        # iterate over each transaction for the current user
        for transaction in transactions.values():
            # add the amount of the current transaction to the amounts list
            amounts.append(transaction["amount"])
            # add the amount of the current transaction to the all_amount list
            all_amount.append(transaction["amount"])
        # calculate the mode of the transaction amounts for the current user
        mode_amount = mode(amounts)
        # add the mode of the transaction amounts to the user_amounts dictionary for the current user
        user_amounts[user_id] = mode_amount
    
    # attempt to retrieve the mode of transaction amounts for the specified user
    try:
        mod_user = user_amounts[id]
    # if the specified user ID does not exist in the transaction data, print an error message and return
    except KeyError:
        print("User ID %s does not exist in the transaction data" % id)
        return
    # if the mode of transaction amounts for the specified user is None, print an error message and return
    except TypeError:
        print("User ID %s has no mode for transaction amounts" % id)
        return
    
    # calculate the mode of all transaction amounts
    mod_total = mode(all_amount)
    # print the mode of all transaction amounts, or a message indicating that there is no mode if there are no repeated values
    print("Total Transaction mode is: %s" % (str(mod_total) if mod_total is not None else "No mode available as there are no same values repeated"))
    # print the mode of user transaction amounts, or a message indicating that there is no mode if there are no repeated values
    print("The mode of user %s is: %s" % (id, str(mod_user) if mod_user is not None else "No mode available as there are no same values repeated"))
  
  
 #(c) A function that returns the median of all transactions of a user and that of all users
# Importing the function get_Transaction_data_set from the module dataset_module
from dataset_module import get_Transaction_data_set

# Defining a function to calculate the median value from a list of values
def median(values):
    # Sorting the values in ascending order
    values.sort()
    # Getting the length of the values
    length = len(values)
    # Checking if the length is even or odd
    if length % 2 == 0:
        # If even, getting the two middle values
        mid = length // 2
        median = (values[mid - 1] + values[mid]) / 2
    else:
        # If odd, getting the middle value
        mid = length // 2
        median = values[mid]
    # Returning the median value
    return median

# Defining a function to get the median value for a given user ID
def get_median():
    # Calling the get_Transaction_data_set function to get the transaction data
    data = get_Transaction_data_set()
    # Asking the user to input a user ID
    try:
        id = int(input("Enter the user_id: "))
    except ValueError:
        print("User ID must be a valid integer")
        return
    # Creating an empty dictionary to store the median amounts for each user
    user_amounts = {}
    # Creating an empty list to store all the transaction amounts
    all_amount = []
    # Looping through each user in the transaction data
    for user_id in data:
        # Getting the transactions for the current user
        transactions = data[user_id]
        # Creating an empty list to store the amounts for the current user
        amounts = []
        # Looping through each transaction for the current user
        for transaction in transactions.values():
            # Adding the transaction amount to the amounts list
            amounts.append(transaction["amount"])
            # Adding the transaction amount to the all_amount list
            all_amount.append(transaction["amount"])
        # Calculating the median amount for the current user and adding it to the user_amounts dictionary
        median_amount = median(amounts)
        user_amounts[user_id] = median_amount
    # Getting the median amount for the specified user ID
    try:
        median_user = user_amounts[id]
    except KeyError:
        print("User ID %s does not exist in the transaction data" % id)
        return
    # Getting the median amount for all transactions
    median_total = median(all_amount)
    # Printing the median amount for all transactions and the median amount for the specified user ID
    print("Total Transaction median is: %f" % median_total)
    print("The median of user %s is %f" % (id, median_user))
    
# (d) A function that returns the interquartile range of transactions of a user and that of all users.   
# Importing the get_Transaction_data_set function from the dataset_module
from dataset_module import get_Transaction_data_set

# Defining the function to calculate the interquartile range
def get_interquartile_range():
    # Prompting the user to input a user ID and converting it to an integer
    try:
        id = int(input("Enter the user_id: "))
    except ValueError:
        # Printing an error message if the input cannot be converted to an integer
        print("User ID should be an integer")
        # Returning None to exit the function
        return
    
    # Getting the transaction data set using the get_Transaction_data_set function
    data = get_Transaction_data_set()
    
    # Creating a dictionary to store the median amounts for each user
    user_amounts = {}
    
    # Creating a list to store all transaction amounts
    all_amount = []
    
    # Looping through each user in the transaction data
    for user_id in data:
        # Getting the user's transactions
        transactions = data[user_id]
        # Creating a list to store the amounts for each transaction
        amounts = []
        # Looping through each transaction for the user
        for transaction in transactions.values():
            # Adding the amount for the transaction to the amounts list
            amounts.append(transaction["amount"])
            # Adding the amount for the transaction to the all_amount list
            all_amount.append(transaction["amount"])
        # Calculating the median amount for the user and adding it to the user_amounts dictionary
        median_amount = median(amounts)
        user_amounts[user_id] = median_amount
  
    # Sorting the all_amount list in ascending order
    sorted_all_amount = sorted(all_amount)
    
    # Calculating the index of the first quartile (Q1)
    n = len(sorted_all_amount)
    q1_index = int((n+1)/4) - 1
    # Calculating the value of the first quartile (Q1)
    q1 = sorted_all_amount[q1_index]
    
    # Calculating the index of the third quartile (Q3)
    q3_index = int(3*(n+1)/4) - 1
    # Calculating the value of the third quartile (Q3)
    q3 = sorted_all_amount[q3_index]
    
    # Calculating the interquartile range (IQR) for all users
    iqr = q3 - q1
    # Printing the interquartile range for all users
    print("Transaction interquartile range for all users is: %f" % iqr)
    
    # Checking if the user ID entered by the user exists in the transaction data
    if id in user_amounts:
        # Getting the user's transactions
        user_transactions = data[id]
        # Creating a list to store the amounts for each transaction for the user
        user_amounts = [transaction["amount"] for transaction in user_transactions.values()]
        # Sorting the user_amounts list in ascending order
        sorted_user_amounts = sorted(user_amounts)
        # Calculating the index of the first quartile (Q1) for the user
        n = len(sorted_user_amounts)
        q1_index = int((n+1)/4) - 1
        # Calculating the value of the first quartile (Q1) for the user
        q1 = sorted_user_amounts[q1_index]
        # Calculating the index of the third quartile (Q3) for the user
        q3_index = int(3*(n+1)/4)
        # Sorting in ascending order
        q3 = sorted_user_amounts[q3_index]
        user_iqr = q3 - q1
        # Printing the interquartile range for all users
        print("Transaction interquartile range for user %s is: %f" % (id, user_iqr))
    else:
        # otherwise print the interquartile range for the user not found
        print("User %s not found" % id)

        
# (e) A function that returns the location centroid of any user based on the transaction locations.         
# Importing the get_Transaction_data_set function from the dataset_module module
from dataset_module import get_Transaction_data_set

# Defining the location_centroid function
def get_location_centroid():
    # Calling the get_Transaction_data_set function to get the transaction data set
    data = get_Transaction_data_set()
    try:
        # Asking the user to enter the user_id as an integer
        id = int(input('Enter the user_id: '))
        # Retrieving the user's transactions from the data set
        user_transactions = data.get(id)
        # Checking if the user exists in the data set
        if user_transactions is None:
            print("User %s not found" % id)
            return
        # Creating empty lists to store the latitudes and longitudes of the user's transactions
        latitudes = []
        longitudes = []
        # Looping through the user's transactions and adding the latitudes and longitudes to their respective lists
        for transaction in user_transactions.values():
            latitudes.append(transaction["latitude"])
            longitudes.append(transaction["longitude"])
        # Calculating the centroid latitude and longitude by taking the average of the latitudes and longitudes, respectively
        centroid_latitude = sum(latitudes) / len(latitudes)
        centroid_longitude = sum(longitudes) / len(longitudes)
        # Printing the centroid latitude and longitude
        print("Centroid latitude: %f" % centroid_latitude)
        print("Centroid longitude: %f" % centroid_longitude)
    # Catching a ValueError if the user enters a non-integer value for the user_id
    except ValueError:
        print("Please enter a valid integer for user_id.")
    # Catching any other exceptions that may occur during the calculation of the centroid
    except Exception:
        print("An error occurred while calculating the centroid.")


# (f) A function that returns the standard deviation of any specif user's transactions.     
# Import the function get_Transaction_data_set from a module named dataset_module
from dataset_module import get_Transaction_data_set

# Define a function named get_standard_deviation
def get_standard_deviation():
    try:
        # Call get_Transaction_data_set function to get a dictionary of user transactions
        data = get_Transaction_data_set()
        
        # Prompt the user to enter a user ID and convert it to an integer
        id = int(input('Enter the user_id: '))
        
        # Get the user's transactions from the dictionary
        user_transactions = data.get(id)
        
        # Check if the user ID entered is valid, and if not, print an error message and return
        if user_transactions is None:
            print("User %s not found" % id)
            return
        
        # Create an empty list to store the amounts of the user's transactions
        amounts = []
        
        # Loop through the user's transactions and append each transaction amount to the `amounts` list
        for transaction in user_transactions.values():
            amounts.append(transaction["amount"])
        
        # Calculate the mean price of the user's transactions
        mean_price = sum(amounts) / len(amounts)
        
        # Calculate the variance of the user's transactions
        variance = 0
        for amount in amounts:
            variance += (amount - mean_price) ** 2
        variance /= len(amounts)
        
        # Calculate the standard deviation of the user's transactions
        standard_deviation = variance ** 0.5
        
        # Print the standard deviation of the user's transactions
        print("Standard deviation of amounts for user %s: %f" % (id, standard_deviation))
    
    # Catch a valueError exception if the user ID entered is not a valid integer
    except ValueError:
        print("Error: Invalid user ID entered. Please enter a valid integer ID.")
    
    # Catch a ZeroDivisionError exception if the user has no transactions
    except ZeroDivisionError:
        print("Error: User has no transactions.")
    
    # Catch all other exceptions and print an error message
    except Exception:
        print("An error occurred while calculating standard deviation:")


# (g) A function that returns the standard deviation of any specif user's transactions. 
# Import the function get_Transaction_data_set from a module named dataset_module
from dataset_module import get_Transaction_data_set

# Define a function named is_fraudulent
def is_fraudulent():
    try:
        # Call get_Transaction_data_set function to get a dictionary of user transactions
        data = get_Transaction_data_set()
        
        # Prompt the user to enter a transaction ID and convert it to an integer
        id = int(input('Enter the Transaction_id: '))
        
        # Initialize a transaction variable to None
        transaction = None
        
        # Loop through each user's transactions in the data dictionary and check if the transaction ID is present
        for user_transactions in data.values():
            if id in user_transactions:
                transaction = user_transactions[id]
                break
        
        # Check if the transaction ID entered is valid, and if not, print an error message and return
        if transaction is None:
            print("Transaction %s not found" % id)
            return
        
        # Get the is_fraudulent value from the transaction
        is_fraudulent = transaction.get("is_fraudulent")
        
        # Check if the is_fraudulent value is present, and if not, print an error message and return
        if is_fraudulent is None:
            print("is_fraudulent not found in transaction %s" % id)
            return
        
        # If the is_fraudulent value is True, print a message indicating the transaction is fraudulent and its details
        if is_fraudulent:
            print("Transaction %s is fraudulent" % id)
            print("Details of transaction:")
            print(transaction)
        
        # Otherwise, print a message indicating the transaction is not fraudulent
        else:
            print("Transaction %s is not fraudulent" % id)
    
    # Catch a ValueError exception if the transaction ID entered is not a valid integer
    except ValueError:
        print("Invalid input: please enter a valid integer for Transaction_id")
    
    # Catch all other exceptions and print an error message
    except:
        print("Sorry an error occurred")

        
# (h) A function that returns the abnormal transaction of any given user. 
# Import the function get_Transaction_data_set from a module named dataset_module
from dataset_module import get_Transaction_data_set

# Define a function named get_abnormal_transaction
def get_abnormal_transaction():
    try:
        # Prompt the user to enter a user ID and convert it to an integer
        id = int(input('Enter the user_id: '))
        
        # Call get_Transaction_data_set function to get a dictionary of user transactions
        data = get_Transaction_data_set()
        
        # Get the transactions for the specified user from the data dictionary
        user_transactions = data.get(id)
        
        # Check if the specified user exists in the data dictionary, and if not, print an error message and return
        if user_transactions is None:
            print("User %s not found" % id)
            return
        
        # Extract a list of all transaction amounts for the specified user
        amounts = [transaction["amount"] for transaction in user_transactions.values()]
        
        # Calculate the average transaction amount for the specified user
        average_amount = sum(amounts) / len(amounts)
        
        # Calculate the standard deviation of transaction amounts for the specified user
        std_dev = (sum((amount - average_amount) ** 2 for amount in amounts) / len(amounts)) ** 0.5
        
        # Create an empty list to store abnormal transactions
        abnormal_transactions = []
        
        # Loop through each transaction for the specified user and check if it is an outlier
        for transaction_id, transaction in user_transactions.items():
            # Use the 3 sigma outlier rule to determine if a transaction is an outlier
            if abs(transaction["amount"] - average_amount) > 3 * std_dev:
                abnormal_transactions.append((transaction_id, transaction))
        
        # If there are abnormal transactions, print them along with their IDs
        if abnormal_transactions:
            print("Abnormal transactions for user %s:" % id)
            for transaction_id, transaction in abnormal_transactions:
                print("%s: %s" % (transaction_id, transaction))
        
        # If there are no abnormal transactions, print a message indicating so
        else:
            print("No abnormal transactions found for user %s" % id)
    
    # Catch a ValueError exception if the user ID entered is not a valid integer
    except ValueError:
        print("Error: Invalid user ID entered.")
    
    # Catch all other exceptions and print an error message
    except Exception:
        print("An error occurred while processing the data.")
        
# (i) A function that computes the Zscore of any user's transactions and for all users transactions.         
# Importing the get_Transaction_data_set function from the dataset_module module
from dataset_module import get_Transaction_data_set

# Defining a function to calculate z-scores
def z_scores():
    try:
        # Getting the transaction data set
        data = get_Transaction_data_set()
        
        # Prompting the user to enter a user ID and converting the input to an integer
        id = int(input('Enter the user_id: '))
        
        # Initializing variables to store all transactions, specific z-scores, and all transaction z-scores
        all_transactions = []
        user_z_scores = []
        all_z_scores = []

        # Calculating z-scores for a specific user
        user_transactions = data.get(id)
        if user_transactions:
            # Creating a list of all transaction amounts for the user
            amounts = []
            for transaction in user_transactions.values():    
                amounts.append(transaction["amount"])
            
            # Calculating the mean and standard deviation of the transaction amounts for the user
            mean_amount = sum(amounts) / len(amounts)
            std_amount = (sum((amount - mean_amount) ** 2 for amount in amounts) / len(amounts)) ** 0.5
            
            # Calculating z-scores for each transaction for the user
            for transaction in user_transactions.values():
                z_score = (transaction["amount"] - mean_amount) / std_amount
                user_z_scores.append(z_score)
                
            # Printing the user-specific z-scores
            print("Z scores for user {}:".format(id), user_z_scores)
        else:
            print("User {} not found".format(id))

        # Calculating z-scores for all users
        for user_transactions in data.values():
            # Creating a list of all transaction amounts for each user
            amounts = []
            for transaction in user_transactions.values():    
                amounts.append(transaction["amount"])
            
            # Calculating the mean and standard deviation of the transaction amounts for each user
            mean_amount = sum(amounts) / len(amounts)
            std_amount = (sum((amount - mean_amount) ** 2 for amount in amounts) / len(amounts)) ** 0.5
            
            # Calculating z-scores for each transaction for each user
            for transaction in user_transactions.values():
                z_score = (transaction["amount"] - mean_amount) / std_amount
                all_z_scores.append(z_score)
                
        # Printing the z-scores for all users
        print("\nZ scores for all users:", all_z_scores)

    except ValueError:
        # Handling the ValueError exception in case the user enters an invalid user ID
        print("Error: Invalid user ID entered. Please enter a valid integer ID.")
    except Exception:
        # Handling any other exceptions that may occur during the execution of the function
        print("An error occurred while calculating Z scores:")


# (j) A function that computes those frequencies of transactions at any given location. 
    
# Importing the get_Transaction_data_set function from the dataset_module module
from dataset_module import get_Transaction_data_set

# Defining a function to get the frequency of transactions at a given location
def get_location_frequency():
    try:
        # Getting the transaction data set
        data = get_Transaction_data_set()
        
        # Prompting the user to enter the latitude and longitude of the location
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))
        
        # Creating a tuple to represent the location
        location = (latitude, longitude)
        
        # Initializing a variable to store the total frequency of transactions at the location
        total_frequency = 0
        
        # Iterating over each user and their transactions in the transaction data set
        for user_id in data:
            for transaction_id in data[user_id]:
                # Checking if the transaction location matches the given location
                transaction = data[user_id][transaction_id]
                if (transaction["latitude"], transaction["longitude"]) == location:
                    # Incrementing the total frequency if the transaction location matches the given location
                    total_frequency += 1
        
        # Printing the total frequency of transactions at the location
        print("The total transaction frequency at location ({}, {}) is: {}".format(latitude, longitude, total_frequency))
    
    # Handling various exceptions that may occur during the execution of the function
    except ValueError:
        print("Error: Invalid latitude or longitude entered. Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero occurred. Please check the input values.")
    except TypeError:
        print("Error: Type mismatch occurred. Please check the input values.")
    except:
        print("An error occurred while processing the data.")

        
# (l) A function that returns the nth percentiles of transactions of any user and all of users
# Import the get_Transaction_data_set function from the dataset_module
from dataset_module import get_Transaction_data_set

# Define a function to calculate the nth percentile of transaction amounts
def get_nth_percentile():
    
    # Get the transaction data using the get_Transaction_data_set function
    data = get_Transaction_data_set()
    
    # Prompt the user to enter a user ID and a percentile
    try:
        user_id = int(input("Enter the user_id: "))
        n = int(input("Enter the percentile (0-100): "))
    # If the user input is not valid, print an error message and return
    except ValueError:
        print("User ID and percentile must be valid integers")
        return
    
    # Calculate the nth percentile for a specific user
    if user_id in data:
        # Get all the transaction amounts for the user
        transactions = data[user_id]
        amounts = [transaction["amount"] for transaction in transactions.values()]
        
        # If the user has no transactions, print an error message and return
        if len(amounts) == 0:
            print("User ID %s has no transactions" % user_id)
            return
        
        # Sort the transaction amounts in ascending order
        amounts.sort()
        
        # Calculate the index of the nth percentile and get the value at that index
        index = int(n/100 * len(amounts))
        percentile = amounts[index]
        
        # Print the nth percentile for the user
        print("The %dth percentile of user %s is: %f" % (n, user_id, percentile))
    
    # If the user ID is not found in the transaction data, print an error message
    else:
        print("User ID %s does not exist in the transaction data" % user_id)
    
    # Calculate the nth percentile for all users
    all_amounts = [transaction["amount"] for transactions in data.values() for transaction in transactions.values()]
    
    # If there are no transactions in the data, print an error message and return
    if len(all_amounts) == 0:
        print("No transactions found in the dataset")
        return
    
    # Sort all transaction amounts in ascending order
    all_amounts.sort()
    
    # Calculate the index of the nth percentile and get the value at that index
    index = int(n/100 * len(all_amounts))
    percentile = all_amounts[index]
    
    # Print the nth percentile for all transactions
    print("The %dth percentile of all transactions is: %f" % (n, percentile))

    

# (k) A function that returns the outliers of any location and and of any user
from dataset_module import get_Transaction_data_set
# Importing the get_Transaction_data_set function from the dataset_module

def get_outlier():
    # Defining a function called get_outlier
    id=int(input('enter the user_id'))
    # Taking user input for the user id and converting it to an integer

    data = get_Transaction_data_set()
    # Retrieving the transaction data set using the get_Transaction_data_set function

    user_transactions = data.get(id)
    # Retrieving the transactions for the given user id

    if user_transactions is None:
        # Checking if the user exists in the data set
        print("User %s not found" % id)
        return
    # Returning if the user is not found in the data set

    latitudes = []
    longitudes = []
    # Creating empty lists to store the latitudes and longitudes of the user's transactions

    for transaction in user_transactions.values():
        # Looping through the user's transactions
        latitudes.append(transaction["latitude"])
        longitudes.append(transaction["longitude"])
        # Adding the latitudes and longitudes to their respective lists

    Lat_user = sum(latitudes) / len(latitudes)
    long_user = sum(longitudes) / len(longitudes)
    # Calculating the centroid latitude and longitude by taking the average of the latitudes and longitudes, respectively

    print("Centroid latitude: %f" % Lat_user)
    print("Centroid longitude: %f" % long_user)
    # Printing the centroid latitude and longitude

    distance_dict = {}
    # Creating an empty dictionary to store distances between the user's transactions and other transactions
    distance_ls = []
    # Creating an empty list to store distances between the user's transactions and other transactions

    for user_id in data:
        # Looping through the transaction data set to compare the user's transactions with others
        transactions = data[user_id]

        if id == user_id:
            # Skipping the user's own transactions
            for i in transactions.keys():
                # Looping through the user's transactions
                latitude = (transactions[i]["latitude"])
                longitude = (transactions[i]["longitude"])
                # Retrieving the latitude and longitude of the transaction
                distance = ((latitude - Lat_user)**2 + (longitude - long_user)**2)
                # Calculating the distance between the transaction and the user's centroid
                distance_ls.append(distance)
                # Adding the distance to the distance list
                distance_dict[i] = distance
                # Adding the distance to the distance dictionary with the transaction ID as the key

    index1 = len(sorted(distance_ls))*.25
    # Calculating the index of the first quartile
    Q1 = sorted(distance_ls)[round(index1)-1]
    # Calculating the first quartile
    index3 = len(sorted(distance_ls))*.75
    # Calculating the index of the third quartile
    Q3 = sorted(distance_ls)[round(index3)-1]
    # Calculating the third quartile
    IQR = Q3 - Q1
    # Calculating the interquartile range
    OutlierLocations =[]
    # Creating an empty list to store outlier locations
    for i in distance_ls:
        # Looping through the distance list
        if i > (Q3 + (1.5 * IQR)) or i < (Q1 - (1.5*IQR)):
            # Checking if the distance is an outlier
            OutlierLocations.append(i)
            # Adding the distance to the outlier list
    keys = []
     # return the transaction keys for the outlier locations
    for value in distance_dict.values():
        if value in OutlierLocations:
            for key, val in distance_dict.items():
                if val == value:
                    keys.append(str(key))
    return print("The outlier transactions ids are :",keys)

