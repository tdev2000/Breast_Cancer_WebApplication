<template>
    <div class="container">
        <h2>Patient Information</h2>

        <!--Patient details-->
        <input v-model="firstName" placeholder="First Name" />
        <input v-model="lastName" placeholder="Last Name" />
        <input v-model="dateOfBirth" type="date" placeholder="Date of Birth" />

        <label class="checkbox">
            <input type="checkbox" v-model="history"/>History of Cancer
        </label>
        
        <!--Image Upload-->
        <input type="file" @change="handleFileUpload"/>

        <button class="primary" @click="uploadImage">Upload & Predict</button>

        <!--Prediction Result-->
        <p v-if="result && result.prediction" class="result">
            Prediction: {{ result.prediction }} <br/>
            Confidence: {{ result.confidence ? (result.confidence * 100).toFixed(2) + '%' : 'N/A' }}
        </p>

        <div v-if="result?.referral_suggestions">
            <h3>Referral Suggestions</h3>
            <div v-for="doc in result.referral_suggestions" :key="doc.id" >
                <p>
                    {{ doc.name }}
                    ({{ doc.specialization }})
                    {{ doc.rating }}
                </p>
            </div>
        </div>
    </div>
</template>

    <script>
    export default {
        name: "Upload",
        data() {
            return {
                firstName: '',
                lastName: '',
                dateOfBirth: '',
                history: false,
                image: null,
                result: null
            };
        },
        //uploadImage
        methods: {
            //store selected file
            handleFileUpload(event) {
                this.image = event.target.files[0];
            },

            //send image to Flask
            async uploadImage() {
                if (!this.image) {
                    alert("Please select a file first.");
                    return;
                }

                const formData = new FormData();

                //sending everything before fetching
                formData.append('image', this.image);
                formData.append('firstName', this.firstName);
                formData.append('lastName', this.lastName)
                formData.append('dateOfBirth', this.dateOfBirth);
                formData.append('history', this.history);
                
                try {
                    const response = await fetch('http://localhost:5000/predict', {
                        method: 'POST',
                        body: formData,
                        credentials: "include"
                    });

                    const data = await response.json();
                    //show result
                    this.result = data;
                    
                    alert("Patient details saved successfully.");
                
                } catch (error) {
                    console.error('There was a problem with the fetch operation:', error);
                    alert('Failed to upload image. Please try again.');
                }
            }
        }
    };
    </script>

    <style scoped>
    .container{ 
    padding: 40px;
    }

    input, select{
    display: block;
    margin: 10px 0;
    padding: 10px;
    width: 260px;
    border-radius: 10px;
    background: #F4BCDA;
    border: none;
    }

    .primary{
    background: #B7087A;
    color: white;
    padding: 12px 40px;
    border-radius: 25px;
    border: none;
    }
    
    .result{
    margin-top: 20px;
    font-weight: bold;
}
</style>