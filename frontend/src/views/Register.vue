<template>
    <div class="container">
        <h2>Registration</h2>

        <input v-model="name" placeholder="Enter your name" />
        <input v-model="email" placeholder="Enter your email" />
        <input v-model="password" type="password" placeholder="Password" />

        <label class="checkbox">
            <input type="checkbox" />I agree with <span>Terms and Conditions</span> and <span>Privacy Policy</span>
        </label>

        <button class="primary" @click="register">Sign Up</button>
        <p class="small">Already have an account? <span @click="$router.push('/login')">Log in</span></p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            name: "",
            email: "",
            password: ""
        };
    },
    methods: {
        async register() {
            if (this.password.length < 8) {
                alert("Password must be at least 8 characters long.");
                return;
            }

            try {
                const response = await fetch("http://localhost:5000/register", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        name: this.name,
                        email: this.email,
                        password: this.password
                    })
                });

                const data = await respone.json();

                if (response.ok) {
                    alert("Registration successful! Please log in.");
                    this.$router.push('/login');
                } else {
                    alert("Registration failed: " + data.message);
                }
            } catch (error) {
                console.error(error);
                alert("Registration failed. Please try again.");
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

.checkbox {
    font-size: 14px;
    align-items: center;
    margin: 10px 0;
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
    color: #000000;
}
</style>
