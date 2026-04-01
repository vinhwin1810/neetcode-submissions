class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashMap = new Map();
        let res = [];
        nums.forEach((num, i) => {
            if (hashMap.has(target - num)){
                res = [i, hashMap.get(target - num)]
            }
            hashMap.set(num, i)
        })
        return res
    }
}
