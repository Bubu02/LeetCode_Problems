class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Case 1: Land ride first, then Water ride
        # Find the earliest possible finish time for any land ride
        min_land_finish = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            min_land_finish = min(min_land_finish, start + duration)
        
        # Pair this earliest land finish with the best matching water ride
        ans1 = float('inf')
        for start, duration in zip(waterStartTime, waterDuration):
            ans1 = min(ans1, max(min_land_finish, start) + duration)
            
        # Case 2: Water ride first, then Land ride
        # Find the earliest possible finish time for any water ride
        min_water_finish = float('inf')
        for start, duration in zip(waterStartTime, waterDuration):
            min_water_finish = min(min_water_finish, start + duration)
            
        # Pair this earliest water finish with the best matching land ride
        ans2 = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            ans2 = min(ans2, max(min_water_finish, start) + duration)
            
        # Return the minimum finish time between both sequence plans
        return min(ans1, ans2)