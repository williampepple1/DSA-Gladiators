/**
 * https://leetcode.com/problems/daily-temperatures
 * Time O(N) | Space O(N)
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures, stack = []) {
    const days = Array(temperatures.length).fill(0);

    for (let day = 0; day < temperatures.length; day++) {/* Time O(N + N) */
        while (canShrink(stack, temperatures, day)) {    /* Time O(N + N) */
            const prevColdDay = stack.pop();
            const daysToWait = (day - prevColdDay);

            days[prevColdDay] = daysToWait;              /* Ignore Space O(N) */
        }

        stack.push(day);                                 /* Space O(N) */
    }

    return days;
};

const canShrink = (stack, temperatures, day) => {
    const previousDay = stack[stack.length - 1];
    const [ prevTemperature, currTemperature ] = [ temperatures[previousDay], temperatures[day] ];
    const isWarmer = prevTemperature < currTemperature;

    return stack.length && isWarmer;
}