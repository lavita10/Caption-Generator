<template>
  <div class="vue-template">
    <div class="container inner-block vertical-center">
      <form>
       <h1>Image Caption Generator</h1>
       <div class="form-group">
          <label>Profile Picture</label>
          <!--<input type="file" name="file" @change="onFileChanged" accept=".jpg, .jpeg, .png" >-->
          <input class="file" name="file" type="file" accept="image/png,image/gif,image/jpeg" @change="update"/>
        </div>
        <button @click.prevent="submit()" class="btn btn-dark btn-lg btn-block"> Upload </button>
      </form>
    </div>
  </div>
</template>
<!--<script>
  export default {
  methods: {
      update(e){
        let file = e.target.files[0];
        let param = new FormData(); //Create form object
        param.append('file',file);//Add data to the form object through append
        console.log(param.get('file')); //FormData private class object, can not be accessed, you can judge whether the value is passed in through get
        this.$axios.post('http://127.0.0.1:5000/upload',param,{headers:{'Content-Type':'application/x-www-form-urlencoded' }}, ) //The request header must be a form
          .then(response=>{
            console.log(response.data);
          })
          .catch(function (error) {
            console.log(error);
          })
      }
    }
}
</script>-->
<script>
//import axios from 'axios';
export default {
  //components : {Navigation},
  name: 'HomePage',                                          
  data() {
    return {
      selectedFile: null
    };
  },
  methods: {
    onFileChanged (event) {
      this.selectedFile = event.target.files[0]
    },
    submit(){
      this.handleSubmit();
    },
    handleSubmit() {
      const data = {
      uploadPic: this.selectedFile,
      };
      console.log(data);
      //this.createProfile(data)    
    },
  },
};
</script>

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