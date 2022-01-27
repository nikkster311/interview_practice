function linear_search(list, target) {
    // return index of target, if not found return none
    for(item in list) {
        if(item == target) {
            console.log("found! " + target)
            return target
        }
        else if(item < target) {
            console.log("the target is higher");
        }
        else if(item > target) {
            console.log("the target is lower");
        }
        else {
            console.log("Item not in list");
        }
    };
};

list = [...Array(30).keys()];
console.log(list);
linear_search(list, 23);