import express from "express";
import bodyParser from "body-parser";

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
    res.render("index3.ejs")
});

app.post("/submit", (req, res) => {
   const numletters= req.body["fName"].length+req.body["LName"];
   res.render("index3.ejs",{Number_of_letters:numletters})
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
})
