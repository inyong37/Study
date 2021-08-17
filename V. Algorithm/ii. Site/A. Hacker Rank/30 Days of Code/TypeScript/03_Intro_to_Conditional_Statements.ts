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
    const N: number = parseInt(readLine().trim(), 10);
    if ((N % 2 !== 0) || (N >= 6 && N <= 20)) {
        console.log('Weird');
    }
    else {
        console.log('Not Weird');
    }
}
