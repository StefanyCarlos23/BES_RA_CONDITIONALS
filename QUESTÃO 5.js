let userName = prompt("Hello! In this program you will discover what is your ideal weight.\n To start, please enter your name:")
let userHeight = Number(prompt("Now, enter your height in meter: "))
let userGender = prompt("Finally, enter your biological sex (Male or Female): ")


if (userGender === "Male") {
    let idealWeight = 72.7*userHeight-58
    alert(userName + ", your ideal weight is " + idealWeight.toFixed(2) + " kilograms.") // .toFixed(2) - is used to display only two decimal places.
} else if (userGender === "Female") {
    // I need to declare the variable idealWeight again because it was declared within the if scope.
    let idealWeight = 62.1*userHeight-44.7
    alert(userName + ", your ideal weight is " + idealWeight.toFixed(2) + " kilograms.")
} else {
    alert("Invalid input for biological sex.") 
}