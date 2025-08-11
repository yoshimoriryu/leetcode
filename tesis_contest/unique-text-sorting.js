const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function yourFunction(data, limit) {
  // contoh parameter data =  ["apple", "orange", "apple" "grape"]
  // contoh parameter limit =  4
  // contoh data yang di return = ["apple" ,"grape" ,"orange"]
  let limitedData = data.slice(0,limit)
  let limitedDataSet = new Set(limitedData);
  // console.log(limitedDataSet);

  limitedData = [...limitedDataSet].sort()
  // limitedData.sort()
  return limitedData
}

function output(data) {
  var value = data.join(' ');
  console.log(value);
}

rl.on('line', (input) => {
  var data = input.split(',');
  var data1 = data[0].split(' ');
  var limit = Number(data[1]);
  var dataInput = yourFunction(data1, limit);
  output(dataInput);
});