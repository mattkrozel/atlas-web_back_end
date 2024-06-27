const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('Two Integers', function() {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(2, 3), 5);
    });
  });
});
