class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) {
            return false
        }
        const countS = s.split('').reduce((acc, num) => {
            acc[num] = (acc[num] || 0) + 1
            return acc
        }, {})
        const countT = t.split('').reduce((acc, num) => {
            acc[num] = (acc[num] || 0) + 1
            return acc
        }, {})
                for (const key in countS) {
            if (countS[key] !== countT[key]) {
                return false;
            }
        }
        return true;
    }
}
