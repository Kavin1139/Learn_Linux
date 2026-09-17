const express = require('express')

const expr = express();

expr.get('/', (req, res) => {
	res.send("Hello world from express");
});

expr.listen(3000);
