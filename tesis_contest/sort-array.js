const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function yourFunction(data) {
  // console.log("ini data: ", data)
    // contoh paramter data [3, 1, 2]
    // contoh data yang perlu di return [1, 2, 3]
    // write your code here
  let arr = []
  for (el in data) {
    // console.log('ini el', el)
    arr.push(data[el].replace(/,|\[|\]/g, ""))
  }
  // console.log(arr)
  return arr.sort()
}

function output(data) {
  var value = data.join(" ");
  console.log(value);
}

rl.on('line', (input) => {
  var data = input.split(" ");
  var dataInput = yourFunction(data);
  output(dataInput);
});