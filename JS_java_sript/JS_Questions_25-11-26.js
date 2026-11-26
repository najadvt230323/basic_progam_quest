// QIS Academy | JavaScript Lab Practical
// ==========================================

// Instructions
// • Write a separate JavaScript program for each question.
// • Use the specified array or object methods wherever applicable.
// • Display the results in the browser console using console.log().
// • Do not hard-code the expected output when the task requires processing the given data.
// • Use meaningful variable names and format your code neatly.
// • For questions involving objects, access properties using dot notation or bracket notation as appropriate.
// Sample Data
// Use the following data for the relevant exercises. You may add more records when required.

// =======================================================================================================

const numbers = [12, 5, 28, 17, 40, 9, 28, 33, 5];
const fruits = ["Apple", "Orange", "Mango", "Banana", "Grapes"];
const students = [
{ id: 1, name: "Arun", age: 21, course: "JavaScript", mark: 78 },
{ id: 2, name: "Meera", age: 22, course: "Python", mark: 92 },
{ id: 3, name: "Rahul", age: 20, course: "JavaScript", mark: 45 },
{ id: 4, name: "Anu", age: 21, course: "Python", mark: 86 },
{ id: 5, name: "Nikhil", age: 23, course: "JavaScript", mark: 67 }
];
const products = [
{ id: 101, name: "Laptop", category: "Electronics", price: 55000, stock: 8 },
{ id: 102, name: "Mouse", category: "Accessories", price: 700, stock: 25 },
{ id: 103, name: "Keyboard", category: "Accessories", price: 1500, stock: 12 },
{ id: 104, name: "Monitor", category: "Electronics", price: 12000, stock: 5 },
{ id: 105, name: "Webcam", category: "Electronics", price: 2500, stock: 15 }
];
// ----------------------------------------------------------------------------------------------------------------------

// Part A – Basic Array Operations
// =====================================

// 1. Create an array containing five of your favourite programming languages. Display the total number of elements
// using length and display the first and last elements.

console.log()
console.log(numbers.length)             //output : 9
console.log(numbers[0])                 //output : 12
console.log(numbers[numbers.length-1])  //output : 5

// 2. Add two new fruits to the end of the fruits array using push(). Display the updated array.

console.log()
console.log(fruits)            //output : [ 'Apple', 'Orange', 'Mango', 'Banana', 'Grapes' ]
fruits.push("bannana",'kivi')
console.log(fruits)            //output : [ 'Apple',  'Orange', 'Mango',  'Banana', 'Grapes', 'bannana', 'kivi' ]

// 3. Remove the last element from the fruits array using pop(). Display both the removed element and the updated array.

console.log()
console.log(fruits)    //output : [ 'Apple', 'Orange', 'Mango', 'Banana', 'Grapes', 'bannana', 'kivi'  ]
fruits.pop()
console.log(fruits)   //output : [ 'Apple',  'Orange', 'Mango',  'Banana', 'Grapes', 'bannana' ]

// 4. Add a new fruit at the beginning using unshift(), then remove the first element using shift(). Display the array
// after each operation.

console.log()
console.log(fruits)    //output : [ 'Apple',  'Orange', 'Mango',  'Banana', 'Grapes', 'bannana' ]
fruits.unshift('kivi')
console.log(fruits)    //output : [ 'kivi', 'Apple',  'Orange', 'Mango',  'Banana', 'Grapes', 'bannana' ]
fruits.shift()
console.log(fruits)    //output : [ 'Apple',  'Orange', 'Mango',  'Banana', 'Grapes', 'bannana' ]

// 5. Check whether "Mango" and "Pineapple" are present in the fruits array using includes().

console.log(fruits.includes("Mango"))          // output : true
console.log(fruits.includes("Pineapple"))      // output : false
console.log(fruits.indexOf("Mango"))           // output : 2
console.log(fruits.indexOf("Pineapple"))       // output : -1


// 6. Find the index of 28 in the numbers array using indexOf(). Also find the last occurrence of 28 using
// lastIndexOf().

console.log(numbers.indexOf(28))         // output : 2
console.log(numbers.lastIndexOf(28))     // output : 6

// 7. Extract the second, third and fourth elements from the numbers array using slice(). Verify whether the original
// array has changed.



// 8. Remove two elements starting from index 2 in a copy of the numbers array using splice(). Display the removed
// elements and the remaining array.

// Part B – Array Iteration and Transformation
// ==================================================

// 1. Use forEach() to display each fruit along with its index in the fruits array.
// 2. Use map() to create a new array containing the square of every number in the numbers array.
// 3. Use filter() to create a new array containing only the even numbers from the numbers array.
// 4. Use find() to find the first student who scored more than 80. Display the complete student object.
// 5. Use findIndex() to find the index of the student named "Rahul".
// 6. Use reduce() to calculate the sum and average of all numbers in the numbers array.
// 7. Use some() to check whether at least one student scored below 50. Use every() to check whether all students
// are aged 18 or above.
// 8. Sort the numbers array in ascending order and then descending order. Use a numeric comparison callback.
// Display the original array as well.

// Part C – Object Methods
// ============================

// 1. Create an object named course with the properties courseName, duration, fee and mode. Display all its
// property names using Object.keys().
// 2. Use Object.values() to display all values of the course object. Use Object.entries() to display its key-value pairs.
// 3. Create an array of key-value pairs for a book (title, author, price and pages). Convert it into an object using
// Object.fromEntries().
// 4. Create two objects containing personal details and contact details. Merge them into a new object using
// Object.assign() or the spread operator. Do not modify the original objects.
// 5. Create a user object with name, email and role. Check whether the email property exists using Object.hasOwn().
// Also check for a phone property that does not exist.
// 6. Create a configuration object and apply Object.freeze(). Try to update an existing property and add a new
// property. Display the object and check it using Object.isFrozen().
// 7. Create an employee object and apply Object.seal(). Try to update an existing property, add a new property and
// delete an existing property. Display the result and check it using Object.isSealed().
// Part D – Real-World Array and Object Challenges
// 1. From the students array, use filter() to display students who scored 70 or above. Display only their names and
// marks in a new array using map().
// 2. From the products array, filter products whose stock is less than 10. Display their names and stock quantities.
// 3. Calculate the total value of the available inventory. For each product, multiply price × stock and use reduce() to
// calculate the grand total.
// 4. Group the students by their course using Object.groupBy(). Display the resulting groups. If your JavaScript
// environment does not support this method, group them manually using a loop.
// 5. Find the student with the highest mark and the student with the lowest mark. Display their names and marks.
// 6. Remove duplicate values from the numbers array and display a new array containing only unique numbers. Use
// Set and the spread operator.
// QIS Academy | JavaScript Lab Practical Page 3
// Submission Checklist
// Task
// Complete
// d
// All programs are written and executed n
// Console outputs are checked n
// Code is properly formatted and commented n
// Screenshots or output evidence are prepared n
// Submission: Save each solution in a clearly named JavaScript file. Submit the source code and output evidence according
// to your trainer's instructions.