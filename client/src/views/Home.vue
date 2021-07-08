<template>
  <div class="vue-template"  style="padding-top:80px">
    <div class="container inner-block vertical-center">
      <form>
       <h1>Image Caption Generator</h1>
       <div class="form-group" style="text-align:center">
          <label>Choose an Image</label><br/>
          <div style="text-align:center">
            <!--<input type="file" name="file" @change="onFileChanged" accept=".jpg, .jpeg, .png" >-->
            <input v-on:change="checkifEmpty($event)" class="file" id="userUploadedImage" name="file" type="file" accept=".jpg"/>
          </div>
        </div>
        <br/>
        <button disabled=True id="predictCaptionButton" @click.prevent="submit()" class="btn btn-dark btn-lg btn-block" > Generate Caption </button>
        <!--<input type = "submit"  :disabled="isDisable(userUploadedImage)" @click.prevent="submit()" class="btn btn-dark btn-lg btn-block"/>-->
      </form>
    </div>
  </div>                      
</template>   
<script>
import axios from 'axios';
export default {
  name: 'Home',
  methods: {
    checkifEmpty(e){
      if(e.srcElement.files.length > 0){

        document.getElementById("predictCaptionButton").disabled = false;
      }else{
        document.getElementById("predictCaptionButton").disabled = true;
      }
        
    },
    submit(){
      const e = document.getElementById("userUploadedImage");
      let file = e.files[0];
      let queryParameter = "";
      let param = new FormData(); //Create form object
      param.append('file',file);//Add data to the form object through append
      console.log(param.get('file')); //FormData private class object, can not be accessed, you can judge whether the value is passed in through get
      //console.log("showed file");
      axios.post('http://127.0.0.1:5000/upload',param,{headers:{'Content-Type':'application/x-www-form-urlencoded' }}, ) //The request header must be a form
      .then(response=>{
        //console.log("within then");
        console.log(response.data);
        //alert('Upload Successful');
        queryParameter =  response.data;
        this.$router.push({name:'Caption', query: queryParameter});
      })
      .catch(function (error) {
        console.log("within catch");
        console.log(error);
      })
      
    },
  }
}
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