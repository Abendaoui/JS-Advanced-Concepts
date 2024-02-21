// ECMAScript6 class Example

class Animal {
  constructor(name) {
    this.name = name
    this.eats = true
  }

  slepping() {
    return `${this.name} Is Sleeping Now.`
  }

  eating() {
    return this.eats ? `${this.name} Is Eating Now.` : this.slepping()
  }
}

class Dog extends Animal {
  constructor(name,age) {
    super(name)
    this.age = age
  }

  getInfo(){
   return `${this.name} Is ${this.age} Years Old Now.`
  }

}

const dog = new Dog('Loki',22)

console.log(dog.getInfo())
