<template>
  <div class="vue-template">
    <div class="container inner-block vertical-center">
      <form>
       <h1>Image Caption Generator</h1>
       <div class="form-group">
          <label>Image</label>
          <!--<input type="file" name="file" @change="onFileChanged" accept=".jpg, .jpeg, .png" >-->
          <!--<input class="file" name="file" type="file" accept="image/png,image/gif,image/jpeg" @change="update"/>-->
          <p>My new caption</p>
        </div>
        <!--<button @click.prevent="submit()" class="btn btn-dark btn-lg btn-block"> Upload </button>-->
      </form>
    </div>
  </div>
</template>

<style scoped>
  .container {
    margin-top: 0.5rem;
  }
  * {
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    font-weight: 400;
}

body,
html,
.App,
.vue-template,
.vertical-center {
    width: 100%;
    height: 100%;
}

.navbar-light {
    background-color: #ffffff;
    box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
}

.vertical-center {
    display: flex;
    text-align: center;
    justify-content: center;
    flex-direction: column;    
}

.inner-block {
    width: 450px;
    margin: auto;
    background: #ffffff;
    box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
    padding: 40px 55px 45px 55px;
    border-radius: 15px;
    transition: all .3s;
}

.vertical-center .form-control:focus {
    border-color: #2554FF;
    box-shadow: none;
}

.vertical-center h3 {
    text-align: center;
    margin: 0;
    line-height: 1;
    padding-bottom: 20px;
}

label {
    font-weight: 500;
}
</style>