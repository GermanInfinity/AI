
const UserModel = (sequelize, Sequelize) => {

    const {INTEGER, STRING, FLOAT, BOOLEAN, DATE} = Sequelize
    const User = sequelize.define('User', {
        Username: {type: STRING},
        Email: {type: STRING},
        Password: {type: STRING},
        IsTech: {type: INTEGER},
        Images: {type: STRING},
        Ratings: {type: INTEGER},
        Skills: {type: STRING},
        SelfDescription: {type: STRING},
        Orders: {type: STRING},
        CurrLocation: {type: STRING},
        Address: {type: STRING},
        Conversations: {type: STRING},
    })
    return User
}

module.exports = UserModel

