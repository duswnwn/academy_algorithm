const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.on("line", (line) => {
    input = line;
    rl.close(); 
});
rl.on('close', () => {
    count = 0 
    for (let i = 1; i <= Math.floor(input.length/2); i++) {
        if (input[i-1] === input[input.length-i]) {
            continue
        }else {
            count += 1
            break
        }
    }
    count == 0 ? console.log("YES") : console.log("NO");
    process.exit();
})