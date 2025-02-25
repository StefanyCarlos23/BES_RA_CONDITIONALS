let a = Number(prompt("Enter a number for A"))
let b = Number(prompt("Enter a number for B"))
let c = Number(prompt("Enter a number for C"))

const quadraticEquation = b**2 -4*a*c

if (quadraticEquation > 0) {
    console.log("There are two distinct roots.")
} else if (quadraticEquation === 0) {
    console.log("There are two equal roots.")
} else {
    console.log("There are two imaginary roots")
}