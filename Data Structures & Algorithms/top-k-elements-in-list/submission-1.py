class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for a in nums:
            if a in res:
                res[a]+=1
            else:
                res[a] = 1
       #sorted(res.items(), key top = =lambda item: item[1], reverse=True).keys()[:k]
        top = [k for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True)[:k]]
        return top