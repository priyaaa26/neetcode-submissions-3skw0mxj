class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for val in nums:
            if val not in freq:
                freq[val] = 1
            else:
                freq[val] += 1 
        #[1,2,2,3,3,3], freq = {1:1, 2:2, 3:3}

        res = [] # [ 0,0,0,0,0,0]
        for i, val in freq.items():
            res.append([val, i])
        res.sort()

        r = []
        while len(r) <k:
            r.append(res.pop()[1])
        return r

        


                
        

