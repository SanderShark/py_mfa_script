const fs = require('fs');
const sqlite3 = require('sqlite3').verbose();

// Connect to the SQLite database
const db = new sqlite3.Database('your_database.db');

// Prompt the user to enter the MFA code
const user_input = prompt("Enter your MFA code: ");

// Read the JSON data from a file
const mfa_json = fs.readFileSync("mfa.json", "utf8");

// Parse the JSON data
const mfa_data = JSON.parse(mfa_json);

// Retrieve the email and code from the JSON data
const email = mfa_data.email;
const code = mfa_data.code;

// Check the user input against the stored code in the database
db.get("SELECT email FROM users WHERE email = ? AND code = ?", [email, user_input], (err, row) => {
  if (row) {
    console.log("Authentication successful!");
    // Proceed with further actions after successful authentication
  } else {
    console.log("Authentication failed. Invalid MFA code.");
  }
});

// Close the database connection
db.close();
