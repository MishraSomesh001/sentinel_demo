const test = require('node:test');
const assert = require('node:assert');
const _ = require('lodash');

test('lodash is importable', () => {
  assert.ok(_.VERSION);
});

test('cloneDeep works', () => {
  const obj = { a: [1, 2, { b: 3 }] };
  const cloned = _.cloneDeep(obj);
  assert.deepStrictEqual(cloned, obj);
  assert.notStrictEqual(cloned.a, obj.a);
});
