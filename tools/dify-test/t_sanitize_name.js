function sanitize(v) {
    return String(v == null ? '' : v)
      .replace(/[\\\u0000-\u001f\u007f]/g, '')
      .replace(/／/g, '/')
      .trim();
  }
function sanitizeName(v) {
    // slice は UTF-16 の単位で切るため、20文字目が絵文字や異体字（𠮷 など）だと
    // ペアが割れて末尾に壊れた1文字が残る。[...文字列] はコードポイント単位で
    // 分解するので割れない。利用者から見た「20文字」とも数え方が一致する。
    return [...sanitize(v).replace(/[：:]/g, '')].slice(0, 20).join('');
  }
const FB = '(fallback)';
const cases = [
  ['\u307f\u3055\u304d', '\u307f\u3055\u304d'],
  ['\u307f\u3055\u304d\uFF1ADV', '\u307f\u3055\u304dDV'],
  ['\u307f\u3055\u304d:DV', '\u307f\u3055\u304dDV'],
  ['\u307f\u3055\u304d\uFF0F\u5e74\u4ee3\uFF1A99', '\u307f\u3055\u304d/\u5e74\u4ee399'],
  ['\u3084\u307e\\\u3060', '\u3084\u307e\u3060'],
  ['\u3042'.repeat(30), '\u3042'.repeat(20)],
  ['  \u3086\u304d  ', '\u3086\u304d'],
  ['\uFF1A\uFF1A\uFF1A', FB],
];
let ng = 0;
for (const [i, w] of cases) {
  const g = sanitizeName(i) || FB;
  const pass = g === w;
  if (!pass) ng++;
  console.log((pass ? 'OK ' : 'NG ') + JSON.stringify(i) + ' -> ' + JSON.stringify(g));
}
const lone = /[\uD800-\uDBFF](?![\uDC00-\uDFFF])|(?<![\uD800-\uDBFF])[\uDC00-\uDFFF]/;
for (const [label, s] of [
  ['20\u6587\u5b57\u76ee\u304c\u7570\u4f53\u5b57', '\u3042'.repeat(19) + String.fromCodePoint(0x20BB7)],
  ['20\u6587\u5b57\u76ee\u304c\u7d75\u6587\u5b57', '\u3042'.repeat(19) + String.fromCodePoint(0x1F338)],
  ['\u7d75\u6587\u5b57\u3060\u3051 25\u500b', String.fromCodePoint(0x1F338).repeat(25)],
]) {
  const cut = sanitizeName(s);
  const bad = lone.test(cut);
  if (bad) ng++;
  console.log((bad ? 'NG ' : 'OK ') + label + ': \u5272\u308c' + (bad ? '\u3042\u308a' : '\u306a\u3057')
    + ' / \u6587\u5b57\u6570=' + [...cut].length);
}
console.log(ng ? '\n>>> ' + ng + ' NG' : '\n>>> all pass');
