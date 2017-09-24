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
        .click('span#PlayButton')
        .pause(3000);
    },
    'game test': function (client) {
        client
        .click('input#single')
        .click('button#Play-CreateGame')
        .pause(3000)
        .assert.containsText('.Game', 'there are 7 players so far')
        .click('button#ReadyButton')
        .pause(3000)
        .assert.visible('.PlayerDisplayBoard')
        .assert.visible('#CardHeader')
        .assert.visible('#CardText')
        // need to assert there are 7 cards
        .assert.visible('.Card')
    },
    'wonder board test': function (client) {
        client
        .assert.containsText('#CardHeader span:first-of-type', 'test')
        .click('#leftNav input')
        .pause(1000)
        .assert.containsText('#CardHeader span:first-of-type', 'Computer Player 1')
        .click('#rightNav input')
        .assert.containsText('#CardHeader span:first-of-type', 'test');
    },
    'play card test': function (client) {
        client
        .assert.elementPresent('.Card[data-card-number="6"]')
        .assert.elementPresent('.Card[data-card-number="5"]')
        .assert.elementPresent('.Card[data-card-number="4"]')
        .assert.elementPresent('.Card[data-card-number="3"]')
        .assert.elementPresent('.Card[data-card-number="2"]')
        .assert.elementPresent('.Card[data-card-number="1"]')
        .assert.elementPresent('.Card[data-card-number="0"]')
        .click('.Card .PlayCardButton')
        .pause(2000)
        .assert.elementNotPresent('.Card[data-card-number="6"]')
        .click('.Card .DiscardCardButton')
        .pause(2000)
        .assert.elementNotPresent('.Card[data-card-number="5"]')
        .end();
    },
};
