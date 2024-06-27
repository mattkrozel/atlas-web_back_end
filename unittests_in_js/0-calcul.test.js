const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('Two Integers', function() {
    it('should return 4', function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });
  describe('First round', function() {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });
  describe('Second round', function() {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });
  describe('Both round', function() {
    it('should return 6', function () {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });
  describe('2 round', function() {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });
  describe('one round floor', function() {
    it('should return 4', function () {
      assert.strictEqual(calculateNumber(1, 3.3), 4);
    });
  });
});
