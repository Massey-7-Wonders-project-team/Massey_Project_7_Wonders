/* jshint expr: true */
module.exports = {
    tags: ['firstTest'],
    'home test': function (client) {
        client
            .url('http://localhost:3000/home')
            .pause(1000);

        client.expect.element('body').to.be.present;

        client.expect.element('div').to.have.attribute('id').which.contains('root');
        client.expect.element('div').to.have.attribute('class').which.contains('container');
        client.expect.element('div').to.have.attribute('class').which.contains('container test-centre');

        client.end();
    },
};
