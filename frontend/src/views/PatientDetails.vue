<template>
    <div class="container">
        <h2>Patient Details</h2>

        <p v-if="patients.length === 0">No patients available.</p>

        <table v-else>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Date of Birth</th>
                    <th>History of Cancer</th>
                    <th>Prediction</th>
                    <th>Confidence</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(patient, index) in patients" :key="index">
                    <td>{{ patient.first_name}}</td>
                    <td>{{ patient.last_name }}</td>
                    <td>{{ patient.date_of_birth }}</td>
                    <td>{{ patient.history ? 'Yes' : 'No' }}</td>
                    <td>{{ patient.prediction }}</td>
                    <td>{{ (patient.confidence * 100).toFixed(2) }}%</td>
                    <td>
                        <button class="edit" @click="editPatient(patient)">Edit</button>        
                        <button class="delete" @click="deletePatient(patient.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template> 
<script>
export default {
    data() {
        return {
            patients: []    //store patients from backend
        };
    },

    //runs automatically when page loads
    async mounted() {
        try {
            //call backend API to get patients for this doctor
            const response = await fetch("http://localhost:5000/patients", {
                credentials: "include"
        });
        
            //convert response to JSON
            const data = await response.json();

            //store data in patients array(for table display)
            this.patients = data;
        } catch (error) {
            //if anything fails, show error in console
            console.error("Error fetching patient data:", error);
        }
    },
    methods: {
        //edit button funtion
        editPatient(patient) {
            const newFirstName = prompt("First name:", patient.first_name);
            const newLastName = prompt("Last name:", patient.last_name);
            const newDateOfBirth = prompt("Date of Birth:", patient.date_of_birth);
            const newHistory = prompt("Does patient have a history of cancer? (1 = Yes, 0 = No):", patient.history);

            if (!newFirstName || !newLastName || !newDateOfBirth) return;
               
            this.updatePatient(patient.id, newFirstName, newLastName, newDateOfBirth, newHistory);
        },

        //Update Backend
        async updatePatient(id, first_name, last_name, date_of_birth, history) {
            try {
                await fetch(`http://localhost:5000/patients/${id}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    credentials: "include",
                    body: JSON.stringify({
                         first_name, 
                         last_name, 
                         date_of_birth, 
                         history: Number(history)})
                });

                //Update UI instantly
                const patient = this.patients.find(p => p.id === id);
                if (patient) {
                    patient.first_name = first_name;
                    patient.last_name = last_name;
                    patient.date_of_birth = date_of_birth;
                    patient.history = history ;
                }

            } catch (error) {
                console.error("Error updating patient data:", error);
            }
        },
        //delete button function
        async deletePatient(id) {
            try {
                await fetch(`http://localhost:5000/patients/${id}`, {
                    method: "DELETE",
                    credentials: "include"
                });

                //Remove patient from UI instantly
                this.patients = this.patients.filter(p => p.id !== id);
            } catch (error) {
                console.error("Error deleting patient data:", error);
            }
        }
    }
};
</script>

<style scoped>
.container {
    padding: 40px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th, td {
    border: 1px solid #E1E6EC;
    padding: 10px;
    text-align: center;
}

th {
    background-color: #F4BCDA;
    color: #B7087A;
}
</style>