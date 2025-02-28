let userName = prompt("Hello! In this program you will discover what is your ideal weight.\n To start, please enter your name:")
let userHeight = Number(prompt("Now, enter your height in meter: "))
let userGender = prompt("Finally, enter your biological sex (Male or Female): ").trim().toLowerCase(); //accept lower case
let idealWeight;

if (isNaN(userHeight) || userHeight <= 0) {
    alert("Invalid height input. Please enter a valid number.");
} else {
    if (userGender === "male") {
        idealWeight = 72.7*userHeight-58
        alert(userName + ", your ideal weight is " + idealWeight.toFixed(2) + " kilograms.") // .toFixed(2) - is used to display only two decimal places.
    } else if (userGender === "female") {
        idealWeight = 62.1*userHeight-44.7
        alert(userName + ", your ideal weight is " + idealWeight.toFixed(2) + " kilograms.")
    } else {
        alert("Invalid input for biological sex. Please enter 'Male' or 'Female'.") 
    }
}