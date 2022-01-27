function binary_search(list, target) {
    var first = 0;
    var last = list.length - 1;
    var index = last/2

    while(index > 0) {
        if(list[index] == target) {
            return index
        // if target is in the bottom half
        } else if(target < list[index]) {
            index = index/2
        // if target is in the upper half
        } else if(target > list[index]) {
            index += index/2
        }
    }
}