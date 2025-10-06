from datetime import datetime
import os
Enter_num = input("Enter Your Numbers:- ")

even_count = 0
log_path = "numbers_log.txt"
try:
    text_list = Enter_num.split(",")
    with open(log_path, "a+") as f:
    
        f.write("\n"+str(datetime.now().strftime("%d/%m/%Y/%H:%M:%S")) )
        f.write("\nEntered Numbers are:- " + str(text_list))
    num_list = []
    for i in text_list:
        num_list.append(int(i))
        if int(i)%2 == 0:
            even_count += 1

    print("max number is:- ", max(num_list))
    print("min number is:- ", min(num_list))
    print("Avearge number is :- ", sum(num_list)/len(num_list))
    print("Even Number count:- ", even_count)
    print("Odd Number count:- ", len(num_list)-even_count)

    with open(log_path, "a+") as f:
        f.write("\nmax number is:- "+str( max(num_list)))
        f.write("\nmin number is:- "+ str(min(num_list)))
        f.write("\nAvearge number is :- "+ str(sum(num_list)/len(num_list)))
        f.write("\nEven Number count:- "+ str(even_count))
        f.write("\nOdd Number count:- "+ str(len(num_list)-even_count))
except:
    print("Enter Integer number only")

finally:
    with open(log_path, "a+") as f:
        f.write("\n"+"="*50)