module.exports = {
    'home test': function (client) {
        client
        .url(client.launchUrl)
        .waitForElementPresent('body', 3000);
    },
    'login test': function (client) {
        client
        .url(client.launchUrl + '/login')
        .waitForElementPresent('body', 3000)
        .setValue('input[type=email]', client.globals.test_email)
        .setValue('input[type=password]', 'password')
        .click('button#LoginButton')
        .pause(3000)
        .assert.containsText('.container h1', 'Welcome')
        .assert.containsText('.container button span', 'Select Play in the Menu to find a Game to join'.toUpperCase());
    },
    'navigation test': function (client) {
        client
        .click('div.Nav button svg')
        .pause(1000)
        .waitForElementPresent('.Nav-Drawer .open', 3000)
        .click('span#LogoutButton')
        .pause(3000);
    },
    'logout test': function (client) {
        client
        .assert.containsText('.container h1', 'Welcome')
        .assert.containsText('.container p', 'Sign in or Register to begin')
        .end();
    },
};
