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

for(let i = 0; i < 10; i += 1) {
  console.log('for loop i: ' + i)
}

let j = 0
while(j < 10) {
  console.log('while loop j: ' + j)
  j += 1
}

let k = 10

do {
  console.log('do while k: ' + k)
} while(k < 10)

const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.forEach((value => {
  console.log('For each value ' + value)
}))

const doubled = numbers.map(value => value * 2)

console.log('Here are the doubled numbers')

console.log(doubled)
