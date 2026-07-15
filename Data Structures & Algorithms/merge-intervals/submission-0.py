
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_array = [intervals[0]]
        for B in intervals[1:]:
            A=merged_array[-1]
            if A[1] < B[0]:
                merged_array.append(B)
            else:
                merged_array[-1]=[A[0], max(A[1], B[1])]
        return merged_array