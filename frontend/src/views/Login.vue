<template>
    <div class="container">
        <h2>Log in</h2>
        <p class=" small">Sign in to your account to get access of various features</p>

        <input type="email" placeholder="Enter you email"/>
        <input type="password" placeholder="Password"/>

        <p class="link">Forgot Password ?</p>

        <button class="primary">Log in</button>

        <P class="small">Don't have an account? <span @click="$router.push('/register')">Sign Up</span></P>
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
    .link{
        color: #D93E8B;
        cursor: pointer;
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