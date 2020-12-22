const ImageModel = (sequelize, Sequelize) => {
    const {INTEGER, STRING, FLOAT, BOOLEAN, DATE} = Sequelize
    const Image = sequelize.define('Image', {
        ImageiD: {type: INTEGER},
        Name: {type: STRING},
        URL: {type: STRING},

    })
    return Image
}

module.exports = ImageModel

