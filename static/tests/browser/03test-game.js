// module.exports = {
//     'home test': function (client) {
//         client
//         .url(client.launchUrl)
//         .waitForElementPresent('body', 3000);
//     },
//     'login test': function (client) {
//         client
//         .url(client.launchUrl + '/login')
//         .waitForElementPresent('body', 3000)
//         .setValue('input[type=email]', client.test_email + '@test.com')
//         .setValue('input[type=password]', 'password')
//         .click('button#LoginButton');
//     },
//     'navigation test': function (client) {
//         client
//         .click('button#Nav-Hamburger')
//         .pause(1000)
//         .click('')
//     },
//     'game test': function (client) {
//         client
//         .pause(3000)
//         .click('input#single')
//         .click('button#Play-CreateGame')
//         .pause(3000)
//         .assert.containsText('.Game', 'there are 7 players so far')
//         .end();
//     },
// };
