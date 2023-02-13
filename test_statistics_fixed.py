#Name: Nhu Nhu Ly
#NSID: cvd326
#instructor's name: Eric Neufeld
#student number: 11333935
#course number: 27177
#lab section: Monday 1:30 - 2:50 - 28623

import Statistics as S


def close_enough(a, b, tolerance):
    """
    Purpose:
        Check if 2 floating point values are close enough to 
        be considered equal.  See the Addendum in the assignment!
    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value
    Post-Conditions:
        none
    Return:
        :return True if the difference between a and b is small
    """
    return abs(a - b) < tolerance


#####################################################################

def statistic_create():
    test_item = 'Statistics.create()'
    expected1 = 0
    reason1 = "Initial count value"
    
    stats = S.Statistics()
    result1 = stats.count()

    if result1 != expected1:
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected1, result1, reason1))
    
    else:
        print('The initial value, which is expected to be {}, is {}. Correct! -- {}'.format(expected1, result1, reason1))


    expected2 = 0
    reason2 = "Initial average value"

    # call the operation
    stats = S.Statistics()
    result2 = stats.mean()

    if result2 != expected2:
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected2, result2, reason2))

    else:
        print('The average value, which is expected to be {}, is {}. Correct! -- {}'.format(expected2, result2, reason2))

#####################
#Test count in add() operation

def test_count_add(value):
    stats = S.Statistics()

    #call the operation
    for i in value:
        stats.add(i)

    result = stats.count()

    #Check count after one value added
    test_item = 'count in add() operation'
    reason1 = "Check count after one value added"
    expected1 = 1

    if result == expected1:
        print('Testing {} - {} is inputted: expected to be {} - the result {}'.format(test_item,value, expected1,result))
        print('The operation works well!')

    #Check count after 3 values added
    
    test_item = 'count in add() operation'
    reason2 = "Check count after one value added"
    expected2 = 3

    if result == expected2:
        print('Testing {} - {} is inputted: expected to be {} - the result {}'.format(test_item,value, expected2,result))
        print('The operation works well!')

    if result != expected2 and result != expected1:
        print('Error in {} - {} is inputted'. format(test_item,value))
        print('The operation fails to meet the expectation...')

########################


main()
