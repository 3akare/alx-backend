import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

client.connect();

async function setNewSchool () {
  const fields = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
  const values = [50, 80, 20, 20, 40, 2];
  let i = 0;

  for (i = 0; i < fields.length; i++) {
    await client.HSET('HolbertonSchools', fields[i], values[i]);
    console.log('Reply:', 1);
  }
}

async function displaySchoolValue () {
  const output = await client.HGETALL('HolbertonSchools');
  const keys = Object.keys(output);
  const values = Object.values(output);

  console.log('{');
  for (let i = 0; i < keys.length; i++) {
    console.log('  ', keys[i], ': ', values[i], ',');
  }
  console.log('}');
}

async function main () {
  try {
    await setNewSchool();
    await displaySchoolValue();
  } catch (error) {
    displaySchoolValue();
  }
}

main();
