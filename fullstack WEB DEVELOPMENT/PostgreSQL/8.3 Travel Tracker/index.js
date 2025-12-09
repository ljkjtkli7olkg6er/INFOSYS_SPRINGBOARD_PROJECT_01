import express from "express";
import bodyParser from "body-parser";
import pg from "pg";
const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
const db = new pg.Client({
  user: "postgres",
  host: "localhost",
  database: "world",
  password: "Jay@1234",
  port: 5432,
});
db.connect();
app.get("/", async (req, res) => {
 const result=await db.query("select  country_code from visited_countryies");
 let countries=[];
 countries.push(Country.country_code);
 result.rows.forEach((country) => {
  countries.push(country.country_code);
});
console.log(result.rows);
res.render("index.ejs", { countries: countries, total: countries.length });
db.end()
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
