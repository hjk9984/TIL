// object = {key : value};
// 키와 값의 집합체

const name = 'kim';
const age = 20;
print(name, age);

const obj1 = {};            // object literal syntax
const obj2 = new Object();  // object constructor syntax

function print(person){
    console.log(person.name);
    console.log(person.age);
}

const kim = {name: 'kim', age: 29};
print(kim);

// 런타임에 프로퍼티를 추가할 수 있다.
// 하지만 이런거는 좋지 않음
kim.hasjob = true;
console.log(kim.hasjob);
delete kim.hasjob;

console.log(kim['name']);
console.log(kim.hasjob);

function printValue(obj, key){
    console.log(obj[key]);
}
printValue(kim, 'name');

// Property value shorthand
const person = new Person('hj', 29);
console.log(person.name)
function makePerson(name, age){
    return {name, age};
    // 키값이 변수명과 같다면 이런식으로 저장 가능
}

//constructor function
function Person(name, age) {
    this.name = name;
    this.age = age;
}


console.log('name' in person);
console.log(person.phone);

for (key in person){
    console.log(key);
}

const array = [1, 2, 3, 4, 5];
for(v of array){
    console.log(v);
}


//cloning
const user = {name: 'kim', age: '29'};
const user2 = user;     //shallow copy
user2.name = 'coder';
console.log(user);

// deep clone
const user4 = {};
Object.assign(user4, user);
console.log(user4);

const f1 = {color:'red'};
const f2 = {color: 'blue', size: 'big'};
const mixed = Object.assign({}, f1, f2);
// 뒤에 있는 인자가 앞의 인자를 덮음
console.log(mixed.color);
console.log(mixed.size);