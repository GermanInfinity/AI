const ConversationModel = (sequelize, Sequelize) => {
    const {INTEGER, STRING, FLOAT, BOOLEAN, DATE} = Sequelize
    const Conversation = sequelize.define('Conversation', {
        ConversationId: {type: INTEGER},
        Messages: {type: STRING},
        Initiator: {type: STRING},
        Participant: {type: STRING},
        OrderId: {type: INTEGER},
        
    })
    return Conversation
}

module.exports = ConversationModel
