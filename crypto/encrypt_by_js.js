var fs = require('fs');
var NodeRSA = require('node-rsa');

var secret = 'hello';
var pubkey = fs.readFileSync('./pubkey.pem');
pubkey = NodeRSA(pubkey, {encryptionScheme: 'pkcs1'});
var encrypted = pubkey.encrypt(secret, 'base64');
console.log(encrypted);

var privkey = fs.readFileSync('./privkey.pem');
privkey = NodeRSA(privkey, {encryptionScheme: 'pkcs1'});
var decrypted = privkey.decrypt(encrypted, 'utf8');
console.log(decrypted, decrypted === secret);
