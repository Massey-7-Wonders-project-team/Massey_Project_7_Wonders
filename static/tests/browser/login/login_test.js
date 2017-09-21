module.exports = {
    tags: ['loginTest'],
    'home test': function (client) {
        client.url(client.launchUrl + '/game').pause(1000);
        client.expect.element('body').to.be.present;
        client.expect.element('div').to.have.attribute('id').which.contains('root');
        client.end();
    },
};
