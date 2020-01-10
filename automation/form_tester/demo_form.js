const formTest = require('./testing_demo.js');

// Example 1
new formTest.FormTest().run('https://www.agari.com/demo/', async function() {

  // fills form with information from dictionary
  await this.fillForm({
    '#FirstName': 'Test',
    '#LastName': 'Tester',
    '#Company': 'WebEnertia',
    '#Title': 'Developer',
    '#Email': 'test@webenertia.com',
    '#Phone': '4082460000',
    '#Employee_Size_Range__c': '1000-6000',
    '#Country': 'United States',
    '#State': 'CA'
  });

  // submits form using button with given selector
  await this.submit('.mktoButton');

  // checks if given URL and current URL of page match
  return await this.checkUrl('https://www.agari.com/thank-you/');
});

// Example 2
// new formTest.FormTest().run('https://www.agari.com/demo/', async function() {

//   // fills form with information from dictionary
//   await this.fillForm({
//     '#FirstName': 'Test',
//     '#LastName': 'Tester',
//     '#Company': 'WebEnertia',
//     '#Title': 'Developer',
//     '#Email': 'test@webenertia.com',
//     '#Phone': '4082460000',
//     '#Employee_Size_Range__c': '1000-6000',
//     '#Country': 'United States',
//     '#State': 'CA'
//   });

//   // logs values of following selectors
//   console.log(await this.getValues([
//     '#FirstName',
//     '#LastName',
//     '#Company',
//     '#Title',
//     '#Email',
//     '#Phone',
//     '#Employee_Size_Range__c',
//     '#Country',
//     '#State'
//   ]));

//   // submits form using button with given selector and takes screenshot
//   // await this.submit('.mktoButton', { path: 'example2.png' });

//   // check value of specific selector
//   return await this.checkValue('#FirstName', 'Test');

//   // checks if all values match
//   // return await this.checkValues({
//   //   '#FirstName': 'Test',
//   //   '#LastName': 'Tester',
//   //   '#Company': 'WebEnertia',
//   //   '#Title': 'Developer',
//   //   '#Email': 'test@webenertia.com',
//   //   '#Phone': '4082460000',
//   //   '#Employee_Size_Range__c': '1000-6000',
//   //   '#Country': 'United States',
//   //   '#State': 'CA'
//   // });
// });
