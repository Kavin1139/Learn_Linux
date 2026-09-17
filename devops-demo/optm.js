const express = require('express');
const dotenv = require('dotenv');

const env = process.argv[2] || "development";
dotenv.config ({ path: `.env.${env}` });

const expr = express();

const PORT = process.env.PORT;
const APP = process.env.APP;

expr.get('/', (req, res) => {
        res.send("Hello world from express" + APP);
});

expr.listen(PORT , () => {
	console.log('Server is running on port' + PORT)
});



