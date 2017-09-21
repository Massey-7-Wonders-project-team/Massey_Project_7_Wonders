/* eslint-disable */

const selenium = require('selenium-download');

selenium.ensure('./node_modules/nightwatch/bin', function (error) {
  if (error) console.error(error.stack);
  process.exit(0);
});
