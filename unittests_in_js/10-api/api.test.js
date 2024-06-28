const request = require('request');
const { expect } = require('chai');
describe('Integration Testing', () => {
  describe('GET /', () => {
    it('Code: 200 | Body: Welcome to the payment system', (done) => {
      const options = {
        url: 'http://localhost:7865',
        method: 'GET',
      };
      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
  describe('GET /cart/12', () => {
    it('Responds with 200 and id 12 in msg', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/12',
        method: 'GET',
      };
      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    });
  });
  describe('GET /cart/hello', () => {
    it('Responds with 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/hello',
        method: 'GET',
      };
      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
  describe('GET /available_payments JSON string', () => {
    it('Responds with 200 and correct json string', (done) => {
      const options = {
        url: 'http://localhost:7865/available_payments',
        method: 'GET',
      };
      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal(
          '{"payment methods":{"credit_cards":true,"paypal":false}}'
        );
        done();
      });
    });
  });
  describe('POST /login with body', () => {
    it('Responds with 200 and correct name Betty', (done) => {
      const options = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        json: {
          username: 'Betty',
        },
      };
      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      });
    });
  });
});
