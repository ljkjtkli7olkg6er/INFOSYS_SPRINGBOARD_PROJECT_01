import express from "express";

const app = express();
const port = 3000;
app.set("view engine","ejs");
app.get("/", (req, res) => {
    const data={
        title:"EJS",
       seconds : new Date().getMinutes(),
       items:["apple","orange","grapes"],

    }
   res.render("index2",data)


});

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
  });