const fetch = require("node-fetch");



url = "https://brainlife.io/api/warehouse/project/"


fetch(url).then(function(response) {
    return response.json();
  }).then(function(data) { 
      console.log(data)   

}).catch(function() {
    console.log("Exception occured");
  });