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
            //get logged-in doctor ID browser storage
            const dotorId = localStorage.getItem("dotorId");

            //call backend API to get patients for this doctor
            const response = await fetch(`http://localhost:8080/api/patients?doctorId=${dotorId}`);
        
            //convert response to JSON
            const data = await response.json();

            //store data in patients array(for table display)
            this.patients = data;
        } catch (error) {
            //if anything fails, show error in console
            console.error("Error fetching patient data:", error);
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