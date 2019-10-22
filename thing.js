const exec = require('child-process-promise').exec;
const jsonfile = require('jsonfile')
const file = 'stuff.json';
// IIFE
// Immediately Invoked Function Expression
(async function () {

  // "load model from database"
  const obj = await jsonfile.readFile(file)
  // "mutate model" NOT SAVED TO DISK YET
  obj.system_capacity = 6;
  // SAVE TO DISK NOW
  await jsonfile.writeFile(file, obj)

  // RUN WITH UPDATED STUFF
  const result = await exec('python3 sam.py')
  console.log(result.stdout)
})();

