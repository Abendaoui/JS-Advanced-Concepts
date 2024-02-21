

// Global Scope
let x = 1

function parentFun() {
  // Local Scope
  let myValue = 2
  console.log(x) // 1
  console.log(myValue) // 2
  console.log("Child Execution");
  console.log("###############################");
  function childFunc() {
    console.log((x += 5)) // 6
    console.log((myValue += 1)) // 3
    console.log("Ending Execution");
  }

  return childFunc
}

// const res = parentFun()
// res()
// res()
// console.log(x);

// console.log(myValue); // Error : myValue is not defined
