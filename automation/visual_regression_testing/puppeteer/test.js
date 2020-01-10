const puppeteer = require('puppeteer');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  page.setViewport({ width: 1400, height: 768 });
  await page.goto('https://www.sandhillglobaladvisors.com/');

  await sleep(2000);

  await page.screenshot({path: 'example.png'});
  await browser.close();
})();
