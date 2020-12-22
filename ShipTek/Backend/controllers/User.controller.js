const Distance = require("../models/GetDistance.js")
const db = require("../models");
const Skill = db.Skill;
const User = db.User;
const Suggestion = db.Suggestion;
var router = require("express").Router();



//CREATE 
exports.create = (User) => {
  return User.create({
    name: User.name,
  })
    .then((User) => {
      console.log(">> Created User: " + JSON.stringify(User, null, 2));
      return User;
    })
    .catch((err) => {
      console.log(">> Error while creating User: ", err);
    });
};



/** SIGN UP **/ 
exports.create = async (NewUser) => { 

  User.count({ where: {username: NewUser.username}})
    .then(count => {

      if (count != 0) {
      	res.status(403).send({
        	message: "Username already exists!"
        });
        return; 
      }


      User.count({ where: {email: NewUser.email}})
          .then(count => {
            if (count != 0) {
            res.status(403).send({
        		message: "Email already exists!"
        	});
              return true;
            }
        
        if (NewUser.tech == 1) {
            User.create({ Username: NewUser.username,
                    Email: NewUser.email, 
                    Password: NewUser.password,
                    IsTech: NewUser.tech,
                    Skills: NewUser.skills,
                    SelfDescription: NewUser.selfDescription,
                    Address: NewUser.address});

           return true; 
        }
        User.create({ Username: NewUser.username,
                    Email: NewUser.email, 
                    Password: NewUser.password,
                    IsTech: NewUser.tech});

      });
  });
}



/** SIGN IN **/ 
exports.signIn = async (UserInfo) => { 
  const userEmail = await User.findOne({ where: { Email: UserInfo.email } });
	if (userEmail === null) {
	  res.status(401).send({
        	message: "Email doesn't exist!"
      });

	} else {

      const user = await User.findOne({ where: { Password: UserInfo.password } });

  	  if (user.Password == UserInfo.password) {
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
 
}

/** HOME **/
exports.dashboard = async (Input) => { 
  /// Use ID instead
  const user = await User.findOne({ where: { Email: "evans@gmail.com"} });
  res.json({ Username: user.Username });
}

/** SUGGESTIONS **/ 
exports.suggestons = async (Input) => { 
  Suggestion.create({ UserName: Input.username, Suggestions: Input.suggestions});
  // return success message. 
}


/** FIND TECHNICIAN **/ 
exports.find = async (Input) => { 
  const technicians = await User.findAll({ where: {isTech: 1}});
  console.log("All techs:", JSON.stringify(technicians, null, 2));

  // A lot of JavaScript here to get closest distance with API. 
  // Then rank smaller list. 

  
  // const location = Input.userLocation;
  // // make an API call to google maps
  // for (i = 0; i < technicians.size; i++) {
  //   data = Distance.getDistance(location, technicians[i].currLocation);
  // }
}

// FIND
exports.findAll = () => {
  return User.findAll({
    include: [
      {
        model: User,
        as: "User",
        attributes: ["id", "title", "description"],
        through: {
          attributes: [],
        }
      },
    ],
  })
    .then((User) => {
      return User;
    })
    .catch((err) => {
      console.log(">> Error while retrieving Users: ", err);
    });
};

// //FIND WITH GIVEN ID 
// exports.findById = (id) => {
//   return User.findByPk(id, {
//     include: [
//       {
//         model:User,
//         as: "Skill",
//         attributes: ["id", "title", "description"],
//         through: {
//           attributes: [],
//         }
//       },
//     ],
//   })
//     .then((User) => {
//       return User;
//     })
//     .catch((err) => {
//       console.log(">> Error while finding User: ", err);
//     });
// };





// ADD A SKILL TO A USER 
exports.addSkill = (UserId, SkillId) => {
  return User.findByPk(UserId)
    .then((User) => {
      if (!User) {
        console.log("User not found!");
        return null;
      }
      return Skill.findByPk(SkillId).then((Skill) => {
        if (!Skill) {
          console.log("Skill not found!");
          return null;
        }

        User.addSkill(Skill);
        console.log(`>> added Skill id=${Skill.id} to User id=${User.id}`);
        return User;
      });
    })
    .catch((err) => {
      console.log(">> Error while adding Skill to User: ", err);
    });
};
