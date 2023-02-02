const fs = require("fs");

fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data.trim().split("\n"));
  var y = 0;
  for (var x in data.trim().split("\n")) {
    y += x;
    console.log(y);
  }
  console.log(y);
});
