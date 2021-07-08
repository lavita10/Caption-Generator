<template>
<div id="app">
    <div id="nav">
      <router-link to="/">Try another Image!</router-link>
    </div>
    <router-view/> 
    <div class="vue-template">
        <div class="container inner-block vertical-center">
            <form>
                <h1>Image Caption Generator</h1>
                <div class="form-group">
                    <img src="#" id="userUploadedImg" alt="uploaded" />
                    <br/><br/>
                    <div class="row">
                        <div class="col-8">
                            <label for="caption1" id="captionText1" >My new caption</label>
                        </div>
                        <div class="col-4">
                            <input type="submit" class="btn btn-dark btn-sm" @click.prevent="readCaption(0)"  value="Read Caption"/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-8">
                            <label for="caption2" id="captionText2" >My new caption</label>
                        </div>
                        <div class="col-4">
                            <input type="submit" class="btn btn-dark btn-sm" @click.prevent="readCaption(1)" value="Read Caption"/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-8">
                            <label for="caption3" id="captionText3">My new caption</label>
                        </div>
                        <div class="col-4">
                            <input type="submit" class="btn btn-dark btn-sm" @click.prevent="readCaption(2)" value="Read Caption"/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-8">
                            <label for="caption4" id="captionText4">My new caption</label>
                        </div>
                        <div class="col-4">
                            <input type="submit" class="btn btn-dark btn-sm" aria-pressed="true" @click.prevent="readCaption(3)" value="Read Caption"/>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div> 
</template>

<script>
export default {
    name: 'Caption',
    data:{
      audioPlayed: false,
      AudioUrls : []                          
    },      
    methods: {
      readCaption(index){
        //  myTrack.play()
        var myTrack = new Audio(this.AudioUrls[index]);
        var playPromise = myTrack.play()
        console.log(playPromise)
        if (playPromise !== undefined){
            playPromise.then(function() {
                this.audioPlayed = true
                console.log("Automatic playback started!");
            }).catch(function(error) {
                console.log("Automatic playback failed.");
                console.log(error)
                // Show a UI element to let the user manually start playback.
            });
        }
      }
    },
    mounted() {
        const data = this.$route.query;
        document.getElementById("userUploadedImg").src = data["image"];
        document.getElementById("captionText1").innerHTML = data["caption"][0];
        document.getElementById("captionText2").innerHTML = data["caption"][1];
        document.getElementById("captionText3").innerHTML = data["caption"][2];
        document.getElementById("captionText4").innerHTML = data["caption"][3];
        this.AudioUrls = [data["AudioURL0"], data["AudioURL1"], data["AudioURL2"], data["AudioURL3"]]
        // this.AudioUrls.push(data["AudioURL0"])
        // this.AudioUrls.push(data["AudioURL1"])
        // this.AudioUrls.push(data["AudioURL2"])
        // this.AudioUrls.push(data["AudioURL3"])
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
img {
    height: 75%;
    width: 75%;
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