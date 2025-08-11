const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function yourFunction(data) {
    // contoh parameter data = "hello world"
    // contoh yang perlu di return ['hello', 'world']
    // write your code here
    return data.split(" ")
}

function output(data) {
  console.log(data);
}

rl.on('line', (input) => {
  var data = input;
  var result = yourFunction(data);
  output(result);
});