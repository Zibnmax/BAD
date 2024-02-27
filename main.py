from datetime import datetime
import sys

NUMBERS_FILE_PATH = '10m.txt'

class MathSolver:
    
    def __init__(self, file_path: str = NUMBERS_FILE_PATH) -> None:
        self.file_path: str = file_path
        self.list_of_numbers: list = []
        try:
            with open(file=file_path, mode='r') as file:
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
            sys.exit(1)
            
    
    def find_min_max(self) -> tuple:
        min_ = min(self.list_of_numbers)
        max_ = max(self.list_of_numbers)
        return min_, max_
    
    def find_median(self) -> int|float:
        list_of_numbers_len = len(self.list_of_numbers)
        sorted_list = sorted(self.list_of_numbers)
        if list_of_numbers_len % 2 == 0:
            return (sorted_list[list_of_numbers_len // 2] + sorted_list[list_of_numbers_len // 2 - 1]) / 2
        return (sorted_list[list_of_numbers_len // 2])
    
    def find_average(self) -> float:
        return (sum(self.list_of_numbers) / len(self.list_of_numbers))
    
    def ascend(self):
        pass
    
    def descend(self):
        pass



if __name__ == '__main__':
    start = datetime.now()
    ms = MathSolver()
    r1 = datetime.now()
    print("file open", r1 - start)
    print(ms.find_min_max())
    r2 = datetime.now()
    print("min max", r2 - r1)
    print(ms.find_median())
    r3 = datetime.now()
    print("median", r3 - r2)
    print(ms.find_average())
    r4 = datetime.now()
    print("average", r4 - r3)

