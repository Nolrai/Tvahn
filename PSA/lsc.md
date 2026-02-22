
Feature type(*cons, vowel)
Feature place(bilabial, alveolar, velar, glottal)
Feature manner(stop, fricative, semivowel, nasal, lateral)
Feature height(low, mid, high)
Feature frontness(front, central, back)
Feature nasalized(nasalized)
Feature stress(*unstressed, secondary, primary)
Diacritic ˈ (floating) [primary]
Diacritic ˌ (floating) [secondary]
Symbol a [low back vowel]
Symbol ã [low back nasalized vowel]
Symbol e [mid front vowel]
Symbol i [high front vowel]
Symbol ĩ [high front nasalized vowel]
Symbol o [mid back vowel]
Symbol u [high back vowel]
Symbol ũ [high back nasalized vowel]
Symbol ə [mid central vowel]
Symbol ɪ [high central vowel]
Symbol ʌ [low central vowel]
Symbol s [alveolar fricative cons]
Symbol r [alveolar lateral cons] # or whatever you want it to be
Symbol h [glottal fricative cons]
Symbol w [bilabial semivowel cons]
Symbol j [alveolar semivowel cons]
Class sonorant {m, n, l, r, w, j}
Class stop {p, t, k}

Deromanizer:
  ' => ʔ

primary-stress-second-last-syllable [vowel]:
  [] => [primary] / _ [] $ Else:
  [] => [primary]

add-secondary-stress [vowel] propagate:
  [unstressed] => [secondary] / _ [] {[primary], [secondary]}
  long-vowels-to-diphthongs:
    aa => aw
    uu => uw
    ee => ej
    oo => ow

styncopate:
  [unstressed vowel] => * // [vowel] _

unstress:
[] => [unstressed]

diphthong-simplify-near-cluster:
ai => a / _ [cons] [cons] au => a / _ [cons] [cons] oi => o / _ [cons] [cons] ui => u / _ [cons] [cons]

nasal-metathesis:
[cons]$1 n => n $1 / _ $ then:
{j,y,w} n => {jĩ, jĩ, wũ} *

epenthesis:
  t s => ts / _ # don't seperate ts
  [cons]$1 [cons]$2 => $1 ɪ $2 / _ {j, i, ɪ}
  [cons]$1 [cons]$2 => $1 ʌ $2 / {w, u, ʌ} _
  [cons]$1 [cons]$2 => $1 ə $2 / _

special-ts:
  t => ts / _ [vowel] s [vowel]
special-s:
  n => s / _ [vowel] s [vowel]
syncope-sufix:
  [vowel] r => * / _ [vowel] s [vowel] r s [vowel] => * / _ s [vowel] r
vowel-harmony:
  [vowel]$1 s u => $1 s $1 / _
final-lention:
  ʌ => u / _ $

degemination:
  t t => ts / _ [vowel]
  t t => tsi / _

Tri:
  [central] w [vowel] r => ur
  ii => yi
nasalization:
  [vowel front] => ĩ / _ n
  [vowel back high] => ũ / _ n
  [vowel] => ã / _ n

nasal-syncope:
  n [central] => * / [nasalized] _
  n => * / _ [cons] n => * / _ $

glottal-loss:
  ʔ => * / {[cons] _, _ [cons]}