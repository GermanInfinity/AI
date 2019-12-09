

//app.js



// // Create an instance of the http server to handle HTTP requests
// let app = http.createServer((req, res) => {
//     // Set a response type of plain text for the response
//     res.writeHead(200, {'Content-Type': 'text/plain'});

//     // Send back a response and end the connection
//     var html = fs.readFileSync('./psycheAI.html');
//     res.write(html);

//     const SpeechToTextV1 = require('ibm-watson/speech-to-text/v1');
//     const { IamAuthenticator } = require('ibm-watson/auth');
//     console.log("hello")

// });

// // Start the server on port 3000
// app.listen(3000, '127.0.0.1');
// console.log('Node server running on port 3000');


const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();

router.get('/', function(req, res){
	res.sendFile(path.join(__dirname+'/psycheAI.html'));

});

app.use(express.static('./'))
app.use('/', router);
app.listen(process.env.port || 3000);
console.log('Node server running on port 3000');