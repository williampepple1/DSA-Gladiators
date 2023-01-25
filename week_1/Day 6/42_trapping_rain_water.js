/**
 * Linear
 * Time O(n) | Space O(n) 
 * https://leetcode.com/problems/trapping-rain-water
 * @param {number[]} height
 * @return {number}
 * 
 */
var trap = function(height) {
    
    const maxLeft = [];
    const maxRight = [];
    const minLeftRight = [];

    let current = 0;
    for(let i = 0; i < height.length; i++) {
     maxLeft.push(current);
     current  = Math.max(current, height[i]);
    }
    current = 0;
    for(let i = height.length - 1; i > -1; i--) {
        maxRight.push(current);
        current = Math.max(current, height[i]);
    }
    // because the elements were added reverse. 
    maxRight.reverse();

    for(let i = 0; i < height.length; i++) {
        const minofLeftRight = Math.min(maxLeft[i],maxRight[i]);
        minLeftRight.push(minofLeftRight);
    }

    let water = 0;
    for(let i = 0; i < height.length; i++) {
        if(minLeftRight[i] - height[i] > 0) {
            water += minLeftRight[i] - height[i];
        }
    }

    return water;
};
