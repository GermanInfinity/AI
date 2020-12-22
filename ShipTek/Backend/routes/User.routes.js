module.exports = app => {
  const user = require("../controllers/User.controller.js");

  var router = require("express").Router();
  const db = require("../models");
  const User = db.User;

  // Create a new User
  router.post("/abc", user.create);
  
  app.use('/api/User', router);

  app.post("/test", (req, res) => {
  	user.create({name: "NewUser2", password: "1234"});
    res.json({ message: "In user" });
   
  });

  //SIGN UP 
  app.post("/sign-up", (req, res) => {
      var name = req.body.username;
      var electronicMail = req.body.email;
      var pass = req.body.password;
      var techNic  = req.body.tech;
      var skillsIn = req.body.skills;
      var descp = req.body.selfDescription;
      var addy = req.body.address;

      User.count({ where: {username: name}})
      .then(count => {

        if (count != 0) {
          res.status(403).send({
            message: "Username already exists!"
          });
          return; 
        }


        User.count({ where: {email: electronicMail}})
            .then(count => {
              if (count != 0) {
              res.status(403).send({
              message: "Email already exists!"
            });
                return true;
              }
          
          if (techNic == 1) {
              User.create({ Username: name,
                      Email: electronicMail, 
                      Password: pass,
                      IsTech: techNic,
                      Skills: skillsIn,
                      SelfDescription: descp,
                      Address: addy});

             return true; 
          }
          User.create({ Username: name,
                      Email: electronicMail, 
                      Password: pass,
                      IsTech: techNic});

        });
    });

  })

  //SIGN IN 
  app.post("/sign-in", async (req, res) => {

      var name = req.body.username;
      var electronicMail = req.body.email;
      var pass = req.body.password;
      var techNic  = req.body.tech;
      var skillsIn = req.body.skills;
      var descp = req.body.selfDescription;
      var addy = req.body.address;

      const userEmail = await User.findOne({ where: { Email: electronicMail } });
      if (userEmail === null) {
        res.status(401).send({
              message: "Email doesn't exist!"
          });

      } else {

          const user = await User.findOne({ where: { Password: pass } });

          if (user.Password == pass) {
            res.json({
              message: "Signed in!",
              ID: user.ID
          })
          } else {
            res.status(401).send({
              message: "Wrong password provided."
          });
          }
      }

  })


};
