const puppeteer = require('puppeteer');

// var url = process.argv[2]; // https://www.agari.com/demo/
var url = 'https://www.agari.com/demo/';

// Async Sleep Function
function sleep(s) {
  return new Promise(resolve => setTimeout(resolve, s*1000));
}

(async () => {
  // Get browser page object
  // const browser = await puppeteer.launch({ headless: false });  // if you want to see it in action
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  console.log('[!] Testing: ' + url + ' ...');

  // Go to page
  await page.goto(url, {waitUntil: 'load'});

  // Fill out form
  await page.type('#FirstName', 'Ariel');
  await page.type('#LastName','Ongoco');
  await page.type('#Company','WebEnertia');
  await page.type('#Title','Developer');
  await page.type('#Email','ariel@webenertia.com');
  await page.type('#Phone','1234567890');
  await page.select('select#Employee_Size_Range__c', '1-6000');
  await page.select('select#Country', 'United States');
  await sleep(1);  // wait for state input to pop up (otherwise, form will be able to submit without it popping up)
  await page.select('select#State', 'CA');  // TODO: Wait for CSS Selector

  // Submit form
  await page.click('.mktoButton');
  await sleep(1);

  // Report current URL
  console.log('[!] Resulting URL: ' + page.url());

  // Takes screenshot
  await page.screenshot({ path: 'result.png' });

  // Check URL
  if (page.url() === url) {
    console.log('[-] Form was NOT submitted successfully.');
  } else if (page.url() === 'https://www.agari.com/thank-you/') {  // condition to tell whether form was submitted or not
  console.log('[+] Form submitted successfully!');
}

// Close browser
  await browser.close();
})();

// TODO: Use Promise.race
// TODO: Move to dependencies
// TODO: Function for testing URL
