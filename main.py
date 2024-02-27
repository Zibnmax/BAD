from datetime import datetime
import sys

NUMBERS_FILE_DEFAULT_PATH = '10m.txt'


def time_measure(func):
    """Time measure decorator
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f'Elapsed time of function "{func.__name__}": {end_time - start_time}')
        return result
    return wrapper

class StatisticSolver:
    """Statistics calculating class. Requires '.txt' filename which contains INT numbers only (every number must be on a new line).
    """
    def __init__(self) -> None:
        self.list_of_numbers: list = []
        self.file_path: str = input(f'Enter file name to proceed or leave empty field to use default file name "{NUMBERS_FILE_DEFAULT_PATH}":\n')
        if not self.file_path:
            self.file_path = NUMBERS_FILE_DEFAULT_PATH
        try:
            with open(file=self.file_path, mode='r') as file:
                for line_count, line in enumerate(file):
                    try:
                        self.list_of_numbers.append(int(line))
                    except ValueError:
                        print(f'Failed to convert line ({line_count + 1}) to integer.')
                        continue
                    except Exception:
                        print('Something went wrong. Breaking now.')
                        break
        except FileNotFoundError:
            print('File not found.')
            raise
        except OSError:
            print('File is not reachable.')
            raise
        except Exception:
            raise("Something went wrong. Breaking now.")
        
        if not self.list_of_numbers:
            raise ValueError('File have no numbers to work with.')
            
    
    def max(self) -> int:
        """Finds max value in file.

        Returns:
            int: max value
        """
        return max(self.list_of_numbers)
    
    def min(self) -> int:
        """Finds min value in file.

        Returns:
            int: mmin value
        """
        return min(self.list_of_numbers)
    
    def median(self) -> int | float:
        """Finds median value of all numbers in file.

        Returns:
            int | float: median
        """
        list_of_numbers_len = len(self.list_of_numbers)
        sorted_list = sorted(self.list_of_numbers)
        if list_of_numbers_len % 2 == 0:
            return (sorted_list[list_of_numbers_len // 2] + sorted_list[list_of_numbers_len // 2 - 1]) / 2
        return (sorted_list[list_of_numbers_len // 2])
    
    def average(self) -> float:
        """Finds arithmetical average value of all numbers in file.

        Returns:
            float: arithmetical average
        """
        return (sum(self.list_of_numbers) / len(self.list_of_numbers))
    
    def ascend(self) -> list[int]:
        """Finds the longest chain of numbers in ascending order.

        Returns:
            list[int]: chain of numbers in ascending order
        """
        longest_list: list[int] = []
        current_list: list[int] = []
        for number in self.list_of_numbers:
            if not current_list:
                current_list.append(number)
                continue
            if number > current_list[-1]:
                current_list.append(number)
            else:
                if len(current_list) > len(longest_list):
                    longest_list = current_list.copy()
                current_list = [number]
        
        if len(current_list) > len(longest_list):
            longest_list = current_list.copy()
        return longest_list
    
    def descend(self) -> list[int]:
        """Finds the longest chain of numbers in descending order.

        Returns:
            list[int]: chain of numbers in descending order
        """
        longest_list: list[int] = []
        current_list: list[int] = []
        for number in self.list_of_numbers:
            if not current_list:
                current_list.append(number)
                continue
            if number < current_list[-1]:
                current_list.append(number)
            else:
                if len(current_list) > len(longest_list):
                    longest_list = current_list.copy()
                current_list = [number]
        
        if len(current_list) > len(longest_list):
            longest_list = current_list.copy()
        return longest_list

@time_measure
def main() -> None:
    nums = StatisticSolver()
    print(f'Max value: {nums.max()}')
    print(f'Min value: {nums.min()}')
    print(f'Median value: {nums.median()}')
    print(f'Average value: {nums.average()}')
    print(f'Longest ascend chain: {nums.ascend()}')
    print(f'Longest descend chain: {nums.descend()}')

if __name__ == '__main__':
    main()
