import express from "express";
import cors from 'cors'
import dotenv from 'dotenv'
import axios from "axios";

dotenv.config();

const app=express();

app.use(express.json());
app.use(express.urlencoded({extended:true}));

app.get(`/predict/:input`, async (req, res) => {
    try {
        const response = await axios.post(`${process.env.PYTHON_URL}/predict/${req.params.input}`);
        res.json(response.data); 
    } catch (error) {
        console.log(error.message);
        res.status(500).send("Error connecting to Python server");
    }
});

app.listen(3000);