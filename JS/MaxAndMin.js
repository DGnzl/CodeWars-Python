function highAndLow(numbers) {
    var nums = numbers.split(" ")
    var max = parseInt(nums[0]);
    var min = parseInt(nums[0]);
    for (var i = 1; i < nums.length; i++) {
        max = Math.max(max, parseInt(nums[i]))
        min = Math.min(min, parseInt(nums[i]))
    }
    return max + " " + min
}

highAndLow("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")