import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log("Error"));
client.on('connect', ()=> console.log('Success'));
