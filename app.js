const express = require('express');

const app = express();
const port = 3000;
let data = '[0,0,0]';

app.get('/get', (req, res) => {
  res.send(data);
});

app.get('/set', (req, res) => {
  if (req && req.query) {
    data = req.query.data
  }
  console.log(data)
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
});
