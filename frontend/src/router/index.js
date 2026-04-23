import { createRouter } from "vue-router";  
import { createWebHistory } from "vue-router";

import Welcome from '../views/Welcome.vue';        
import Register from '../views/Register.vue';
import Login from '../views/Login.vue';
import Upload from '../views/Upload.vue';
import PatientDetails from "../views/PatientDetails.vue";     
import Dashboard from "@/views/Dashboard.vue";

const routes = [
    { path: '/', name: 'Welcome', component: Welcome },
    { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true }}, // Protected route
    { path: '/register', name: 'Register', component: Register },
    { path: '/login', name: 'Login', component: Login },
    { path: '/upload', name: 'Upload', component: Upload , meta: { requiresAuth: true }}, // Protected route
    { path: '/patients', name: 'PatientDetails', component: PatientDetails, meta: { requiresAuth: true }} // Protected route
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

// Navigation guard
router.beforeEach((to, from, next) => {
    const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

    // allow public pages
    const publicPages = ['/', '/login', '/register'];

    // block protected routes
    if (to.meta.requiresAuth && !isLoggedIn) {
        return next('/login');
    }

    next();
});

export default router;