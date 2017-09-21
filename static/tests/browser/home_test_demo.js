module.exports = {
    'home test': function (client) {
        client
      .url(client.launchUrl)
      .waitForElementPresent('body', 3000);
    },
};
