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
                    <td>{{ patient.firstName }}</td>
                    <td>{{ patient.lastName }}</td>
                    <td>{{ patient.dateOfBirth }}</td>
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
            patients: []
        };
    },
    mounted() {
        //Load patients from localStorage
        const savedPatients = localStorage.getItem("patients");
        if (savedPatients) {
            this.patients = JSON.parse(savedPatients);
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