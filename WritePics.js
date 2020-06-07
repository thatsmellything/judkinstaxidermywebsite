//document.body.onload = run;

getCount('Images');

function loadHowManyPictures(){

}

function writeImagesIntoHTML(){
    
}


function getCount(foldername)
    {
      var myObject, f, filesCount;
      myObject = new ActiveXObject("Scripting.FileSystemObject");
      f = myObject.GetFolder(foldername);
      filesCount = f.files.Count;
      document.write("The number of files in this folder is: " + filesCount);
    }
function test1(){

//requiring path and fs modules
const path = require('path');
const fs = require('fs');
//joining path of directory 
const directoryPath = path.join(__dirname, 'Documents');
//passsing directoryPath and callback function
fs.readdir(directoryPath, function (err, files) {
    //handling error
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    } 
    //listing all files using forEach
    files.forEach(function (file) {
        // Do whatever you want to do with the file
        console.log(file); 
    });
});
}
