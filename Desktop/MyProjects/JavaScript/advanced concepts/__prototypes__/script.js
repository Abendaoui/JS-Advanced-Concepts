// Object with Getter and Setter

const car = {
  doors: 4,
  model: 'Car',
  get carModel() {
    return 'The Car Model : ' + this.model
  },
  set carModel(newName) {
    this.model = newName
  },
}

const tesla = {}
Object.setPrototypeOf(tesla, car)
tesla.carModel = 'Tesla'
// tesla.doors = 2

// console.log(tesla);
// console.log("################################");
// console.log(car);

// Object.keys(tesla).forEach((key) => {
//   console.log(key)
// })
// console.log('################################')
// for (key in tesla) {
//   console.log(tesla[key])
// }
