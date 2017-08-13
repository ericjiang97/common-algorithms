/**
 * Binary search function for JSON files
 * @param {*} array the SORTED array to look through
 * @param {*} key the key of an item
 * @param {*} target the target to look for.
 * @return the element
 */
function binarySearch(array, key, target) {
    var min = 0
    var max = array.length
    while (min <= max) {
        var middle = Math.round((min + max) / 2)
        var currentEle = array[middle][key]
        if (currentEle === target) {
        return array[middle]
        } else if (target < currentEle) {
        max = middle - 1
        } else {
        min = middle + 1
        }
    }
    return false
}