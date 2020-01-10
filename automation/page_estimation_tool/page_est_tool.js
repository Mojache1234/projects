// Set global variables
var ss = SpreadsheetApp.getActiveSpreadsheet();
var ui = SpreadsheetApp.getUi();

function doOpen() {

  // Create Menu
  ui.createMenu('Run Script')
    .addItem('Run', 'runScript')
    .addItem('Clear Tabs', 'clearTabs')
    .addToUi();

  // Clear tabs at the beginning
  clearTabs();
}

// Run Script
function runScript() {
  var linksArray = [];
  var lastRow = ss.getSheetByName('Original').getLastRow();
  var links = ss.getRange('A1:A' + lastRow.toString()).getValues();
  var pages = pageSort(links);

  // Create a page for each item
  for (var page in pages) {
    var newPage = ss.insertSheet();
    newPage.setName(page + " - " + pages[page].length.toString());

    // Insert each link in respective page
    var range = newPage.getRange('A1:A' + pages[page].length.toString());
    var r = 1;
    for (var link in pages[page]) {
      var cell = range.getCell(r++, 1);
      cell.setValue(pages[page][link]);
    }
    ss.setActiveSheet(newPage);
  }
  ss.setActiveSheet(ss.getSheetByName('Original'));
}

// Function that returns a JSON object with keys as first layer page and values as list of pages
function pageSort(links) {
  var linksObj = {};
  var otherLinks = [];

  for (var i in links) {
    var link = links[i][0];
    if (!/\/$/.test(link)) link = link + '/';

    // Check if link has hashes or query strings. If so, skip.
    if (/^http(s)?:\/\/www.+?\/(.+)?[#|?](.+)?/.test(link)) {
      otherLinks.push(link);
      continue;
    };

    // Check if link starts with www
    if (/^(http(s)?:\/\/www)/.test(link)) {
      // Extract parent link
      var sublink = link.match(/^http(s)?:\/\/www.+?\/(.+?\/)?/)[2];
      var parent = sublink ? sublink.substring(0, sublink.length - 1) : "/";

      // If it doesn't end with a slash, append one then check if it already exists in list
      if (linksObj[parent] && linksObj[parent].indexOf(link) != -1) continue;

      if (!linksObj[parent]) linksObj[parent] = [link];
      else linksObj[parent].push(link);
    } else otherLinks.push(link);
  }

  if (otherLinks) addOther(otherLinks);
  return linksObj;
}

// Function to delete all except for original and other
function clearTabs() {
  var sheets = ss.getSheets();

  // Delete all sheets
  for (var i = 0; i < sheets.length; i++) {
    var sheet = sheets[i];
    if (sheet.getSheetName() != "Original" && sheet.getSheetName() != "Other") {
      ss.deleteSheet(sheets[i]);
    }
  }

  // Clear out other sheet
  var other = ss.getSheetByName('Other');
  other.clear();
}

// Add to Other List
function addOther(links) {
  var other = ss.getSheetByName('Other');
  var range = other.getRange('A1:A' + links.length.toString());
  links = links.map(function (x) { return [x] });
  range.setValues(links);
}
