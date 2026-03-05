
let students = JSON.parse(localStorage.getItem("students")) || [];

function clearErrors() {
    document.querySelectorAll(".error").forEach(e => e.innerText = "");
}

function saveData() {
    localStorage.setItem("students", JSON.stringify(students));
}

function displayStudents(data) {
    let table = document.getElementById("studentTable");
    table.innerHTML = "";

    data.forEach((student, index) => {
        table.innerHTML += `
            <tr>
                <td>${student.studentId}</td>
                <td>${student.name}</td>
                <td>${student.age}</td>
                <td>${student.gender}</td>
                <td>${student.grade}</td>
                <td>${student.contact}</td>
                <td>
                    <button onclick="editStudent(${index})">Update</button>
                    <button onclick="deleteStudent(${index})">Delete</button>
                </td>
            </tr>
        `;
    });
}

function addStudent() {
    clearErrors();

    let studentId = document.getElementById("studentId").value.trim();
    let name = document.getElementById("name").value.trim();
    let age = document.getElementById("age").value.trim();
    let gender = document.getElementById("gender").value;
    let grade = document.getElementById("grade").value.trim();
    let contact = document.getElementById("contact").value.trim();
    let editIndex = document.getElementById("editIndex").value;

    let valid = true;

    if (studentId === "") {
        document.getElementById("idError").innerText = "Student ID is required";
        valid = false;
    }

    if (name === "") {
        document.getElementById("nameError").innerText = "Name is required";
        valid = false;
    }

    if (age === "" || age < 1 || age > 100) {
        document.getElementById("ageError").innerText = "Age must be between 1 and 100";
        valid = false;
    }

    if (gender === "") {
        document.getElementById("genderError").innerText = "Please select gender";
        valid = false;
    }

    if (grade === "") {
        document.getElementById("gradeError").innerText = "Grade is required";
        valid = false;
    }

    if (!/^[0-9]{10}$/.test(contact)) {
        document.getElementById("contactError").innerText = "Contact must be exactly 10 digits";
        valid = false;
    }

    if (!valid) return;

    // Unique ID check
    if (editIndex === "") {
        let exists = students.some(student => student.studentId === studentId);
        if (exists) {
            document.getElementById("idError").innerText = "Student ID already exists";
            return;
        }
        students.push({ studentId, name, age, gender, grade, contact });
    } else {
        students[editIndex] = { studentId, name, age, gender, grade, contact };
        document.getElementById("editIndex").value = "";
    }

    saveData();
    clearFields();
}

function editStudent(index) {
    let student = students[index];
    document.getElementById("studentId").value = student.studentId;
    document.getElementById("name").value = student.name;
    document.getElementById("age").value = student.age;
    document.getElementById("gender").value = student.gender;
    document.getElementById("grade").value = student.grade;
    document.getElementById("contact").value = student.contact;
    document.getElementById("editIndex").value = index;
}

function deleteStudent(index) {
    students.splice(index, 1);
    saveData();
    displayStudents(students);
}

function searchStudent() {
    let searchId = prompt("Enter Student ID:");
    if (!searchId) return;

    let found = students.find(s => s.studentId === searchId.trim());
    if (found) {
        displayStudents([found]);
    }
}

function showStudents() {
    displayStudents(students);
}

function exitSystem() {
    location.reload();
}

function clearFields() {
    document.getElementById("studentId").value = "";
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("gender").value = "";
    document.getElementById("grade").value = "";
    document.getElementById("contact").value = "";
}

