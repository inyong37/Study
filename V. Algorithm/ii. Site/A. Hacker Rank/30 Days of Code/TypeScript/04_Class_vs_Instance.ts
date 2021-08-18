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

class Person {
    age: number;
    constructor(initAge: number) {
        if (initAge >= 0) {
            this.age = initAge;
        } else {
            this.age = 0;
            console.log('Age is not valid, setting age to 0.');
        }
    }
    
    amIOld(): void {
        if (this.age < 13) {
            console.log('You are young.');
        } else if (this.age >= 13 && this.age < 18) {
            console.log('You are a teenager.');
        } else {
            console.log('You are old.')
        }
    }
    yearPasses(): void {
        this.age += 1;
    }
}

function main() {
    // Enter your code here
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        let age: number = parseInt(readLine());
        let person = new Person(age);
        person.amIOld();
        for (let j = 0; j < 3; j ++) {
            person.yearPasses();    
        }
        person.amIOld();
        console.log('');
    }
}

/*
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

function Person(initAge: number){
    let age: number;
    if (initAge >= 0) {
        age = initAge;
    }
    else {
        age = 0;
        console.log('Age is not valid, setting age to 0.');
    }
    
    let amIOld = function(): void {
        if (age < 13) {
            console.log('You are young.');
        }
        else if (age >= 13 && age < 18) {
            console.log('You are a teenager.');
        }
        else {
            console.log('You are old.')
        }
    };
    
    let yearPasses = function(): void {
        age += 1;
    };
    amIOld();
    for (let i = 0; i < 3; i++) {
        yearPasses();
    }
    amIOld();
    console.log('');
}

function main() {
    // Enter your code here
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        let person = Person(parseInt(readLine()));
    }
}
*/
