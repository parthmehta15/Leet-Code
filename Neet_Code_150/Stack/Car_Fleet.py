#Pair [pos, speed] make a list and sort -> .sort sorts based on first item in list of list -> In this case pos
#First find time to destination and make a list
#Then see in reverse order if time to reach is greater than previous car than make time same for both equal to greater value(more time)
#At the end find unique times list-> set



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        data = [[pos, spd] for pos, spd in zip(position, speed)]
        data.sort() #This sorts based on first item in list of list
        time_to_dest = []
        for i in range(len(position)):
            time = (target - data[i][0]) / data[i][1]
            time_to_dest.append(time)
        fleet = 0
        for i in reversed(range(len(time_to_dest)-1)): 
            if time_to_dest[i] <= time_to_dest[i+1]:
                time_to_dest[i] = time_to_dest[i+1]

        return len(set(time_to_dest))
        