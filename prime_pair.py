
Enter_num = input("Enter Your Numbers:- ")
try:
    text_list = Enter_num.split(",")
    num_list = []
    for i in text_list:
        num_list.append(int(i))

    prime_nums = [2,3,5,7,11,13,17,19,21,23,29,31,37,41,43,47,53,61,67,71,73,79,83,91,93]
    pair_list = []
    for i in range(len(num_list)):
        for j in num_list[i+1:]:
            if (num_list[i]+j) in prime_nums:
                print(num_list[i],"+", j)
                pair_list.append((num_list[i],j))

    print("Total number of pair:- ", len(pair_list))
except:
    print("Enter Integer Numbers")