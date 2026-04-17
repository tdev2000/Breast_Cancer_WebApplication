<template>
    <div class="container">
        
       <!--Welcome Message-->
       <h1>Welcome,Dr. {{ doctorName }}</h1>
       <p class="subtitle">Breast Cancer Detection Dashboard</p>

       <!--Crads-->
       <div class="cards">

            <!--Total Patients-->
            <div class="card">
                <h3>Total Patients</h3>
                <p class="number">{{ patients.length }}</p>
            </div>

            <!--Last Prediction-->
            <div class="card">
                <h3>Last Prediction</h3>
                <p v-if="patients.length > 0">
                    {{ patients[patients.length - 1].prediction }} 
                </p>
                <p v-else>No predictions available</p>
            </div>

            <!--Last Confidence-->
            <div class="card">
                <h3>Last Confidence</h3>
                <p v-if="patients.length > 0">
                    {{ (patients[patients.length - 1].confidence * 100).toFixed(2) }}%
                </p>
                <p v-else>No confidence available</p>
            </div>

            <!--Quick Actions-->
            <div class="actions">
                <h3>Quick Actions</h3>
                <button @click="$router.push('/upload')">Upload New Image</button>
                <br>
                <button @click="$router.push('/patients')">View Patients</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            doctorName: '',
            patients: []
        };
    },

    async mounted() {
        //get doctor name 
        this.doctorName = localStorage.getItem("doctorName");

        try {
            //get doctor name and ID from local storage
            const doctorId = localStorage.getItem("doctorId");

            //fetch patients for this doctor
            const response = await fetch(`http://localhost:5000/api/patients?doctorId=${doctorId}`);
            const data = await response.json();
            this.patients = data;
        } catch (error) {
            console.error("Error fetching dashboard data:", error);
        }
    }
};
</script>

<style scoped>
.container {
    padding: 40px;
}

.subtitle {
    color: #B4B4B4;
    margin-bottom: 30px;
}

/*Cards layout*/
.cards {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
}

.card {
    flex: 1;
    background: #F4BCDA;
    padding: 20px;
    border-radius: 20px;    
    text-align: center;
}

.number {
    font-size: 30px;
    font-weight: bold;
    color: #B7087A;
}

/*Buttons*/
.actions {
    margin-top: 20px;
}

button {
    background: #B7087A;
    color: white;
    padding: 12px 30px;
    border: none;
    border-radius: 20px;
    margin-right: 10px;
    cursor: pointer;
}

button:hover {
    opacity: 0.8;
}
</style>