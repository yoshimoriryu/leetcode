const { count } = require('console');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function isPrime(n) {
  if (n <= 1) return false
  if (n <= 3) return true
  if (n % 2 == 0 || n % 3 == 0) return false

  for (let i = 5; i*i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) return false
  }
  return true
}

function yourFunction(data, limit) {
  let count = 0
  let primes = []
  for (let i=0; i < Math.min(limit, data.length); i++) {
    // console.log(data[i], isPrime(data[i]))
    if (isPrime(data[i])) {
      count += 1
      primes.push(data[i])
    }
  }
  // console.log(data, count, prime)
  return { primeArr: primes, totalPrimeArr: count };
}

function output(data) {
  var value1 = data.primeArr.join(' ');
  var value = value1 + ',' + data.totalPrimeArr;
  console.log(value);
}

rl.on('line', (input) => {
  var data = input.split(',');
  var data1 = data[0].split(' ');
  var parameter = data1.map(Number);
  var limit = Number(data[1]);
  var dataInput = yourFunction(data1, limit);
  output(dataInput);
});
