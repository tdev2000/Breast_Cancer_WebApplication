<template>
    <div class="container">
        <h2>Patient Information</h2>

        <input placeholder="First Name" />
        <input placeholder="Last Name" />
        <input type="date" placeholder="Date of Birth" />

        <select>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
        </select>

        <label>
            <input type="checkbox" />History of Cancer
        </label>

        <input type="file" />

        <button class="primary">Upload</button>
        <p class="result">Prediction will appear here</p>
    </div>
</template>

    <script>
    export default {
        name: "Upload"
    }
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