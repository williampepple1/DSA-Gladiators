/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    const map = new Map();

    for (let i = 0, l = s.length; i < l; i++) {
        const count = map.get(s[i]) || 0;
        map.set(s[i], count + 1);
    }

    for (let i = 0, l = t.length; i < l; i++) {
        const count = map.get(t[i]) || 0;
        map.set(t[i], count - 1);
    }

    for (const [key, value] of map) {
        if (value !== 0) {
            return false;
        }
    }

    return true;
}