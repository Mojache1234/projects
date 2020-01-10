const imageDiff = require('image-diff');

imageDiff({
  actualImage: './example.png',
  expectedImage: './example.png',
  diffImage: 'result.png'
}, (err, imagesAreSame) => {
  if (err) console.log(err);
  else console.log(imagesAreSame);
});
