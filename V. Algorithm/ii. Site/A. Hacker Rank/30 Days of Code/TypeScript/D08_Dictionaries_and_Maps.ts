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
    let phoneBook: {[name: string]: any} = {};
    let n: number = parseInt(readLine());
    for (let i: number = 0; i < n; i++) {
        let s: string = readLine();
        let splitted = s.split(' ');
        phoneBook[splitted[0]] = splitted[1];
    }
    for (let i: number = 0; i < n; i++) {
        let s: string = readLine();
        if (s in phoneBook) {
            process.stdout.write(s + '=' + phoneBook[s]);
        } else {
            process.stdout.write('Not found');
        }
        console.log();
    }
    
}
