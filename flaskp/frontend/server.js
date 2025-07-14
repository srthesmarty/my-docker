const express = require('express');
const axios = require('axios');
const app = express();

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get('/', (req, res) => {
  res.render('form');
});

app.post('/submit', async (req, res) => {
  try {
    const response = await axios.post('http://backend:5000/submit', req.body);
    res.send(response.data);
  } catch (err) {
    res.status(500).send("Error sending data to Flask backend.");
  }
});

app.listen(3000, () => {
  console.log('Frontend running on http://localhost:3000');
});

