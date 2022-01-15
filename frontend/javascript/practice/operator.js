// this file was written only from what I didnt know.

// 1. String concatenation
console.log('my' + 'cat');
console.log(`string literals:
''''
1+2 = ${1+2}`);

// 2. Numeric operators
console.log(2**3);

// 3. Increment and decrement operators
let a = 2;
const pre = ++a;
console.log(pre);

// tips
let b = 5;
function check(){
    for( let i =0; i<10; i++){
        console.log('no!');
    }
    return true;
}
// 여러 조건문 작성시 cost가 큰 조건문은 뒤로 빼기
console.log(`${a > b || check()}`);

if(a < b){
    console.log(' is true');
}


//Equality
const c = '5';
const d = 5;

//loose equality
console.log(c == d);
//strict equality !==
console.log(c === d);

//object equality by reference
console.log('object equality')
const k1 = {name:'k'};
const k2 = {name:'k'};
const k3 = k1;
console.log(k1 == k2);
console.log(k1 === k2);
console.log(k1 === k3);

//equlity puzzle
console.log('puzzle')
console.log(0 == false);
console.log(0 === false);
console.log('' == false);
console.log('' === false);
console.log(null == undefined);
console.log(null === undefined);

// conditional operators: if
const name = 'df';
if (name === 'khj'){
    console.log('welcome khj');
}else if ( name === 'coder'){
    console.log('you are amazing coder');
}else {
    console.log('unknown');
}

console.log(name === 'khj'? 'yes' : 'no');

switch(name){
    case 'hjk':
        console.log('yes');
        break;
    default:
        console.log('whatever');
        break;
}