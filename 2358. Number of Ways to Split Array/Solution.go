func waysToSplitArray(nums []int) int {
    n := len(nums)
        ans := 0
        total_sum := 0
        left := 0
        for _, i := range nums{
            total_sum += i
        }

        for j:= 0; j<n-1; j++ {
            fmt.Println(j)
            left += nums[j]
            right := total_sum - left

            if left >= right{
                ans += 1
            }
        }
        return ans
}