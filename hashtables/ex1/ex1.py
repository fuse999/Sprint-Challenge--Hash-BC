#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16) # initialize hash table with 16 values

    for zeroth in range(0, length):# for every item in the given list
        first = hash_table_retrieve(ht, (limit-weights[zeroth]))
        if first != None:# if we find a match
            answer = [zeroth, first]
            # print(answer)
            return answer
        else:# If there is no match continue entering items
            hash_table_insert(ht, weights[zeroth], zeroth)
    # If such a pair doesn’t exist
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# print(answer_2)
