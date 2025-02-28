while (true) {
    let schoolGrades = Number(prompt("Enter your grade: "))

    if (isNaN(schoolGrades)) {
        alert("Invalid input! Please enter a valid number.");
        continue;
    }
    if (schoolGrades >10 || schoolGrades <0){
        alert("Invalid grade!!")
    continue
    } else{
        if (schoolGrades >=7) {
            alert("Student approved!!")
        } else if (schoolGrades <7 && schoolGrades >=4) {
            alert("Student in recovery")
        } else {
            alert("Failed student!!")
        }
        break
    }
}
