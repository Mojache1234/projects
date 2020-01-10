const autoTest = require('./testing_demo.js');

autoTest.start({
  url: 'https://www.agari.com/demo/',
  submitButton: '.mktoButton',
  form: {
    '#FirstName': 'Test',
    '#LastName': 'Tester',
    '#Company': 'WebEnertia',
    '#Title': 'Developer',
    '#Email': 'test@webenertia.com',
    '#Phone': '4082460000',
    'select#Employee_Size_Range__c': '1-6000',
    'select#Country': 'United States'
  },
  formWait: {
    'select#State': 'CA'
  }
});

