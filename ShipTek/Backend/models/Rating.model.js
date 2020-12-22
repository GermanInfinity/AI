const RatingModel = (sequelize, Sequelize) => {
    const {INTEGER, STRING, FLOAT, BOOLEAN, DATE} = Sequelize
    const Rating = sequelize.define('Rating', {
        RatingId: {type: INTEGER},
        UserID: {type: INTEGER},
        OrderId: {type: INTEGER},
        RatingValue: {type: BOOLEAN},
        RatingComment: {type: STRING},

    })
    return Rating
}

module.exports = RatingModel
