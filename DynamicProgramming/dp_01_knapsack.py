# https://www.youtube.com/watch?v=cJ21moQpofY
# list of value: weight pair tuple
import pprint

items = (
    (2, 3),
    (2, 1),
    (4, 3),
    (5, 4),
    (3, 2)
)


# iterate over items
def knapsack(target_weight: int) -> list:
    # initialize 2D matrix of item\max capacity with 0s (including empty sack)
    # first row is made out of 0 as for no item there would be no value for any size of the sack (empty sack case)
    value_table = [[0 for _ in range(target_weight + 1)] for _ in range(len(items) + 1)]
    # for every item
    for i, (value, weight) in enumerate(items, 1):
        # for every size of sack
        for j in range(target_weight + 1):  # j => sack_size
            condition = ""
            # if sack is big enough to fit current item
            if j >= weight:
                condition = "if"
                # choose maximum between storing just current item add solution for the leftover space
                value_table[i][j] = max(
                    value,  # value of the item itself
                    value + value_table[i - 1][j - weight]  # check if we still can fit leftover weight [j
                )
            else:
                condition = "else"
                # we store the solution for the previous (smaller) item
                value_table[i][j] = value_table[i - 1][j]

            message = f"for item {i} size {weight} in {j} size sack =  {value_table[i][j]} - {condition}"
            # print(message)
    return value_table


# read the table
def read_the_table(table_to_read) -> list:
    """

    :param table_to_read: 2D matrix with value solutions
    :return:
    """
    answer = []

    j = len(table_to_read[0]) - 1
    for i in range(len(table_to_read)-1, 0, -1):
        # if the value is different it means that current item has been included
        # because the value got changed by it
        if table_to_read[i][j] != table_to_read[i - 1][j]:
            answer.append(items[i - 1])
            # we use i - 1 to exclude the empty sack case
            weight_of_current_item = items[i-1][1]
            j -= weight_of_current_item

    return answer


if __name__ == "__main__":
    result = knapsack(7)
    pprint.pprint(result)
    items_list = read_the_table(result)
    print(items_list)