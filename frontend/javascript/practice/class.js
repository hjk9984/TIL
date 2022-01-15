'use strict';
// object-oriented programming
// class: template
// object: instance of a class
// JS classes
// - introduced in ES6
// - syntactical sugar over prototype-based inferitance

class Person{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }

    speak() {
        console.log(`${this.name}: hello!`);
    }
}

const khj = new Person('khj', 20);
console.log(khj.name);
khj.speak();

class User {
    constructor(first, last, age){
        this.first = first;
        this.last = last;
        this.age = age;     //setter 함수가 실행되는 거임
    }

    get age() {
        return this._age;
    }

    set age(value){
        if(value < 0){
            throw Error('age can not be negative');
        }
        this._age = value;      //this.age로 하면 에러 발생
    }
}

const user1 = new User('steve', 'job', 0);
console.log(user1.age);


// fields public, private
// too soon
class Experiment {
    publicField = 2;
    #privateField = 0;
}
const experiment = new Experiment();
console.log(experiment.publicField);
console.log(experiment.privateField);

//static
// by class
class Article {
    static publisher = 'khj';
    constructor(articleNumber){
        this.articleNumber = articleNumber;
    }

    static printPublisher() {
        console.log(Article.publisher)
    }
    
    print(){
        console.log(this.articleNumber);
    }
}

const article1 = new Article(1);
const article2 = new Article(2);
console.log(Article.publisher);
Article.printPublisher();


class note extends Article {
    //다형성, override
    print(){
        console.log('from note');
        super.print();
    }
}

const note1 = new note(5);
note1.print();

console.log(note1 instanceof Article);
console.log(note1 instanceof Object);
console.log(note1 instanceof note);