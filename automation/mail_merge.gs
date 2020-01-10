// global variables
EMAIL_SENT = 'EMAIL_SENT';

// trigger functions
// function doOpen() {
function onOpen(e) {
    var ui = SpreadsheetApp.getUi();

    ui.createMenu('Mail Merge')
        .addItem('Send Emails', 'send_emails')
        // @TODO: create "Run Test Emails" that will send to me, user, and anyone in team that opted in for testing
        .addToUi();
}

// opens email document using a document id
function open_doc(doc_id) {
    // var doc = DocumentApp.openById(doc_id);
    var doc = DocumentApp.openById(doc_id);
    content = doc.getBody();
    return content.getText();
}

// gets subject line given paragraph string
function get_subject(doc_text) {
    text_arr = doc_text.split('\n');
    subject = ''; // @TODO: Create error handler for empty subject
    text_arr.forEach(function (e) {
        line = e.split(':');
        if (line[0] == 'Subject') subject = line[1].trim();
    });
    return subject;
}

function get_body(doc_text) {
    text_arr = doc_text.split('\n');
    // @TODO: Create error handler for empty body
    body = text_arr.filter(function (e) { return e.split(':')[0].toString() != 'Subject' });
    return body.join('\n');
}

// goes through Email List sheet tab and seets
function send_emails() {
    var sheet = SpreadsheetApp
        .getActiveSpreadsheet()
        .getSheetByName('Email List');

    names = sheet.getRange('A2:A').getValues();
    emails = sheet.getRange('B2:B').getValues();

    // @TODO: see if you can create dialogue so team can just choose based on template name
    doc_ids = sheet.getRange('C2:C').getValues();
    status = sheet.getRange('D2:D');


    for (var i = 0; i < emails.length; i++) {
        // skip empty email fields
        if (emails[i] == "") continue;

        if (status.getCell(i + 1, 1).getValue() != EMAIL_SENT) {

            doc_id = open_doc(doc_ids[i]);
            subject = get_subject(doc_id);
            body = get_body(doc_id);

            // @TODO: see if fields can be put using JSON/list (also write a script that will generate JSON for team or find better process) 
            subject = subject.replace(/\*\|name\|\*/g, names[i]);
            body = body.replace(/\*\|name\|\*/g, names[i]);


            try {
                Logger.log(body);

                MailApp.sendEmail(emails[i], subject, '', { htmlBody: body, name: 'Alex Lee' });

                // MailApp.sendEmail(emails[i], subject, body);
                // Logger.log('Remaining Email Quota: ' + MailApp.getRemainingDailyQuota());

                // @TODO: replace this with logging function instead
                status.getCell(i + 1, 1).setValue(EMAIL_SENT);
                Logger.log(emails[i] + ' was sent an email.');

            } catch (err) {
                Logger.log('WARNING: ' + emails[i] + ' might not be a valid email. Please remove this from the list.');
            }
        } else {
            Logger.log(emails[i] + ' was not sent an email.');
        }
    }

    SpreadsheetApp.flush();
}

// unit and integration test functions
function test_get_subject() {
    Logger.log(get_subject(open_doc('1-oE17V5WAkFGJqXmi6VGtv7_WnpnohBibNWYc_yl_CA')));
}

function test_get_body() {
    Logger.log(get_body(open_doc('1-oE17V5WAkFGJqXmi6VGtv7_WnpnohBibNWYc_yl_CA')));
}