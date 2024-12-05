function get_info() {
    // Retrieve values
    const firstName = document.getElementById("firstname").value.trim();
    const lastName = document.getElementById("lastname").value.trim();
    const fatherName = document.getElementById("fathername").value.trim();
    const motherName = document.getElementById("mothername").value.trim();
    const email = document.getElementById("email").value.trim();
    const phoneNumber = document.getElementById("pno").value.trim();
    const dob = document.getElementById("dob").value;
    const quali = document.getElementById("quali").value.trim();
    
    //Radio button validation
    const gender = document.querySelector('input[name="gender"]:checked');
    if (!gender) {
        alert("Please select your gender.");
        return;
    }

    // Basic Validation
    if (firstName === "" || lastName === "" || fatherName === "" || motherName === "" || email === "" ||
        phoneNumber === "" || dob === "" || quali === "") {
        alert("All fields are required.");
        return;
    }
    
    // Email Validation
    const emailPattern =  /@.*\.com$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return;
    }
    
    // Phone Number Validation (assuming 10 digits)
    if (phoneNumber.length !== 10 || isNaN(phoneNumber)) {
        alert("Please enter a valid 10-digit phone number.");
        return;
    }

    // If all validations pass, display the entered details
    document.write(
        "ENTERED DETAILS ARE:<br><hr>" +
        "<b>First name:</b> " + firstName +
        "<br><b>Last name:</b> " + lastName +
        "<br><b>Father's name:</b> " + fatherName +
        "<br><b>Mother's name:</b> " + motherName +
        "<br><b>E-mail:</b> " + email +
        "<br><b>Phone number:</b> " + phoneNumber +
        "<br><b>Date of Birth:</b> " + dob +
        "<br><b>Gender:</b> " + gender.value +
        "<br><b>Qualification:</b> " + quali
    );

    alert("User Registration Successful.");
}