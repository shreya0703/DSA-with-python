class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def subsequence(idx , arr,curr):
            if idx>=len(arr):
                result.append(curr[:])
            
                return
            curr.append(arr[idx])
            subsequence(idx+1, arr, curr)
            curr.pop()
            subsequence(idx+1,arr,curr)

        subsequence(0,nums,[])
        return result


        