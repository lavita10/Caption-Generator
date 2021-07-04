<template>
  <div class="vue-template"  style="padding-top:80px">
    <div class="container inner-block vertical-center">
      <form>
       <h1>Image Caption Generator</h1>
       <div class="form-group" style="text-align:center">
          <label>Choose an Image</label><br/>
          <div style="text-align:center">
            <!--<input type="file" name="file" @change="onFileChanged" accept=".jpg, .jpeg, .png" >-->
            <input class="file" id="userUploadedImage" name="file" type="file" accept=".jpg"/>
          </div>
        </div>
        <br/>
        <button :disabled='isDisabled' @click.prevent="submit()" class="btn btn-dark btn-lg btn-block" > Predict Caption </button>
        <!--<input type = "submit"  :disabled="isDisable(userUploadedImage)" @click.prevent="submit()" class="btn btn-dark btn-lg btn-block"/>-->
      </form>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'Home',
  computed: {
    isDisabled() {
      return true;
      }
   },
  methods: {
    // isDisable(file) {
    //   return file.length > 0;
    // },
    // update(e){
    //   let file = e.target.files[0];
    //   //console.log(file);
    //   let param = new FormData(); //Create form object
    //   param.append('file',file);//Add data to the form object through append
    //   console.log(param.get('file')); //FormData private class object, can not be accessed, you can judge whether the value is passed in through get
    //   //console.log("showed file");
    //   axios.post('http://127.0.0.1:5000/upload',param,{headers:{'Content-Type':'application/x-www-form-urlencoded' }}, ) //The request header must be a form
    //   .then(response=>{
    //     console.log("within then");
    //     console.log(response.data);
    //     alert('Upload Successful');
    //   })
    //   .catch(function (error) {
    //     console.log("within catch");
    //     console.log(error);
    //   })
    //},
    submit(){
      const e = document.getElementById("userUploadedImage");
      let file = e.files[0];
      let queryParameter = "";
      //console.log(file);
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
<!--<script>
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
</script>-->

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