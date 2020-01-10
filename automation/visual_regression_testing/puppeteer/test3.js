const puppeteer = require('puppeteer');

var url = 'https://www.agari.com/demo/';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto(url);

  await page.type('#FirstName', 'Tester');

  var selector = '#FirstName';
  var text = await page.evaluate(
    selector => document.querySelector(selector).value,
    selector
  );

  console.log(text);

  await browser.close();
})();
