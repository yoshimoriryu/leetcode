const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function yourFunction(data) {
    // contoh parameter data = "abcdefgh"
    // contoh yang perlu di return "abcfgh"
    // write your code here
    N = data.length
    // console.log(N)
    if (N < 6) {
      return data
    } else {
      return data.slice(0,3) + data.slice(N-3,N)
    }
    return 0;
}

function output(data) {
  console.log(data);
}

rl.on('line', (input) => {
  var data = input;
  var result = yourFunction(data);
  output(result);
});