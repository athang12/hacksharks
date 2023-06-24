const mongoose=require("mongoose")
mongoose.connect("mongodb+srv://weekenddiscoveries6:V62ejRjlVilThUGv@cluster0.dhpp5yh.mongodb.net/")
.then(()=>{
    console.log("mongodb connected");
})
.catch(()=>{
    console.log('failed');
})


const newSchema=new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    email:{
        type:String,
        required:true
    },
    password:{
        type:String,
        required:true
    },
    interests:{
        type:Array,
        required:false
    },
    already:{
        type:Array,
        required:false
    },
    tosend:{
        type:Array,
        required:false
    }
})

const collection = mongoose.model("collection",newSchema)

module.exports=collection
