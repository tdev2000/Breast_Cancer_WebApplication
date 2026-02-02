<template>
    <div class="container">
        <h2>Registration</h2>

        <input placeholder="Enter your name"/>
        <input placeholder="Enter your email"/>
        <input type="password" placeholder="Password"/>

        <label class="checkbox">
            <input type="checkbox"/> I agree with <span>Terms and Conditions</span> and <span>Privacy Policy</span>
        </label>

        <button class="primary">Sign Up</button>
        <p class="small">Already have an account? <span @click="$router.push('/login')">Log in</span></p>
    </div>
</template>

<style scoped>
.container{
    text-align: center;
    padding: 40px;
}
input{
    width: 260px;
    padding: 12px;
    border-radius: 20px;
    border: none;
    background: #F4BCDA;
    margin: 10px 0;
}
.checkbox{
    font-size: 14px;
}
span{
    color: #DE77AB;
    cursor: pointer;
}
.primary{
    background: #B7087A;
    color: white;
    padding: 12px 40px;
    border-radius: 25px;
    border: none;
}
.small{
    color: #000000;
}
</style>
