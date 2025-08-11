const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// GPT solution
function yourFunction(s, t) {
    if (t.length > s.length) return "";

    // Frequency map for t
    let need = {};
    for (let c of t) {
        need[c] = (need[c] || 0) + 1;
    }
    let required = Object.keys(need).length;

    let have = {};
    let formed = 0;
    let left = 0;
    let minLen = Infinity;
    let minStart = 0;

    for (let right = 0; right < s.length; right++) {
        let c = s[right];
        have[c] = (have[c] || 0) + 1;

        if (need[c] && have[c] === need[c]) {
            formed++;
        }

        // Shrink window while valid
        while (formed === required) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }

            let leftChar = s[left];
            have[leftChar]--;
            if (need[leftChar] && have[leftChar] < need[leftChar]) {
                formed--;
            }
            left++;
        }
    }

    return minLen === Infinity ? "" : s.slice(minStart, minStart + minLen);
}

function output(data) {
  console.log(data);
}

var inputs = [];
rl.on('line', (input) => {
  inputs.push(input.trim());
    if (inputs.length === 2) {
        const s = inputs[0];
        const t = inputs[1];
        const result = yourFunction(s, t);
        output(result);
        rl.close();
    }
});