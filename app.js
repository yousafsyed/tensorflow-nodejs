var express = require('express');
var app = express();
var path = require('path');
var FormData = require('form-data');
var fs = require('fs');

var formidable = require('formidable')



app.use('/static', express.static('public'))

// respond with "hello world" when a GET request is made to the homepage
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});


app.post('/upload', function(req, res) {
    
   var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
       // console.log(files);
      var oldpath = files.webcam.path;
      var newpath = './files/' + files.webcam.name;
      fs.rename(oldpath, newpath, function (err) {
        if (err) throw err;
        res.send(JSON.stringify({"sucess":"uploaded"})).end();
      });
    });
});


app.options('/upload', function(req, res) {
        //console.log('OPTIONS');
        res.status(200).send();
    });


app.listen(3000, function () {
  console.log('App listening on port 3000!')
})