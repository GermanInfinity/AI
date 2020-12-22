const config = require("../config/db.config.js");

const Sequelize = require("sequelize");
const sequelize = new Sequelize(config.DB, config.USER, config.PASSWORD, {
  host: config.HOST,
  dialect: config.dialect,
  operatorsAliases: false,

  pool: {
    max: config.pool.max,
    min: config.pool.min,
    acquire: config.pool.acquire,
    idle: config.pool.idle,
  },
});

const db = {};

db.Sequelize = Sequelize;
db.sequelize = sequelize;

db.User = require("./User.model.js")(sequelize, Sequelize);
db.Image = require("./Image.model.js")(sequelize, Sequelize);
db.Conversation = require("./Conversation.model.js")(sequelize, Sequelize);
db.Message= require("./Message.model.js")(sequelize, Sequelize);
db.Order = require("./Order.model.js")(sequelize, Sequelize);
db.Rating = require("./Rating.model.js")(sequelize, Sequelize);
db.Skill = require("./Skill.model.js")(sequelize, Sequelize);

// db.Skill.belongsToMany(db.User, {through: "central_tag", as: "tutorials", 
//                                  foreignKey: "tag_id",});
// db.User.belongsToMany(db.Skill, {through: "central_tag", as: "tutorials", 
//                                  foreignKey: "tag_id",});
module.exports = db; 

