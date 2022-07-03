const express = require("express");
const app = express();
const port = 3000;
const host = "0.0.0.0";

app.get("/", (req, res) =>
  res.send(
    `<html>
      <body>
        <center>
          <h1>Express App works on host and port ${host}:${port}</h1>
          <h1>Express App works on request with hostname ${req.hostname}</h1>
          <h1>Express App works on request with headers ${req.headers}</h1>
        </center>
      </body>
    </html>`
  )
);

app.listen(port, host, () =>
  console.log(`Example app listening at http://${host}:${port}`)
);
