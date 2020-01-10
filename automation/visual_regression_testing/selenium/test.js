var driver = require('webdriverio').remote({
    desiredCapabilities: {
        browserName: 'chrome'
    }
});

require('webdrivercss').init(driver, {
    screenWidth: [768, 1400]
});

driver
    .init()
    .url("http://wordpress.com")
    .execute(() => {
        var element = document.getElementById('top-create-website-button');
        element.style.visibility = 'hidden'
    })
    .webdrivercss('Wordpress', [
        {
            name: 'Homepage',
            elem: 'body'
        }
    ])
    .end();
