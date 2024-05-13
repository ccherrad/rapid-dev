<template>
  <NuxtLayout name="login">
  <div class="bg-gray-100 flex flex-col items-center justify-center">
    <h2 class="text-3xl text-center text-gray-900 mb-8">Log in</h2>
    <div class="space-y-4 w-full max-w-xs">
      <button class="w-full flex items-center justify-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50" @click="loginWithGoogle">
        <i class="fab fa-google text-red-500 mr-2"></i> Continue with Google
      </button>
      <button class="w-full flex items-center justify-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50" @click="loginWithApple">
        <i class="fab fa-apple text-black mr-2"></i> Continue with Apple
      </button>
      <div class="border-t border-gray-300 my-6 w-full"></div>
      <div class="flex flex-col space-y-4">
        <label for="email" class="sr-only">Email</label>
        <input id="email" name="email" type="email" required v-model="email" @input="validateEmail" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Enter your email address...">
        <button class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none" @click="loginWithEmail">
          Continue with email
        </button>
      </div>
      <div class="text-center text-sm text-gray-500">
        <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">Forgot password?</a>
      </div>
      <div class="text-center text-sm text-gray-500">
        You can also <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">continue with SAML SSO</a>
      </div>
    </div>
    <div class="mt-6 text-center text-xs text-gray-500 w-full max-w-xs">
      By clicking "Continue with Apple/Google/Email/SAML" above, you acknowledge that you have read and understood, and agree to Notion's <a href="#" class="text-indigo-600 hover:text-indigo-500">Terms & Conditions</a> and <a href="#" class="text-indigo-600 hover:text-indigo-500">Privacy Policy</a>.
    </div>
  </div>
  </NuxtLayout>
</template>

<script>
export default {
  data() {
    return {
      email: ''
    };
  },
  methods: {
    loginWithGoogle() {
      // Implement Google login logic here
    },
    loginWithApple() {
      // Implement Apple login logic here
    },
    loginWithEmail() {
      // Implement email login logic here
    },
    validateEmail() {
      // Implement email validation logic here if needed
    }
  }
};
</script>

<style>
/* Add your CSS styles here */
body {
  font-family: 'Open Sans', sans-serif;
}
</style>

