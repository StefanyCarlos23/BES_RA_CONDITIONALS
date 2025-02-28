let userAge = Number(prompt("To find out if you can retire, enter your age: "))
let jobTime = Number(prompt("Now, enter how many years of service you have:"))

if (isNaN(userAge) || userAge <0 || isNaN(jobTime) || jobTime <0) {
    console.log("Invalid Input!!. Please enter you age and you work time.")
} else if (userAge >= 65 || jobTime >= 30 || (userAge === 60 && jobTime === 25)) {
    console.log("Congratulations, you can retire!!")
} else {
    console.log("You cannot retire yet.")
}