let E = [];
let O = [];

while (true) {
    let input = prompt("Enter a integer (or type '000' to exit)")

    if (input === "000") {
        break
    } 

    let number = Number(input)

    if (isNaN(number)){
        alert("Invalid input")
    } else if (number %2 === 0) {
        E.push(number)
        alert("The number " + number + " id even.")
    } else {
        O.push(number)
        alert("The number " + number + " is odd.")
    }
    
}

alert("Even number list: " + E + " \n Odd numbers list: " + O)
