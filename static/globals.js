const shortid = require('shortid');

const emailId = shortid.generate();

module.exports = {
    test_email: emailId + '@test.com',
};
