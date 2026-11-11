// node furst.js
// node JAVASCRIPT_LAB_PRACTICAL_03-11-26.js
console.log("Hello welcome to externnal js file");

a = 10;
var b = 11;

let n = 'najad';
const pi = 3.14


console.log(a + b)
console.log(typeof a)

console.log(n)
console.log(pi)

let c = String(a)
console.log(a)
console.log(typeof c)

// --------------------------------------------

// ====================== DATA TYPES =========================

let age = 25;
console.log(typeof age);

let weight = 35.8;
console.log(typeof weight);

let company = 'quest';
console.log(typeof company);

let stack;
console.log(typeof stack);

let skills = null;
console.log(typeof skills);

let isActive = true;
console.log(typeof isActive);

let stud = ['najad', 25, true, 37.5];
console.log(stud);
console.log(typeof stud);

let stud1 = { name: 'najad', age: 25, skills: ['python', 'JS'], weight: 37.5, Active: true };
console.log(stud1);
console.log(typeof stud1);

// ------------------------------------------------------------------------------------------------
// arithamatics
// ================
num1 = 5
num2 = 6
num3 = '6'
num4 = '5'
num5 = 'najad'

reslt_1 = num1 + num2
reslt_2 = num1 + num3
reslt_3 = num3 + num1
reslt_4 = num3 + num4
reslt_5 = num4 + num3

reslt_6 = num1 - num2
reslt_7 = num1 - num3
reslt_8 = num3 - num1
reslt_9 = num3 - num4
reslt_10 = num4 - num3

reslt_11 = num1 + num5
reslt_12 = num1 - num5

console.log(reslt_1);
console.log(typeof reslt_1);
console.log(reslt_2);
console.log(typeof reslt_2);
console.log(reslt_3);
console.log(typeof reslt_3);
console.log(reslt_4);
console.log(typeof reslt_4);
console.log(reslt_5);
console.log(typeof reslt_5);
console.log(reslt_6);
console.log(typeof reslt_6);
console.log(reslt_7);
console.log(typeof reslt_7);
console.log(reslt_8);
console.log(typeof reslt_8);
console.log(reslt_9);
console.log(typeof reslt_9);
console.log(reslt_10);
console.log(typeof reslt_10);
console.log(reslt_11);
console.log(typeof reslt_11);
console.log(reslt_12);
console.log(typeof reslt_12);

console.log()
console.log(5 == 5)
console.log(5 == 6)
console.log(5 == '5')
console.log(5 === '5')

console.log()
console.log(5 != 5)
console.log(5 != 6)
console.log(5 != '5')
console.log(5 != '6')
console.log(5 !== '5')

console.log()
console.log(5 < 5)
console.log(5 > 6)
console.log(5 <= 5)
console.log(5 >= 6)
console.log(5 <= '5')
console.log(5 >= '6')

num6 = 10
num7 = 10

reslt_13 = num6++
reslt_14 = ++num7

console.log(reslt_13);
console.log(reslt_14);

num6 = 10
num7 = 10
reslt_13 = num6--
reslt_14 = --num7
console.log(reslt_13);
console.log(reslt_14);

// opreters
// ================

console.log()
console.log(5 < 10 && 6 > 4)
console.log(5 < 10 && 6 > 10)

console.log(5 < 10 || 6 > 4)
console.log(5 < 10 || 6 > 10)
console.log(5 < 4 || 6 > 10)

console.log()
console.log(!true)
console.log(!false)
console.log(!5)
console.log(!0)
console.log(!"")
console.log(!" ")
console.log(!null)
console.log(!undefined)
console.log(!NaN)

// ===================== CONTROL STATEMENTS OR CONDITION ==========================

// =====================~=== IF , ELSE IF , ELSE ===================================
age1 = 25

if (age1 > 25) { console.log("age > 25") }
else if (age1 < 25) { console.log("age < 25") }
else { console.log("age = 25") };

// age2 = prompt( 'enter your age :' )

// if (age2 > 25) {console.log(typeof age2) , console.log("age > 25") }
// else if (age2 < 25) { console.log(typeof age2, " age < 25") }
// else { console.log("age = 25") };

// -------------------------------------------------------------------------

// ========================== SWITCH ======================

// day = Number(prompt('Enter a valu b/w 1 - 7 :'))

// switch(day)
// {
//     case 1 : console.log('mon') ; break ;
//     case 2 : console.log('tue') ; break ;
//     case 3 : console.log('wed') ; break ;
//     case 4 : console.log('thu') ; break ;
//     case 5 : console.log('fri') ; break ;
//     case 6 : console.log('sat') ; break ;
//     case 7 : console.log('sun') ; break ;
//     default : console.log('invalid input') ; 

// }

// -----------------------------------------------------------------------------

// =============================== LOOPS ========================================

// --------------- FOR LOOP---------------
for (let i = 1; i <= 10; i++) {
    console.log(i)
}

for (let i = 10; i >= 0; i--) {
    console.log(i)
}

for (let i = 1; i <= 10; i = i + 2) {
    console.log(i)
}

// --------------- WHILE LOOP ---------------
console.log()
i = 0

while (i <= 10) {
    console.log(i)
    i++
}

// --------------- DO WHILE LOOP ---------------

// pin = Number(prompt('Enter a pin :'))

// do{
//     if (pin == 123)
//     {
//         console.log('Login successful')
//         break;
//     }    
//     else
//     {
//         console.log('Incorrect pin')
//     }
//     pin = Number(prompt('Enter a pin :'))

// }while(true);

// -------------------- FOR OF ------------------------------
console.log()

stu = ['najad', 'shahal', 'richu', 'yaseen']

for (s of stu) {
    console.log(s)
}

// -------------------- FOR in ------------------------------
console.log()

let stu_1 = { name: 'najad', age: 25, skills: ['python', 'JS'], weight: 37.5, Active: true };


for (s in stu_1) {
    console.log(s, ' : ', stu_1[s])
}

// =========================================================================================================
// ======================================== function =====================================

console.log()

function greet() {
    console.log('Welcom to js function')
}

function greet_1() {
    return 'Welcom to js quest'
}

greet()
console.log(greet_1())
// ---------------------------------------------------

function add_1(a, b) {
    return a + b
}

console.log(add_1(6, 11))

// ---------------------------------------------------

function name_1(name_2, age) {
    console.log('NAME : ', name_2, '\nAGE : ', age)
}

name_1('najad', 25)
name_1(25, 'najad')
name_1(age = 25, name_2 = 'najad')

// ------------------------------------------------------
console.log()

greet_2 = () => 'Welcome'
greet_3 = () => { 'Welcome_3' }
greet_4 = () => { return 'Welcome_4' }

console.log(greet_2())
console.log(greet_3())
console.log(greet_4())

add_2 = (a, b) => a + b
console.log(add_2(20, 30))

// -----------------------------------------------------

function calc(a, b, fun) {
    return fun(a, b)
}

add = (a, b) => a + b
mul = (a, b) => a * b


console.log(calc(6, 11, add))
console.log(calc(6, 11, mul))
// =======================================================

// a= confirm("do you w")
// console.log(a)

// name_3 = prompt("enter your namae :")
// console.log(name_3)

// function get_value() {
//     is_delete = confirm('Do you wand delete')
//     console.log(is_delete)
// }

// ===========================================================

// ============= String Basics =============


console.log()
console.log('String Basics')
console.log('===============')

var name_4 = 'JavaScript'

console.log(name_4)
console.log(typeof name_4)
console.log(name_4.length)

console.log(name_4[0])
console.log(name_4.language(0))
console.log(name_4[-1])             //not using negateve indaxing
console.log(name_4[20])

console.log(name_4[0, 5])
console.log(name_4.substring(0,5))
console.log(name_4.slice(5, 9))
console.log(name_4.slice(4))

console.log(name_4.slice(0, 3))
console.log(name_4.slice(-6, -1))
console.log(name_4.slice(-6))

console.log('hi', name_4)
console.log('hi' + name_4)
console.log(`hi ${name_4}`)

// -----------------------------------------

for (i = 0; i < name_4.length; i++) {
    console.log(name_4[i])
}

console.log()

for (i of name_4) {
    console.log(i)
}
// -------------------------------------------

console.log()
console.log(name_4.toUpperCase())
console.log(name_4.toLowerCase())

var name_5 ="    najad     "
console.log(name_5.trim())
console.log(name_5.trimStart())
console.log(name_5.trimEnd())

var name_6 ="*******najad vt*********"
console.log(name_6.trim("*"))   // not working




