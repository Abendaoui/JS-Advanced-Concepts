Prototypal Inheritance && The Prototypal Chain

ES6 Introduced Classes Which is the Modern Way To Construct Obects

Prototypal Inheritance && Chain Are:

1. => ES6 Classes are considered "syntactic sugar".
2. => Often In Interview Questions.

Rules:

1. => The __proto__ Must Be an Object Or null
2. => An object can only directly inherit from one object


Code Excution :
console.log('Player Plays : ' + player.plays)
console.log('Player Alive : ' + player.alive)

console.log(player)
console.log('Player Alive : ' + player.alive)

console.log(Object.getPrototypeOf(player))
console.log(player.__proto__);

console.log(Object.getPrototypeOf(player) === player.__proto__)
