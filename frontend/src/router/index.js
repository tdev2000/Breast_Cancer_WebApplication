import { createRouter } from "vue-router";  
import { createWebHistory } from "vue-router";

import Welcome from '../views/Welcome.vue';
import Register from '../views/Register.vue';
import Login from '../views/Login.vue';
import Upload from '../views/Upload.vue';

const routes = [
    { path: '/', name: 'Welcome', component: Welcome },
    { path: '/register', name: 'Register', component: Register },
    { path: '/login', name: 'Login', component: Login },
    { path: '/upload', name: 'Upload', component: Upload } 
]

const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router;