// # Given an integer array nums, return true if any value appears at least twice in the array,
// #  and return false if every element is distinct.

// #  Javascript

var containsDuplicate = (nums, numsSet = new Set()) => {
    for (const num of nums) {/* Time O(N) */
        if (numsSet.has(num)) return true;

        numsSet.add(num);       /* Space O(N) */
    }

    return false;
};