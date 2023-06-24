const express = require("express")
const collection = require("./mongo")
const cors = require("cors")
const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(cors())



app.get("/",cors(),(req,res)=>{

})


app.post("/",async(req,res)=>{
    const{email,password}=req.body

    try{
        const check=await collection.findOne({email:email})

        if(check){
            res.json("exist")
        }
        else{
            res.json("notexist")
        }

    }
    catch(e){
        res.json("fail")
    }

})



app.post("/signup",async(req,res)=>{
    
    const{email,password,name}=req.body
    const inter=[]
    const al=[]
    const data={
        name:name,
        email:email,
        password:password,
        interests:inter,
        already:al
    }

    try{
        const check=await collection.findOne({email:email})

        if(check){
            res.json("exist")
        }
        else{
            res.json("notexist")
            await collection.insertMany([data])
        }

    }
    catch(e){
        res.json("fail")
    }

})

app.post("/interests",async (req,res) => {
    
    const inter=req.body.selectedCheckboxes
    const email=req.body.email
    const le=Object.keys(inter).length
    const arr=[]
    for(let i = 0; i < le; i++)
    {
        arr.push(inter[i])
    }
    try{
        // const check=await collection.findOne({mail:mail})
        await collection.updateOne({email:email},{interests:[]})
        await collection.updateOne({email:email},{ $push: { interests: { $each: arr } } })
        
    }
    catch(e){
        console.log(e)
    }
    console.log("done")
})

app.listen(3000,()=>{
    console.log("port connected");
})

