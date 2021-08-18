'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;
process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

function main() {
    // Enter your code here
    let t: number = parseInt(readLine().trim());
    for (let i: number = 0; i < t; i++) {
        let s: string = readLine().trim();
        for (let j: number = 0; j < s.length; j = j + 2) {
            process.stdout.write(s[j]);
        }
        process.stdout.write(' ');
        for (let j: number = 1; j < s.length; j = j + 2) {
            process.stdout.write(s[j]);
        }
        console.log('');
    }
}
