const assert = require('assert').strict;
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('sum', function() {
    it('should return 6', function () {
      assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });
  describe('subtract', function() {
    it('should return -4', function () {
      assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
  });
  describe('divide', function() {
    it('should return .2', function () {
      assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
  });
  describe('divide error', function() {
    it('should return Error', function () {
      assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
});
