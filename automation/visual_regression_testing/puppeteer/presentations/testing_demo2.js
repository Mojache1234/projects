try {
  var puppeteer = require('puppeteer');
} catch (err) {
  console.log('This module requires "puppeteer". Please install using the following:\n\n\tnpm install -g puppeteer');
}

class FormTest {

  // run test
  run(url, runFunction) {
    this.url = url;

    (async () => {

      // set up browser
      const browser = await puppeteer.launch();
      const page = await browser.newPage();
      this.browser = browser;
      this.page = page;
      await this.page.goto(this.url, { waitUntil: 'load' });

      // try-catch block to catch unhanled promises
      try {

        // run function by passing object context
        var result = await runFunction.bind(this)();

      } catch (err) {
        console.log(err);
      }

      // clean up browser
      await this.close();

      // return result to terminal
      console.log(result);
    })();
  }

  /* utility functions */

  // asynchronous sleep utility
  sleep(s) {
    return new Promise(resolve => setTimeout(resolve, s*1000));
  }

  // private optional parameter parser utility
  _opt(options, key) {
    return (options && options[key]) ? options[key] : '';
  }

  // fills form given dictionary
  async fillForm(data) {
    for (var selector in data) {
      try {
        // wait for it to either appear or after 1 second
        await Promise.race([
          this.page.waitForSelector(selector),
          this.sleep(5)
        ]);

        // sense type of input and fill form accordingly
        var tag = await this.page.evaluate(
          selector => document.querySelector(selector).tagName, selector
        );

        if (tag === 'SELECT') {
          await this.page.select(selector, data[selector]);
        } else if (tag === 'INPUT') {
          await this.page.type(selector, data[selector]);
        }

        // check if form was filled out properly
        var value = await this.getValue(selector);
        if (value != data[selector]) {
          console.warn('[!] ' + selector + ' expected to be "' + data[selector] + '" but is "' + value + '" instead.');
        }
      } catch (err) {
        console.warn('[!] Error on selector: ' + selector);
        console.warn(err);
        return false;
      }
    }
  }

  // submit form as it is and take a screenshot
  async submit(submitButton, options) {
    var path = this._opt(path, options);
    await this.page.click(submitButton);

    // if submit is given a path, take screenshot of resulting page
    if (path) {
      await this.page.screenshot({ path: path });
    }
  }

  // close browser
  async close() {
    await this.browser.close();
  }

/* getter functions */

  // get value for given selector
  async getValue(selector) {
    try {
      // check if selector exists on page
      await Promise.race([
        this.page.waitForSelector(selector),
        this.sleep(2)
      ]);

      // check if value is valid, if not use textContent
      return await this.page.evaluate(
        selector => {
          var query = document.querySelector(selector);
          return (query.value) ? query.value : query.textContent;
        }, selector);
    } catch (err) {
      console.warn('[!] Error on selector: ' + selector);
      console.warn(err);
      return false;
    }
  }

  // get values for given selectors
  async getValues(selectors) {
    var response = {};
    var promises = [];
    for (var x in selectors) {
      var selector = selectors[x];
      try {
        // check if selector exists on page
        await Promise.race([
          this.page.waitForSelector(selector),
          this.sleep(2)
        ]);

        // get value
        var text = await this.page.evaluate(
          selector => {
            var query = document.querySelector(selector);
            return (query.value) ? query.value : query.textContent;
          }, selector
        );

        promises.push(text);
        response[selector] = text;
      } catch (err) {
        console.warn('[!] Error on selector ' + selector);
        console.warn(err);
        return false;
      }
    }
    await Promise.all(promises);
    return response;
  }

  /* validation functions */

  // check if current url equals given url
  async checkUrl(url) {
    await this.sleep(2); // wait 2 seconds just in case
    var actual = await this.page.url();
    return (actual == url);
  }

  // checks if value of selector matches given value
  async checkValue(selector, value) {
    return await this.getValue(selector) == value;
  }

  // checks multiple values
  async checkValues(data) {
    for (var selector in data) {
      var content = await this.getValue(selector);
      if (content != data[selector]) {
        console.warn('[!] ' + selector + ' expected to be "' + data[selector] + '" but is "' + content + '" instead.');
        return false;
      }
    }
    return true;
  }
}

module.exports = { FormTest };
