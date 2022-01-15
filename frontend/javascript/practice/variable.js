// Javascript is very flexible
// flexible == dangerous
// added ECMAScipt 5
// use strict make script be strict to declartion role
'use strict';

console.log("hello world");


// 2. Variable, read write
// let (added in ES6) (mutable)

// block scope
let globalName = 'global name';
{
    let name = 'khj'
    console.log(name);
    name = 'hi';
    console.log(name);
}
console.log(name);  // it doesn't work
console.log(globalName);

// var is old fashioned so that is not recommended to use it
// var can use variable not previously declared.
// this issue is called "var hoisting"
// var hoisting move declaration from bottom to top.

// and var has no block scope 
console.log(age);
{
    age = 4;
    var age;
}
console.log(age);


// 3. contant, read only
// favor immutable data type always for a few reasons:
// - security
// - thread safety
// - reduce human mistakes
// so we can classify variable to mutable let and immutable const.
const pi = 3.14;

// Note!
// Immutable data types: premitive types, frozen objects (i.e. object.freeez())
// Mutable data types: all objects by defaut are mutalbe in JS.


// 4. Variable types
// primitive, single item: number, string, boolean, null, undefined, symbol
// object, box-container
// function, first-class function

const count = 17;   //integer
const size = 17.1;  //decimal number
console.log(`value: ${count}, type: ${typeof count}`);
console.log(`value: ${size}, type: ${typeof size}`);

// number - special numeric values: infinity, -infinity, NaN
const infinity = 1/0;
const negativeInfinity = -1/0;
const nan = 'not a number' / 2;
console.log(infinity);
console.log(negativeInfinity);
console.log(nan);

//bigInt (fairly new, dont use it yet)
const bigInt = 1234567891234567891234567891234567891111111111111n;
console.log(`value: ${bigInt}, type: ${typeof bigInt}`);

//string
const char = 'c';

const brendan = 'brendan';
const greeting = 'hello ' + brendan;
console.log(`value: ${greeting}, type: ${typeof greeting}`);
const hellobob = `hi ${brendan}!`;                              //template literals
console.log(`value: ${hellobob}, type: ${typeof hellobob}`);
console.log(`value: `+hellobob+`, type: `+ typeof hellobob);

// boolean
// false: 0, null, undefined, NaN, ''
// true: any other type
const can = true;
const test = 3 < 1;
console.log(`value: ${can}, type: ${typeof can}`);

// null
let nothing = null;
console.log(`value: ${nothing}, type: ${typeof nothing}`);

// undefined
let x;
let y = undefined;
console.log(`value: ${x}, type: ${typeof x}`);

// symbol, create unique identifiers for objects
const sym1 = Symbol('id');
const sym2 = Symbol('id');
console.log(sym1 === sym2);

const gsym1 = Symbol.for('id');
const gsym2 = Symbol.for('id');
console.log(gsym1 === gsym2);
console.log(`value: ${sym1.description}, type: ${typeof sym1}`);

// object, real-life object, data structure
// a pointer of object is immutable but attributes of object is mutable. 
const khj = {name: 'khj', age: 29};

// 5. Dynamic typing: dynamically typed language
let text = 'hello';
console.log(text.charAt(0));        //h
console.log(`value: ${text}, type: ${typeof text}`);
text = 5;
console.log(`value: ${text}, type: ${typeof text}`);
text = '7' + 5;
console.log(`value: ${text}, type: ${typeof text}`);
text = '8' / '2';
console.log(`value: ${text}, type: ${typeof text}`);
// console.log(text.charAt(0));     >> dynamic typing 때문에 안됨
// to solve this issue, type script cane out.