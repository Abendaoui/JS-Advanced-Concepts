const counterFunc = () => {
  let counter = 0

  function increament() {
    console.log('Count Increaseing : ' + counter++)
  }

  function decrement() {
    console.log('Count Decreasing : ' + counter--)
  }
  function getCount() {
    console.log('Counter Count : ' + counter)
  }

  return {
    increament,
    decrement,
    getCount,
  }
}

const counter = counterFunc()

// counter.increament()
// counter.decrement()
// counter.increament()
// counter.getCount()
