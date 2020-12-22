const SkillModel = (sequelize, Sequelize) => {
    const {INTEGER, STRING, FLOAT, BOOLEAN, DATE} = Sequelize
    const Skill = sequelize.define('Skill', {
        SkillID: {type: INTEGER},
        Name: {type: STRING},
        Technician: {type: STRING},

    })
    return Skill
}

module.exports = SkillModel
