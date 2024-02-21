// Object Literals
const person = {
  name: 'adil bendaoui',
}

const player = {
  plays: true,
}

// JS now has getPrototypeOf and setPrototypeOf methods of using __proto__

Object.setPrototypeOf(player, person)

// console.log(player.plays)
// console.log(player.alive)

// Extending the prototype chain => general to specific to more specific

const guitarist = {
  strings: 6,
  __proto__: player,
}

// console.log(guitarist.strings);
// console.log(guitarist.plays)
// console.log(guitarist.name)

