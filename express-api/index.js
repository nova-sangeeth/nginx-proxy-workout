const express = require("express");
const app = express();
const port = 3000;
const host = "0.0.0.0";

app.get(
  "/express-api", (req, res) => 
  res.send(
    `<html>
      <body>
        <center>
          <h1>Express App works on port ${port}</h1>
          <h1>Request host name: ${req.hostname}</h1>
        </center>
      </body>
    </html>`
    )
  );


app.listen(port, host, () =>
  console.log(`Example app listening at http://${host}:${port}`)
);
