const MongoClient = require("mongodb").MongoClient;

const url = "mongodb://localhost:27017";
const mydbname = "spotify";

async function connectToDatabase() {
  try {
    const client = await MongoClient.connect(url);
    const db = client.db(mydbname);
    return db;
  } catch (err) {
    console.error('Error connecting to MongoDB:', err);
    throw err;
  }
}

module.exports = {connectToDatabase}