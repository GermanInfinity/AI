const SuggestionModel = (sequelize, Sequelize) => {
    const {INTEGER, STRING, FLOAT, BOOLEAN, DATE} = Sequelize
    const Suggestion = sequelize.define('Suggestion', {
        UserName: {type: INTEGER},
        Suggestion: {type: STRING},
        
    })
    return Suggestion
}

module.exports = SuggestionModel
