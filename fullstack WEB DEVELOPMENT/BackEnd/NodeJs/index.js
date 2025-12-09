//const fs=require("fs");
// fs.writeFile("message.txt","hello node js",(err) => {
//     if (err) throw err;
//     console.log('The file has been saved!');
//   }); 
// cd




//import generatename from "sillyname";
// var generatename=require("sillyname")
//var sillyname=generatename();
//console.log(`My name is ${sillyname}d.`)



// import  superheroes from "superheroes";
// const name=superheroes.random();
// console.log(`i am ${name}`);

import inquirer from "inquirer";
import qr from "qr-image";
import fs from "fs";
inquirer
  .prompt([{
    message:"tper in your URL:",
    name:"URL",
  },
   
  ])
  .then((answers) => {
const url=answers.URL;
var qr_svg = qr.image(url);
qr_svg.pipe(fs.createWriteStream('qr_image.png'));
 
  })
  .catch((error) => {
    if (error.isTtyError) {
      // Prompt couldn't be rendered in the current environment
    } else {
      // Something else went wrong
    }
  });