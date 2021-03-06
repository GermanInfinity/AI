/** DATABASE INTIALIZATION **/
const db = require("./models");
const SkillController = require("./controllers/Skill.controller");
const UserController = require("./controllers/User.controller");


/** API INTIALIZATION **/
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();

var corsOptions = {
  origin: "http://localhost:8000"
};
var fname;

app.use(cors(corsOptions));

// parse requests of content-type - application/json
app.use(bodyParser.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// simple route
app.get("/", (req, res) => {
  res.json({ message: "Welcome to ShipTek" });
});

require("./routes/User.routes")(app);
require("./routes/Home.routes")(app);

// set port, listen for requests
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});





/** DATABASE RUN **/ 
const run = async () => {

};

// db.sequelize.sync();
db.sequelize.sync({ }).then(() => {
  console.log("Drop and re-sync db.");
  run();
});
