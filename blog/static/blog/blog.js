// alert('Hello, world!')
// const theNumber = 1
// //let yourName = 'Thiru'

// if (theNumber === 2) {
//   let yourName = 'valluvan'
//   alert(yourName)
// }

// alert(yourName)

// console.time('myTimer')
// console.count('counter1')
// console.log('A normal log message')
// console.warn('Warning: something bad might happen')
// console.error('Something bad did happen!')
// console.count('counter1')
// console.log('All the things above took this long to happen:')
// console.timeEnd('myTimer')

// function sayHello(yourName) {
//   if (yourName === undefined) {
//       console.log('Hello, no name')
//   } else {
//        console.log('Hello, ' + yourName)
//   }
// }

// const yourName = 'Thiru'  // Put your name here

// console.log('Before setTimeout')

// setTimeout(() => {
//     sayHello(yourName)
//   }, 2000
// )

// console.log('After setTimeout')

// for(let i = 0; i < 10; i += 1) {
// console.log('for loop i: ' + i)
// }

// let j = 0
// while(j < 10) {
// console.log('while loop j: ' + j)
// j += 1
// }

// let k = 10

// do {
// console.log('do while k: ' + k)
// } while(k < 10)

// const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

// numbers.forEach((value => {
// console.log('For each value ' + value)
// }))

// const doubled = numbers.map(value => value * 2)

// console.log('Here are the doubled numbers')

// console.log(doubled)

////class related

// class Greeter {
//   constructor (name) {
//     this.name = name
//   }

//   getGreeting () {
//     if (this.name === undefined) {
//       return 'Hello, no name'
//     }

//     return 'Hello, ' + this.name
//   }

//   showGreeting (greetingMessage) {
//     console.log(greetingMessage)
//   }

//   greet () {
//     this.showGreeting(this.getGreeting())
//   }
// }

// const g = new Greeter('Thiru')  // Put your name here if you like
// g.greet()


// class DelayedGreeter extends Greeter {
//   delay = 2000

//   constructor (name, delay) {
//     super(name)
//     if (delay !== undefined) {
//       this.delay = delay
//     }
//   }

//   greet () {
//     setTimeout(
//       () => {
//         this.showGreeting(this.getGreeting())
//       }, this.delay
//     )
//   }
// }

// const dg2 = new DelayedGreeter('Thiru 2 Seconds')
// dg2.greet()

// const dg1 = new DelayedGreeter('Thiru 1 Second', 1000)
// dg1.greet()


function resolvedCallback(data) {
  console.log('Resolved with data ' +  data)
}

function rejectedCallback(message) {
  console.log('Rejected with message ' + message)
}

const lazyAdd = function (a, b) {
  const doAdd = (resolve, reject) => {
    if (typeof a !== "number" || typeof b !== "number") {
      reject("a and b must both be numbers")
    } else {
      const sum = a + b
      resolve(sum)
    }
  }

  return new Promise(doAdd)
}

const p = lazyAdd(3, 4)
p.then(resolvedCallback, rejectedCallback)

lazyAdd("nan", "alsonan").then(resolvedCallback, rejectedCallback)
