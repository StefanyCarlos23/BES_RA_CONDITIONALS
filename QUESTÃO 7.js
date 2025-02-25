let userAge = Number(prompt('Enter your age to find out if you can ride a Hopi Hari roller coaster: '))
let userWeight = Number(prompt('Now enter your weight: '))

// I added the check to ensure that the user enters a number.
if (isNaN(userAge) || isNaN(userWeight)) {
    alert("Please enter valid numbers for age and weight.")
} else if (userAge >= 15 && userWeight < 120) {
    alert("Allowed!")
} else {
    alert("Prohibited!")
}
