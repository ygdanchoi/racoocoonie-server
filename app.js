const express = require('express');

const app = express();
const port = 3000;
let data = '[0,0,0]';

app.get('/get', (req, res) => {
  res.send(data);
});

app.get('/set', (req, res) => {
  console.log(query.data)
  data = req.query.data
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
});
