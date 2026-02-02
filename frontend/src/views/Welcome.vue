<template>
    <div class="container">
        <!--Logo-->
        <img src="@/assets/logo.png" class="logo"/>
        <!--Title-->
        <h1>
            Clinician <span>Breast Cancer Detection System</span> For Clinicians
        </h1>

        <!--Subtitle-->
        <p class="subtitle">Let's get started...</p>
        <p class="small">Login to find your doctor and connect with them</p>

        <!--Buttons-->
        <button class="primary" @click="$router.push('/login')">Log in</button>
        <button class="outline" @click="$router.push('/register')">Sign Up</button>
    </div>
</template>  

<style scoped>
.container{
    text-align: center;
    padding: 40px;
}
.logo{
    width: 120px;
    margin-bottom: 20px;
}
h1 span{
    color: #B7087A;
}
.primary{
    background: #B7087A;
    color: white;
    padding: 12px 40px;
    border-radius: 25px;
    border: none;
    margin: 10px 0;
}
.outline{
    background: transparent;
    color: #B7087A;
    border: 2px solid #B7087A;
    padding: 12px 40px;
    border-radius: 25px;
}
.subtitle{
    font-weight: bold;
}
.small{
    color: #B4B4B4;
}
</style>