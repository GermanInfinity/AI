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

//User and Rating 
db.User.hasMany(db.Rating, {as: "Rating", foreignKey: "key",});
db.Rating.belongsTo(db.User, {foreignKey: "key", as: "User",});

//User and Skill
db.User.hasMany(db.Skill, {as: "Skill", foreignKey: "key",});
// db.Skill.hasMany(db.User, {foreignKey: "key", as: "User",});

//User and Orders
db.User.hasMany(db.Order, {as: "Order", foreignKey: "key",});


//User and Conversations
db.User.hasMany(db.Conversation, {as: "Conversation", foreignKey: "key",})


//Order and Conversation
// db.Order.belongsTo(db.Conversation, {foreignKey: "key", as: "Conversation",});
db.Conversation.belongsTo(db.Order, {foreignKey: "key", as: "Order",});

//Conversation to Message
db.Conversation.belongsTo(db.Message, {foreignKey: "key", as: "Message",});
db.Message.hasMany(db.Conversation, {foreignKey: "key", as: "Conversation",});

//Images to Order
// db.Image.hasMany(db.Order, {foreignKey: "key", as: "Order",});
db.Order.hasMany(db.Image, {foreignKey: "key", as: "Image",});



//Images to Users
// db.Image.belongsTo(db.User, {foreignKey: "key", as: "User",});
db.User.hasMany(db.Image, {foreignKey: "key", as: "Image",});

module.exports = db; 

