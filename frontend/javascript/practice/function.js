// function is object in JS (first-class function)

function log(msg){
    console.log(msg);
}
log("hello");

// parameters
// premitive parameters: passed by value
// object parameters: passed by reference
function changeName(obj){
    obj.name = 'k';
}
const khj = {name:'khj'};
changeName(khj);
console.log(khj);

// default parameters
// empty parameter is replaced undifined
function showMsg(msg, from){            //from ="unknown"처럼 기본값 저장 가능
    console.log(`${msg} by ${from}`);
}
showMsg('HI');

function printAll(...args){
    for(const arg of args){
        console.log(arg);
    }

    //리턴이 없을 경우 아래와 같다
    //return undefined;
}


// function은 hoisting이 되기 때문에
// 뒤에서 선언해도 앞에서 사용가능 
const print = function () { //anonymous function
    console.log('print');
};
print();


// Callback function using function expression
const printYes = function () {
    console.log('yes');
};
const printNo = function () {
    console.log('no');  
};
function randomQuiz(answer, printYes, printNo){
    if(answer === 'love you'){
        printYes();
    } else {
        printNo();
    }
}
randomQuiz('wrong', printYes, printNo);
randomQuiz('love you', printYes, printNo);


// Arrow function
// always anonymous
const add = (a, b) => a+b;
const simplePrint = () => console.log("simplePrint");
