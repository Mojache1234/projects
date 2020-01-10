// Initiate global variables
var sheet = SpreadsheetApp.getActiveSpreadsheet();

// Add Menu Item(s)
function doOpen() {
  var ui = SpreadsheetApp.getUi();

  ui.createMenu('GA Test')
  .addItem('Run Test', 'runTestWithNotify')
  .addItem('Schedule Run on Tuesdays', 'setAutoDate')
  .addItem('Cancel All Scheduled Runs', 'removeAutoDates')
  .addToUi();
}

function runTestWithNotify() {
  var ui = SpreadsheetApp.getUi();

  // Notify User on Open
  ui.alert('You are about to run the script. This may take a while. Please press OK.');

  // Run Test
  try {
    runTest();
  } catch (err) {
    // Log Errors and Alerts User
    ui.alert(err);
    Logger.log(err);
  }

  // Notify user when done
  ui.alert('Done!');
}

// Generates Google Analytics Test Report
function runTest() {

  // Set Sheet Ranges and Formatting
  var summary = Analytics.Management.AccountSummaries.list()['items'];
  sheet.getRange('A1:F1')
  .setValues([['Main Name', 'Profile Name', 'ID', 'Website URL', 'Has Google Analytics', 'Skip']])
  .setFontWeights([['bold', 'bold', 'bold', 'bold', 'bold', 'bold']]);
  var content = sheet.getRange('A2:F2000');

  // Associate Skips with URLs
  var urlsToSkip = skipUrls();

  // Clear Content Range to Reset
  content.clear();

  // Get Data
  var row = 1;
  for (var i = 0; i < summary.length; i++) {

    var properties = summary[i]['webProperties'];

    if (properties) {
      for (var j = 0; j < properties.length; j++) {

        // Set Main Name
        var name = properties[j]['name'];
        var profiles = properties[j]['profiles'];

        content.getCell(row, 1).setValue(name);

        for (var k = 0; k < profiles.length; k++) {

          // Set Profile Name and ID
          var name = profiles[k].name;
          var id = profiles[k].id;

          // Set Metrics
          var metrics = 'ga:pageviews';
          var dimensions = 'ga:hostname';

          content.getCell(row, 2).setValue(name);
          content.getCell(row, 3).setValue(id);

          // Get data from GA
          var data = Analytics.Data.Ga.get('ga:' + id, 'yesterday', 'today', metrics, { 'dimensions': dimensions })['rows'];

          if (data) {
            for (var r = 0; r < data.length; r++){
              var dataRow = data[r];
              var url = dataRow[0];

              // Check If URL Should Be Skipped
              if (urlsToSkip.indexOf(url) > -1 || !/^(www\.)/.test(url)) continue;

              content.getCell(row, 4).setValue(url);

              // Check if URL has captured traffic (traffic > 0)
              content.getCell(row, 5)
              .setValue(dataRow[1] > 0 ? 'YES' : 'NO')
              .setBackground(dataRow[1] > 0 ? '#90ee90' : '#ff9999');
              Logger.log(url + ': ' + dataRow[1]);

              content.getCell(row, 6).setValue('NO');
              row++;
            }
          }
        }
      }
    }
  }
}

// Associate Skips with URLs
function skipUrls() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();

  var toSkip = sheet.getRange('F2:F500').getValues();
  var urls = sheet.getRange('D2:D500').getValues();
  var skipsRange = sheet.getSheetByName('Skip').getRange('A1:A1000');

  // Find Skipped URL's First Empty Cell
  var row = function (range) {
    var rowCount = 1;
    if (range) for (var i = 0; i < range.getValues().length; i++) {
      if (range.getValues()[i][0] != '') rowCount++;
    }
    return rowCount;
  }(skipsRange);

  // Put Marked Url's In Skipped URLs
  if (urls.length && toSkip.length) {
    for (var i = 0; i < toSkip.length; i++) {
      if (toSkip[i][0] == 'YES') {
        // Write To Skipped URL's
        skipsRange.getCell(row++, 1).setValue(urls[i][0]);
      }
    }
  }

  // Get New List of URLs to Skip
  var urlsToSkip = skipsRange.getValues()
  .map(function(url) {
    return url[0]
  })
  .filter(function(url) {
    return url != '';
  });

  return urlsToSkip;
}

// Email Alerts
function emailAlert() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();

  // Get Date Today
  var date = new Date();
  var today = Utilities.formatDate(date, 'PST', 'MMM dd, yyyy');

  // Email to Each Email Listed in the "Email List" Sheet
  var emails = sheet.getSheetByName('Email List').getRange('A1:A100').getValues();
  for (var i = 0; i < emails.length; i++) {
    var email = emails[i][0];
    if (email) {
      var subject = 'Weekly Google Analytics Test Report - ' + today;
      var message = 'Weekly Google Analytics test report is now ready. Please follow this link: ' + sheet.getUrl();
      try {
        MailApp.sendEmail(email, subject, message);
      } catch (err) {
        // ui.alert(err);
        Logger.log('WARNING: ' + email + ' might not be a valid email. Please remove this from the list.');
      }
    }
  }
}

// Sets Time-Driven Triggers - https://www.benlcollins.com/spreadsheets/time-triggers/
function setAutoDate() {
  var ui = SpreadsheetApp.getUi();

  removeAutoDates();
  // Run Test Every Monday Morning
  ScriptApp.newTrigger('runTest')
  .timeBased()
  .atHour(6)
  .onWeekDay(ScriptApp.WeekDay.TUESDAY)
  .everyWeeks(1)
  .inTimezone("America/Los_Angeles")
  .create();

  // Send Email Every Monday Morning
  ScriptApp.newTrigger('emailAlert')
  .timeBased()
  .atHour(9)
  .onWeekDay(ScriptApp.WeekDay.TUESDAY)
  .everyWeeks(1)
  .inTimezone("America/Los_Angeles")
  .create();

  // Inform User
  ui.alert('Script will now run every week on Tuesdays between 6:00 A.M. and 7:00 A.M. PST.<br />You will get an email on Tuesdays between 8:00 A.M. to 9:00 A.M. PST.');
}

// Removes Time-Driven Triggers
function removeAutoDates() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();

  var triggers = ScriptApp.getUserTriggers(sheet);
  for (var i = 0; i < triggers.length; i++) {
    if (triggers[i].getEventType() == 'CLOCK') {
      ScriptApp.deleteTrigger(triggers[i]);
      Logger.log('Deleted ' + triggers[i].getHandlerFunction() + ' trigger.');
    }
  }
}

// sorts dictionary based on value
function sortValues(values) {
  var values_list = Object.keys(values).map(function(key) {
    return [key, values[key]];
  });

  values_list.sort(function (a, b) { return b[1] - a[1] });

  return values_list;
}

// Get list of retainers email
function getRetainers() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Retainers');
  var emails = [];

  // get list of retainers
  var retainers = sheet.getRange('A1:A100').getValues();
  for (var i = 0; i < retainers.length; i++) {
    if (retainers[i][0].length <= 0) { continue; };
    emails.push(retainers[i][0]);
  }

  return emails;
}

function getDataInUrlList(urlList, options, metrics) {
  var urls_master = {};

  // get summary from GA
  var summary = Analytics.Management.AccountSummaries.list()['items'];
  for (var i = 0; i < summary.length; i++) {
    var properties = summary[i]['webProperties'];

    // if properties, filter using urlList
    if (properties) {
      for (var j = 0; j < properties.length; j++) {
        var property = properties[j];

        var url = (property['websiteUrl'].slice(-1) == '/') ? property['websiteUrl'] : property['websiteUrl'] + '/';

        var profiles = property['profiles'];
        var profiles_master = {};

        // filter using urlList
        if (urlList.indexOf(url) > -1) {
          for (var k = 0; k < profiles.length; k++) {
            var id = profiles[k]['id'];

            // TODO: find way to manage multiple dimenions
            // get data
            var data = Analytics.Data.Ga.get('ga:' + id, '28daysAgo', 'today', metrics, options)['rows'];

            // cycle through data and push row items
            var profile_data = {};

            if (data) {
              for (var r = 0; r < data.length; r++) {
                var dataRow = data[r];
                var dimension = dataRow[0];
                var metric = dataRow[1];

                if (metric > 2) {
                  profile_data[dimension] = metric;
                }
              }
            }
            if (Object.keys(profile_data).length) profiles_master[id] = profile_data;
          }
          if (Object.keys(profiles_master).length) urls_master[url] = profiles_master;
        }
      }
    }
  }
  return urls_master;
}

// Check summary for retainer websites for top 5 slowest pages
function getSpeeds() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Google Analytics Speed Test Report');
  var range = sheet.getRange('A2:D1000');
  range.clear();

  var emails = getRetainers();
  var metrics = "ga:avgPageLoadTime";
  var options = {
    "dimensions": "ga:pagePath",
    "sort": "-ga:avgPageLoadTime",
    "filters": "ga:avgPageLoadTime>2;ga:country==United States;ga:pageLoadSample>2",
    "max-results": 5
  }
  var data = getDataInUrlList(emails, options, metrics);

  if (Object.keys(data).length > 0) {
    var message = "";

    // update sheet
    var row = 1;
    for (var url in data) {
      // message subtitle
      message += '<h2>Page Load Times for URL: ' + url + '</h2>';

      var profiles = data[url];
      for (var profile_id in profiles) {
        var pages = profiles[profile_id];

        message += 'Profile ID: <strong>' + profile_id + '</strong><br /><br />';

        // start table headers
        message += '<table style="border: 1px solid black;"> \
        <thead> \
          <tr> \
            <th style="border: 1px solid black;margin: 0;padding: 2.5px;">Page URL</th> \
            <th style="border: 1px solid black;margin: 0;padding: 2.5px;">Page Load Time</th> \
          </tr> \
        </thead> \
        <tbody>'

        // print out data
        for (var page in pages) {
          var pageSpeed = pages[page];
          var pageLink = '<a href="' + url.substring(0, url.length - 1) + page + '">' + page + '</a>';
          // new table row with data
          message += '<tr><td style="border: 1px solid black;margin: 0;padding: 2.5px;">' + pageLink + '</td><td style="border: 1px solid black;margin: 0;padding: 2.5px;">' + parseFloat(pageSpeed).toFixed(2) + ' seconds</td></tr><br />';

          // write to google sheets
          range.getCell(row, 1).setValue(url);
          range.getCell(row, 2).setValue(profile_id);
          range.getCell(row, 3).setValue(page);
          range.getCell(row, 4).setValue(pageSpeed);

          row++;
        }

        // end table headers
        message += '</tbody></table>'

        message += '<br />';
      }

      message += '<hr /><br /><br />';
    }

    // send email
    email(message);
  }
}

// generic email given a message (pulls from mailing list)
function email(message) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();

  // get date today
  var date = new Date();
  var today = Utilities.formatDate(date, 'PST', 'MMM dd, yyyy');

  // email to each email listed in the "email list" sheet
  var emails = sheet.getSheetByName('Email List').getRange('A1:A100').getValues();
  for (var i = 0; i < emails.length; i++) {
    var email = emails[i][0];
    if (email) {
      var subject = 'Weekly Google Analytics Page Load Time Report - ' + today;
      message += '<br /><br />Please follow this link to view the entire report: ' + sheet.getUrl();

      try {
        // MailApp.sendEmail(email, subject, message);

        MailApp.sendEmail({
          to: email,
          subject: subject,
          htmlBody: message
        });
      } catch (err) {
        Logger.log('WARNING: ' + email + ' might not be a valid email. Please remove this from the list.');
      }
    }
  }
}

// Ariel's Testing Tool
function testFunction() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var metrics = 'ga:pageviews';
  var dimensions = 'ga:hostname';
  var summary = Analytics.Management.AccountSummaries.list()['items'][0];
  var property = summary['webProperties'][0];
  var profile = property['profiles'][0];
  var id = profile.id;
  var data = Analytics.Data.Ga.get('ga:' + id, 'yesterday', 'today', metrics, { 'dimensions': dimensions });
  Logger.log(data);
}
