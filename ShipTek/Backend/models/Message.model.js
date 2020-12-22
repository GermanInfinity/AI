const MessageModel = (sequelize, Sequelize) => {
    const {INTEGER, STRING, FLOAT, BOOLEAN, DATE} = Sequelize
    const Message = sequelize.define('Message', {
        UserId: {type: INTEGER},
        Username: {type: STRING},
        Email: {type: STRING},
        Password: {type: STRING},
        IsTech: {type: BOOLEAN},
        Images: {type: STRING},
        Ratings: {type: INTEGER},
        Skills: {type: STRING},
        Orders: {type: STRING},
        Conversations: {type: STRING},
    })
    return Message
}

module.exports = MessageModel