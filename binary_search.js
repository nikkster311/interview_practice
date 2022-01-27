function binary_search(list, target) {
    var first = 0;
    var last = list.length - 1;

    while(first <= 0) {
        midpoint = (first + last)/2
        if(list[midpoint] == target) {
            console.log(list[midpoint]);
            return midpoint
        // if target is in the bottom half
        } else if(target < list[midpoint]) {
            last = midpoint - 1
        // if target is in the upper half
        } else if(target > list[midpoint]) {
            first = midpoint + 1
        }
    }
    return none;
}


list = [...Array(30).keys()];
console.log(list);
binary_search(list, 23);