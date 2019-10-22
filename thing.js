const exec = require('child-process-promise').exec;
const jsonfile = require('jsonfile')
const file = 'stuff.json';
const fs = require('fs')
// pretend this is a library that takes an object and saves to csv
const csvThingy = () => { }
const axios = { get: () => ({ data: [] }) };
/*
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
*/
// PRETEND THIS IS A ROUTE
(async function (req, res, next) {
  // pull load data from api using axios
  const { data: load } = await axios.get('http://YOUR API THING GOES HERE')
  // PRETEND THIS IS DONE
  // save in /tmp/latitude,longitude.csv
  const loadCSVFilename = `/tmp/${req.body.latitude},${req.body.longitude}.csv`
  await csvThingy(loadCSVFilename, load)
  // normalize any req.body params
  // prevent people from requesting stupid stuff
  const params = {
    system_capacity: 50,
    ...req.body
  }
  if (params.system_capacity > 30) {
    params.system_capacity = 30
  }

  // generate arg string USE A LIBRARY TO GEN SAFELY
  // prevents hackers from pwning you
  // don't do it this way, I'm just showing quick how to
  // I need to call a script on node, and need to pass it parameters
  // what is a safe way to do that without people running arbitrary code on my shell
  const args = Object.keys(params).map(key =>
    // use a tool to escape quotes when you do params[key]
    // idk a good tool
    `--${key} "${params[key]}"`
  ).join(' ')
  try {
    // run exec on data
    const result = await exec(`python3 sam.py ${args}`)

    // parse relevant data
    // format info
    const data = parseData(result.stdout)

    // send info
    res.json(data)

    // delete csv file to save space
    // BE CAREFUL WITH THIS LINE
    // IT REMOVES A FILE
    // fs.unlink(loadCSVFilename)
  } catch (err) {
    // catch any errors from the exec and onward
    console.log(err)
  }
  // ignore the following lines, THEY DO NOTHING other than mock the above route
})({ body: {} }, { json: (d) => { console.log(`U R JSONING,`, d) } }, () => { })

// don't do it this way, but it's ok for now. bugs are easy to come up here
// instead, have the python return JSON formatted data (look at the bottom of sam.py)
const parseData = data => {
  const lines = data.split('\n')
  const startsWith = prefix => word => word.startsWith(prefix)
  return {
    annualEnergy: lines.find(startsWith('Annual energy ')).slice(26)
  }
}
