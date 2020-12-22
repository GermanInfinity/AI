const OrderModel = (sequelize, Sequelize) => {
    const {INTEGER, STRING, FLOAT, BOOLEAN, DATE} = Sequelize
    const Order = sequelize.define('Order', {
        OrderId: {type: INTEGER},
        OrderDate: {type: DATE},
        Technician: {type: BOOLEAN},
        Client: {type: BOOLEAN},
        Conversations: {type: STRING},
        OrderDetails: {type: STRING},
        Submission: {type: STRING}, //URL to Image table
        Status: {type: STRING},
    })
    return Order
}

module.exports = OrderModel
