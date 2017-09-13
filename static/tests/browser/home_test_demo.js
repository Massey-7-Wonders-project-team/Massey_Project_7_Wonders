module.exports = {
    'home test': function (client) {
        client
      .url('http://localhost:3000/')
      .waitForElementPresent('body', 1000);
    },
};
