class Solution:
    def trap(self, height: List[int]) -> int:
 
        n = len(height)
        if n == 0:
            return 0
        water = 0

        # start from front of the array
        # and look for the max wall
        max_idx = 0
        max_height = height[0]

        for i in range(1, n):
            if height[i] >= max_height:
                max_idx = i # save the highest wall index for later
                max_height = height[i]

            water += max_height - height[i]

    # after that start from back and go reverse to the max wall idx
    # and correct the result (pour the extra water if there is smaller wall on the right side)
        back_max_height = height[-1]

        for i in range(n - 1, max_idx, -1):
            if height[i] > back_max_height:
                back_max_height = height[i]

            water -= max_height - back_max_height

        return water


