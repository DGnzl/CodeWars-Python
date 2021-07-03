function calculate(str) {
    //return eval(str.replace(/plus/g, '+').replace(/minus/g, '-')).toString()
    let ans = 0
    str = str.replace(/plus/g, ' ')
    str = str.replace(/minus/g, ' -')
    let numbers = str.split(' ')
    
    for (let i = 0; i < numbers.length; i++) {
      ans += parseInt(numbers[i])
    }
    return ans.toString()
  }