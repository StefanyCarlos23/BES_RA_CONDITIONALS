while (true) {
    let ageInput = (prompt("Enter you age to find out if you can be a voter (or type '000' to exit): "))
    
    if (ageInput === "000") {
        break
    } 
    
    let userAge = Number(ageInput)

    if (isNaN(userAge)){
        alert("Invalid input")
    } else if (userAge < 16){
        alert(`You can't be a voter yet. Wait more ${16 - userAge} years.`)
    } else if (userAge >= 16 && userAge <18) {
        alert("You can be an optional voter")
    } else if (userAge >= 18 && userAge <=65){
        alert("You are required to be a voter")
    } else {
        alert("You are no longer required to vote")
    }
}