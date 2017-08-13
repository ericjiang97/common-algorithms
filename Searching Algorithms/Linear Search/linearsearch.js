/**
 * Linear search function
 * @param {*} array the array to look through
 * @param {*} key the key of an item
 * @param {*} target the target to look for.
 */
function linearSearch (array, key, target) {
    for (var i = 0; i < array.length; i++) {
        if (array[i][key] === target) {
            return array[i]
        }
    }
    return false
}