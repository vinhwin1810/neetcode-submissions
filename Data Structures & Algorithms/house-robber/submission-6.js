class Solution {
    rob(nums) {
        this.nums = nums
        this.memo = {}
        return this.superRob(0)
    }

    superRob(i) {
        if (i >= this.nums.length) {
            return 0
        }

        if (this.memo[i] !== undefined) {
            return this.memo[i]
        }

        let skip = this.superRob(i + 1)
        let take = this.nums[i] + this.superRob(i + 2)

        this.memo[i] = Math.max(skip, take)

        return this.memo[i]
    }
}