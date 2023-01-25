/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
    let map = new Map();
    for (let char of s) {
      if (map.has(char)) {
        map.set(char, map.get(char) + 1);
      } else {
        map.set(char, 1);
      }
    }
  
    let index = -1;
    for (let [key, value] of map.entries()) {
      if (value === 1) {
        index = s.indexOf(key);
        break;
      }
    }
  
    return index;
  }