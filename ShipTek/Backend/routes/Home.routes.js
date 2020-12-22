module.exports = app => {
  const user = require("../controllers/User.controller.js");
  const db = require("../models");
  const User = db.User;
  // var origin1 = new google.maps.LatLng(55.930385, -3.118425);
  // var origin2 = 'Greenwich, England';
  // var destinationA = 'Stockholm, Sweden';
  // var destinationB = new google.maps.LatLng(50.087692, 14.421150);

  var router = require("express").Router();



  //HOME
  app.post("/dashboard", (req, res) => {
    user.dashboard({ email: "evans@gmail.com" });

    //res.json({ username: user.Username});

  })

  //SUGGESTIONS
  app.get("/findTech", async (req, res) => {
    var technicians = await User.findAll({ where: {isTech: 1}});
    res.json({
      technicians: technicians,
    })
    console.log("All techs:", JSON.stringify(technicians, null, 2));
  })


  //SEARCH FOR TECHNICIAN
  // app.post("/find", (req, res) => { 
  //   user.find({ userLocation: req.location });
  // })

};

