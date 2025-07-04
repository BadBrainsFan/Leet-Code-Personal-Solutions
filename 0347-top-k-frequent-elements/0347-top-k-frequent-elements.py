class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        else:
            count = {}
            for number in nums:
                if number not in count:
                    count[number] = 1
                else:
                    count[number] += 1
            
            middle_list = []

            for key, value in count.items():
                if value >= k:
                    middle_list.append(key)

            middle_list.sort()
            answer = []

            while len(answer) < k:
                answer.append(middle_list.pop())
            
            return answer