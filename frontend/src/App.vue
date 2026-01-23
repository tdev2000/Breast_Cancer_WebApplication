<template>
  <div class="page">
    <!--Logo Image-->
    <img src="@/assets/logo.png" alt="Logo" />
    <!--Title section-->
    <h2>
      Clinician <span>Breast Cancer Detection System</span> For Clinicians
    </h2>

    <!--Next Button-->
    <button @click="$emit('next')">Next</button>
    </div>
 </template>

 <style>
  .page {
    background-color: #F4bcda;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  </style>