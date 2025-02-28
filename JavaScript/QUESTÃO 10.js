while (true) {
    let firstGrade = Number(prompt("Enter your first term grade (0 to 10): "))
    if (isNaN(firstGrade) || firstGrade <0 || firstGrade >10) {
        console.log("Invalid input!! The first grade must to be between 0 and 10. Please enter them again.")
        continue
    }

    let secondGrade = Number(prompt("Now, your second term grade (0 to 10): "))
    if (isNaN(secondGrade) || secondGrade <0 || secondGrade >10) {
        console.log("Invalid input!! The second grade must to be between 0 and 10. Please enter them again.")
        continue
    }

    const average = (firstGrade + secondGrade)/2
    console.log(`The average of grades is ${average.toFixed(2)}.`)

    while (true) {
        let university = Number(prompt(`Enter the code of your university
            1 - PUCPR
            2 - UNICAMP
            3 - EXIT
            Your choice: `
            ))

        if (university === 3) {
            console.log("Exiting the program. Goodbye!")
            break
        } else if (university < 1 || university > 3) {
             console.log('University code invalid, enter again:')
            continue
        }

        // Logic for PUCPR
        if (university === 1) {
            if (average >= 7) {
                console.log('You are approved!!')
            } else if (average >= 4.0 && average <= 6.9) {
                console.log("In final exam")
            } else {
                console.log("You are failed")
            }
        }
         // Logic for UNICAMP
        if (university === 2) {
            if (average >= 5) {
                console.log('You are approved!!')
            } else {
                console.log("In final exam")
            }
        }
    }
}
