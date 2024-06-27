const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('Two Integers', function() {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(2, 3), 5);
    });
  });
  describe('First round', function() {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(3.7, 1), 5);
    });
  });
  describe('Second round', function() {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });
  describe('Both round', function() {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });
});
