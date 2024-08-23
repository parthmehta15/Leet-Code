#Assign dict
# The key is key and value is [[values, timestamps]] -> for set
# For get
#Check if key valid else return ''
# Now if key is valid
# Return perform binary search to find the index of current timestamp or the one before it
# Once found return the value at that index


class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key] += [[value, timestamp]]
        else:
            self.data[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:

        res = ''
        value_list = self.data.get(key, [])     
        left = 0
        right = len(value_list) - 1
        while left<=right:
            mid = (left + right)//2
            if value_list[mid][1] <= timestamp:
                res = value_list[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)