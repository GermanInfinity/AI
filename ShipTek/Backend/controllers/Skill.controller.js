const db = require("../models");
const Skill = db.Skill;
const User = db.User;


// CREATE AND SAVE SKILL 
exports.create = (Skill) => {
  return Skill.create({
    title: Skill.title,
    description: Skill.description,
  })
    .then((Skill) => {
      console.log(">> Created Skill: " + JSON.stringify(Skill, null, 4));
      return Skill;
    })
    .catch((err) => {
      console.log(">> Error while creating Skill: ", err);
    });
};

// RETRIEVE ALL SKILLS
exports.findAll = () => {
  return SkillfindAll({
    include: [
      {
        model: User,
        as: "User",
        attributes: ["id", "name"],
        through: {
          attributes: [],
        },
        // through: {
        //   attributes: ["tag_id", "Skill_id"],
        // },
      },
    ],
  })
    .then((Skills) => {
      return Skill;
    })
    .catch((err) => {
      console.log(">> Error while retrieving Skill: ", err);
    });
};

// GET SKILL FOR A GIVEN SKILL ID 
exports.findById = (id) => {
  return Skill.findByPk(id, {
    include: [
      {
        model: User,
        as: "User",
        attributes: ["id", "name"],
        through: {
          attributes: [],
        },
        // through: {
        //   attributes: ["tag_id", "Skill_id"],
        // },
      },
    ],
  })
    .then((Skill) => {
      return Skill;
    })
    .catch((err) => {
      console.log(">> Error while finding Skill: ", err);
    });
};
