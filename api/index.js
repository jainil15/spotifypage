const express = require("express");
const { connectToDatabase } = require("./db.js");
const cors = require("cors");
const portNo = 8800;
const app = express();
app.use(express.json());
app.use(cors());

app.get("/api/top50", async (req, res) => {
  try {
    const db = await connectToDatabase();
    const collection = db.collection("spotify_scrapped");
    const result = await collection.find({}).toArray();
    return res.status(200).json(result);
  } catch (err) {
    console.log(err);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

app.get("/api/track/:id", async (req, res) => {
  try {
    const db = await connectToDatabase();
    const collection = db.collection("spotify_scrapped");
    const track_id = req.params.id;
    const result = await collection.find({ song_href: `/track/${track_id}` }).toArray();
    return res.status(200).json(result);
  } catch (error) {
    console.log(error);
    return res.status(500).json({ error: "Internal Server error" });
  }
});

app.listen(portNo, () => {
  console.log("LISTENING TO 8800");
});
