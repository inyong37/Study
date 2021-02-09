// Author      : inyong1020@gmail.com
// Date        : 2020-06-30-Tue.
// Description : Hacker Rank; 30 Days of code; Day 21: Generics.
// State       : Passed.
// Environment : -
// Input       : -
// Output      : -
// Reference   : https://www.hackerrank.com/challenges/30-generics/tutorial
// Reference   : https://opentutorials.org/course/2517/14153
// Reference   : https://www.hackerrank.com/challenges/30-generics/forum
// Reference   : https://www.programmingoneonone.com/2020/05/generics-problem-solution-hackerRank.html
/*
Objective
Today we're discussing Generics; be aware that not all languages support this construct, so fewer languages are enabled for this challenge. Check out the Tutorial tab for learning materials and an instructional video!

Task
Write a single generic function named printArray; this function must take an array of generic elements as a parameter (the exception to this is C++, which takes a vector). The locked Solution class in your editor tests your function.

Note: You must use generics to solve this challenge. Do not write overloaded functions.

Input Format

The locked Solution class in your editor will pass different types of arrays to your printArray function.

Constraints

You must have exactly  function named printArray.
Output Format

Your printArray function should print each element of its generic array parameter on a new line.
*/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <class T>
void printArray(vector<T> vec)
{
    for(int i = 0; i<vec.size(); i++)
        cout << vec[i] << endl;
}


int main() {
	int n;

	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}

	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}
