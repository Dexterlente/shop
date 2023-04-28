# Problem 1:
def is_palindrome(value: str) -> bool:
    '''
        Check whether a given string is a palindrome or not

        Parameters: value: str
        Returns: bool
    '''
    return value ==  value[::-1]

palindrome_test_values = ('mom', 'father', 'mother', 'deified')

for value in palindrome_test_values:
    # palindrome_value = is_palindrome(value)
    print(f'Checking if "{value}"" is palindrome: {is_palindrome(value)}')

# Problem 2:


def get_consecutive_zero_sum_combinations(values):
    '''
        Returns a combination of three consecutive element where their sum is
        equal to zero

        Parameters: List[int]
        Returns: List[List[int]]
    '''

zero_sum_test_values = [-1, 0, 1, 2, -1, -4, 5]

    for i in range(len(values)):
        for j in range(i+1, len(values)+1)
            list = values[i:j]
        if sum(list) == 0:
            
    return zero_sum_test_values


results = get_consecutive_zero_sum_combinations(zero_sum_test_values)

for result in results:
    print(
        f'Combinations [{", ".join([str(num) for num in result])}] is equal to zero')


# Problem 3:
def is_power_of_three(num: int) -> bool:
    '''
        Check whether a given integer is a power of three

        Parameters: num: int
        Returns: bool
    '''

    if num <= 0:
        return False
    while num % 3 == 0:
        num //=3
    return True if num == 1
    
power_of_three_test_values = (1, 6, 13, 81, 7, 3)

for value in power_of_three_test_values:
    print(
        # f'Checking if "{value}"" is a power of three: {is_power_of_three(value)}'
        )
    if is_power_if_three(valuevalue)
        print(f"{value}: True")
    else:
        print{f"{value}: False")

# Problem 4:
class MySqlDatabase:
    def insert(self, data):
        print('Inserted data using MySql')


class MsSqlDatabase:
    def insert(self, data):
        print('Inserted data using MsSql')


class UserManagerService:
    def __init__(self, database):
        self.database = database

    def create(self, data):
        self.database.insert(data)


data = {
    'first_name': 'Jane',
    'last_name': 'Doe'
}

database = MySqlDatabase()
service = UserManagerService(database=database)
service.create(data)