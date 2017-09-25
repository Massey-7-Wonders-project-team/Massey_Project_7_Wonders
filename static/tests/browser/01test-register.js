module.exports = {
    'register test': function (client) {
        client
        .url(client.launchUrl + '/register')
        .waitForElementPresent('body', 3000)
        .setValue('input[type=profile]', 'test')
        .setValue('input[type=email]', client.globals.test_email)
        .setValue('input[type=password]', 'password')
        .click('button#RegisterButton')
        .pause(3000)
        .assert.containsText('.container button', 'Select Play in the Menu to find a Game to join'.toUpperCase())
        .end();
    },
};
