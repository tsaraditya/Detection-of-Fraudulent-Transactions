#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Here the distance_module and statistics_module are imported inorder to fetch functions from them.
import distance_module as mod
import statistics_module as modu
# defining an usder interface module for customer to interact with the functions.
def user_interface():
    # using while loop for looping the questions again until the customer decides to quit.
    while True:
        try:
            #Dispaying choices for the customer to select from
            print('\n')
            print("Dear customer welcome to our Transaction Analysis Tool")
            print("-------------------------------------------------------")
            print("Please choose from the below given choices,Thank You.")
            print('\n')
            print('DISTANCE')
            print("1. Calculate distance between two transactions of a single user")
            print("2. Calculate distance between two transactions of different users")
            print('\n')
            print('TRANSACTION')
            print("3. Calculate the average transactions of given user_id and all user_ids.")
            print("4. Calculate the mode of transactions of the given user_id and all user_ids")
            print("5. Calculate the median of transactions of the given user_id and all user_ids")
            print("6. Calculate the interquartile range of transactions of the given user_id and all user_ids")
            print("7. Calculate the Location Centroid of the given user_id, based on their Transaction Locations")
            print("8. Calculate the Standard Deviation of Transactions of the given user_id.")
            print("9. Detect whether the given transaction_id is fraudulent or not and also specify the details of that transaction_id")
            print("10. Find the abnormal transactions for the given user_id")
            print("11. Compute the Z score of transactions of the given user_id and all user_ids")
            print("12. Computes the frequencies of transactions at any given location")
            print("13. Calculate the nth percentiles of transactions of any user and all of users")
            print("14. Calculate the outliers of any location of any user")
            print("15. Quit")
            # Asking customer to enter a choice
            choice = int(input("Enter your choice: "))
            #if the customer choice is 1 then goes to distance module for single user transaction 

            if choice == 1:
                mod.single_user_Transaction()
            #if the customer choice is 2 then goes to distance module for different user transaction 
            elif choice == 2:
                mod.different_user_Transaction()
            #if the customer choice is 3 then goes to statistics module for finding average 
            elif choice == 3:
                modu.get_average()
            #if the customer choice is 4 then goes to statistics module for finding mode
            elif choice == 4:
                modu.get_mode()
            #if the customer choice is 5 then goes to statistics module for finding median
            elif choice == 5:
                modu.get_median()
            #if the customer choice is 6 then goes to statistics module for finding interquartile range
            elif choice == 6:
                modu.get_interquartile_range()
            #if the customer choice is 7 then goes to statistics module for finding location centroid
            elif choice ==7:
                modu.get_location_centroid()
            #if the customer choice is 8 then goes to statistics module for finding standard deviation
            elif choice == 8:
                modu.get_standard_deviation()
            #if the customer choice is 9 then goes to statistics module for checking whether fraudulent or not
            elif choice == 9:
                modu.is_fraudulent()
            #if the customer choice is 10 then goes to statistics module for finding abnormal transaction
            elif choice == 10:
                modu.get_abnormal_transaction()
            #if the customer choice is 11 then goes to statistics module for finding z scores
            elif choice == 11:
                modu.z_scores()
            #if the customer choice is 12 then goes to statistics module for finding location_frequency
            elif choice == 12:
                modu.get_location_frequency()
            #if the customer choice is 13 then goes to statistics module for finding nth percentile
            elif choice == 13:
                modu.get_nth_percentile()
            #if the customer choice is 14 then goes to statistics module for finding outliers.
            elif choice == 14:
                modu.get_outlier()
            #if the customer choice is 15 then quit the program.
            elif choice==15:
                print("Goodbye!")
                break
            else:
                #Otherwise prints invalid choice entered by the customer
                print("Sorry dear customer,Invalid choice, please try again.")
        # Raising Exceptions and providing suitable comments to be displayed
        except ValueError:
            print("Sorry dear customer,Please enter a valid input!!!.")
        except Exception:
            print("Sorry, dear customer. Some errors have occured")

