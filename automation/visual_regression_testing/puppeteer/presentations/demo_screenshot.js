const puppeteer = require('puppeteer');

// Get command-line arguments
// var url = process.argv[2]; // https://www.sandhillglobaladvisors.com/
var url = 'https://www.sandhillglobaladvisors.com/'
// var waitTime = process.argv[3];
var waitTime = 2;

// Create Promise for sleep
function sleep(s) {
  return new Promise(resolve => setTimeout(resolve, s*1000));
}

// Anonymous async function
(async () => {
  // Get browser page object
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto(url);

  // Set viewport and go to URL
  var totalHeight = await page.evaluate(() => {
    return Math.max(
        document.body.parentNode.scrollHeight,
        document.body.parentNode.offsetHeight,
        document.documentElement.clientHeight,
        document.documentElement.scrollHeight,
        document.documentElement.offsetHeight
      );
    });

    console.log(totalHeight);
    await page.setViewport({ width: 1400, height: totalHeight });

  // Wait for page to load for specified seconds
  await sleep(waitTime);

  // Take screenshot and create file called example.png
  await page.screenshot({ path: 'example.png' });

  // Close browser
  await browser.close();
})();
