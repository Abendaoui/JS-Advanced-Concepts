// IIFE (Immediately Invoked Function Expression)

// const privateCounter = (() => {
//   let count = 0
//   console.log('Initiale Value  : ' + count)
//   return () => {
//     count += 1
//     console.log(count)
//   }
// })()

// privateCounter() // 1
// privateCounter() // 2

const credits = ((num) => {
  let credits = num
  console.log('Initiale Credits Value  : ' + credits)
  return () => {
    credits--
    if (credits > 0) {
      console.log('Playing Game : ' + credits + ' credit(s) remaining')
    }
    if (credits <= 0) {
      console.log('Not Enough Credits : ' + credits)
    }
  }
})(3)
credits()
credits()
credits()


