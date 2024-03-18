const mongoose = require('mongoose')
const mongouri ="mongodb+srv://yrmewara:yrmewara1234@yogesh.0wlmpnc.mongodb.net/hostel?retryWrites=true&w=majority&appName=Yogesh"
const connectToMongo =async ()=>{
    mongoose.connect(mongouri,()=>{
     
         console.log('connected to mongose succesfullly')
    })
}
module.exports= connectToMongo;