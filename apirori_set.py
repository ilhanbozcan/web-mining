import csv

data_set = []


with open('data.csv',encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',)
    for line in spamreader:
        data_set.append(set(line))

min_sup = 0.3
data_lenght = len(data_set)


## INITIAL STEP C1##
candidate_list = []
candidate = []

for set in data_set:
    for item in set:
        if item in candidate_list:
            pass
        else:
            candidate_list.append(item)

for item in sorted(candidate_list):
    candidate.append({item})


####################################


def get_frequent_list(candidate):
    item_count = []
    frequent_list = []
    ### New List to Count frequent

    for x in range(len(candidate)):
        item_count.append(0)

    ###Check minsup
    for index,item in enumerate(candidate):
        for transaction in data_set:
            if item.issubset(transaction):
                item_count[index] += 1


    for index,count in enumerate(item_count):
        if count/data_lenght >= min_sup:
            frequent_list.append(candidate[index])

    return frequent_list


def get_candidate_list(frequent_set):
    candidate = {}
    candidate_list = []
    candidate_sorted = []
    for frequent_item in frequent_set:
        frequent_item_list = list(frequent_item.copy())
        for frequent_item_next in frequent_set:
            frequent_item_next_list = list(frequent_item_next.copy())

            ###check same list
            if frequent_item_list == frequent_item_next_list:
                pass

            ###handle if 1 item in list
            elif len(frequent_item_list) == 1:
                candidate = frequent_item.union(frequent_item_next)

            ### union
            elif frequent_item_list[-1] < frequent_item_next_list[-1] and  frequent_item_list[:-1] == frequent_item_next_list[:-1]:
                candidate = frequent_item.union(frequent_item_next)

            ###check candidate list to dublicate and empty set
            if len(candidate) != 0 and candidate not in candidate_list:
                candidate_sorted = list(candidate)
                candidate.clear()

                for item in sorted(candidate_sorted):
                    candidate.add(item)

                candidate_list.append(candidate)


    return candidate_list


frequent_list = get_frequent_list(candidate)
print("C1 :  " ,candidate)
print("F1 :  " ,frequent_list)
num = 1
while (len(frequent_list) > 1):
    num +=1
    candidate = get_candidate_list(frequent_list)
    frequent_list = get_frequent_list(candidate)
    print("C" + str(num) + " " + ":  ", candidate)
    print("F" + str(num)+ " " +":  ", frequent_list)







