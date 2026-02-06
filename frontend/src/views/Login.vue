<template>
    <div class="container">
        <h2>Log in</h2>
        <p class=" small">Sign in to your account to get access of various features</p>

        <input type="email" v-model="email" placeholder="Enter you email" />
        <input type="password" v-model="password" placeholder="Password" />

        <p class="link">Forgot Password ?</p>

        <button class="primary" @click="login">Log in</button>
        <P class="small">Don't have an account? <span @click="$router.push('/register')">Sign Up</span></P>
    </div>
</template>
<script>
export default {
    data() {
        return {
            email: "",
            password: ""
        };
    },
    methods: {
        login() {
            const savedEmail = localStorage.getItem("doctorEmail");
            const savedPassword = localStorage.getItem("doctorPassword");

            if (this.email === savedEmail && this.password === savedPassword) {
                localStorage.setItem("isLoggedIn", "true");
                this.$router.push('/upload');
            } else {
                alert("Invalid email or password. Please try again.");
            }
        }
    }
};
</script>

<style scoped>
.container {
    max-width: 400px;
    margin: 0 auto;
    padding: 40px;

    display: flex;
    flex-direction: column;
    align-items: center;
}

input {
    width: 260px;
    padding: 12px;
    border-radius: 20px;
    border: none;
    background: #F4BCDA;
    margin: 10px 0;
}

.link {
    color: #D93E8B;
    cursor: pointer;
}

span {
    color: #DE77AB;
    cursor: pointer;
}

.primary {
    background: #B7087A;
    color: white;
    padding: 12px 40px;
    border-radius: 25px;
    border: none;
}

.small {
    color: #B4B4B4;
}
</style>