// index.html の sanitize と同じ実装を検証する
function sanitize(v) {
  return String(v == null ? '' : v)
    .replace(/[\\\u0000-\u001f\u007f]/g, '')
    .replace(/／/g, '/')
    .trim();
}
const FALLBACK = '(相談者にフォールバック)';
const cases = [
  ['やま\\だ', 'やまだ'],
  ['ふつうの名前', 'ふつうの名前'],
  ['みか\t', 'みか'],
  ['a\r\nb', 'ab'],
  ['さくら／ゆき', 'さくら/ゆき'],
  ['\\\\', FALLBACK],
  ['  ゆき  ', 'ゆき'],
  ['C:\\書類', 'C:書類'],
];
let ok = true;
for (const [inp, want] of cases) {
  const got = sanitize(inp) || FALLBACK;
  const pass = got === want;
  if (!pass) ok = false;
  console.log((pass ? 'OK ' : 'NG ') + JSON.stringify(inp) + ' -> ' + JSON.stringify(got));
}
console.log(ok ? '\n全件パス' : '\n失敗あり');
