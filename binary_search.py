class BinarySearch:
    def __init__(self, nums: list[int], target) -> int:
        self.nums = nums
        self.target = target
    def searching(self) -> int:
        low_pointer = 0
        high_pointer = len(self.nums)

        while low_pointer <= high_pointer:
            mid = (low_pointer + high_pointer) // 2

            if self.nums[mid] == self.target:
                return mid
                
            
            elif self.nums[mid] < self.target: # Means the target number is located rigth of the middle array.
                low_pointer = mid + 1
            
            else:  # Means the target number is located left of the middle array.
                high_pointer = mid - 1

        return -1 # Target number isn't locate in input array.
    def __str__(self):
        return f"Target: {self.target}\nResultado da busca:\nNúmero buscado está na posicao: {self.searching()}"


search = BinarySearch(nums = [-1, 0, 3, 5, 9, 12], target = 9)
search.searching()
print(search)
