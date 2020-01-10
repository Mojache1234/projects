// const puppeteer = require('puppeteer');
import puppeteer from 'puppeteer';

var sleep = function (s) {
  return new Promise(resolve => setTimeout(resolve, s * 1000));
}

function opt(options, key) {
  return (options && options[key]) ? options[key] : false;
}

// function to start test
async function start(options) {

  // set parameters
  var url = options.url;
  var submitButton = options.submitButton;
  var form = options.form;
  var formWait = opt(options, 'formWait');

  // set up browser
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // try-catch all unhandled promise errors
  try {
    await page.goto(url, { waitUntil: 'load' });

    // report what's being tested
    console.log('[!] Testing: ' + url + ' ...');

    // loop through form items
    for (var x in form) {
      // TODO: turn this into a function maybe?
      if (/^select/.test(x)) {
        await page.select(x, form[x]);
      } else {
        await page.type(x, form[x]);
      }
    }

    // loop through async form items if any
    if (formWait) {
      // await sleep(1);
      for (var x in formWait) {
        var selector = (x.indexOf('#') == 6) ? '#' + x.split('#')[1] : x;

        // wait for it to either appear or after 1 second
        await Promise.race([
          page.waitForSelector(selector),
          sleep(10)
        ]);

        if (/^select#.*/.test(x)) {
          await page.select(x, formWait[x]);
        } else {
          await page.type(x, formWait[x]);
        }
      }
    }

    // submit form
    await page.click(submitButton)
    await Promise.race([
      page.waitForNavigation(),
      sleep(5)
    ]);

    // report current url
    console.log('[!] Resulting URL: ' + page.url());

    // take screenshot
    await page.screenshot({ path: 'result.png' });

    // Check URL
    if (page.url() === url) {
      console.log('[-] Form was NOT submitted successfully.');
    } else if (page.url() === 'https://www.agari.com/thank-you/') {
      console.log('[+] Form submitted successfully!');
    }

    // close browser
    await browser.close();
  } catch (err) {
    // report error and close browser
    console.log(err);
    await browser.close();
  }
}

// export all functions
module.exports = {
  sleep: sleep,
  start: start
}
