const path = require('path');
const os = require('os');
const fs = require('fs');
const http = require('http');

var pathObj = path.parse(__filename);
// console.log(pathObj);
var totalMemory = os.totalmem()
var freeMemory = os.freemem()
// console.log(`totalMemory ${totalMemory}`)
// console.log(`freeMemory ${freeMemory}`)
// fs.readdir('./', function(err, files) {
//     if (err) console.log('Error', err);
//     else console.log('Result', files);
// })

const Logger = require('./logger');
const logger = new Logger();

// Register a listener
logger.on('messageLogged', (arg) => {
    console.log('Listener called', arg);
});

logger.log('message');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.write('Hello world');
        res.end();
    }

    if (req.url === '/api/courses') {
        res.write(JSON.stringify([1, 2, 3]));
        res.end();
    }
});

// server.on('connection', (socket) => {
//     console.log('New connection...');
// });

server.listen(3000);

console.log('Listen on port 3000...');
