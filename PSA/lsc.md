
Feature type(*cons, vowel, semivowel)
Feature place(bilabial, alveolar, velar, glottal)
Feature manner(stop, fricative, nasal, lateral)
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
Symbol w [bilabial semivowel]
Symbol j [alveolar semivowel]
Class sonorant {m, n, l, r, w, j}
Class stop {p, t, k}

Deromanizer:
  ' => ʔ
  \? => ʔ
  \- => *

primary-stress-second-last-syllable [vowel]:
  [] => [primary] / _ [] $
  Else: [] => [primary]

add-secondary-stress [vowel] propagate:
  [unstressed] => [secondary] / _ [] {[primary], [secondary]}

long-vowels-to-diphthongs:
    aa => aw
    uu => uw
    ee => ej
    oo => ow

styncopate:
  [unstressed vowel] => * // [vowel] _

hw-epenthesis:
  hw => huw / $ _
  hw => w

unstress:
  [] => [unstressed]

diphthong-simplify-near-cluster:
  ai => a / _ [cons] [cons]
  au => a / _ [cons] [cons]
  oi => o / _ [cons] [cons]
  ui => u / _ [cons] [cons]

nasal-metathesis:
  [cons]$1 n => n $1 / _ $
  then:
    {j,y,w} n => {jĩ, jĩ, wũ} *

epenthesis:
  t s => ts / _ # don't seperate ts
  [cons]$1 [cons]$2 => $1 ɪ $2 / _ {j, i, ɪ}
  [cons]$1 [cons]$2 => $1 ʌ $2 / {w, u, ʌ} _
  [cons]$1 [cons]$2 => $1 ə $2 / _

special-ts:
  t => ts / _ ([!cons])+ s ([!cons])
special-s:
  n => s / _ ([!cons])+ s ([!cons])

syncope-sufix:
  ([!cons])+ r => * / _ ([!cons])+ s
  ([!cons])+ r s => * / _ ([!cons])+ s ([!cons])+ r

primary-stress-second-syllable [vowel]:
  [] => [primary] / $ [] _
  Else: [] => [primary]

add-secondary-stress2 propagate:
  [unstressed] => [secondary] / {[primary], [secondary]} [unstressed] _

add-secondary-stress-first:
  [unstressed] => [secondary] / $ _

weaken-unstressed-vowels:
  ai&[unstressed] => i
  au&[unstressed] => u
  oi&[unstressed] => o
  ui&[unstressed] => i
  i&[unstressed] => ɪ
  {u,a,o}&[unstressed] => ʌ
  e&[unstressed] => ɜ

vowel-harmony:
  [vowel]$1 {s,r} u => $1 {s,r} $1 / _

unstress-2:
  [] => [unstressed]

remove-weak:
  {ɪ, ʌ, ɜ, ə} => * / _ s

final-lention:
  ʌ => u / _ $

degemination propagate:
  ss => s
  tt => ts / _ [vowel]
  tt => tsi / _

rs-epentisis:
  rs [vowel]$1 => r $1 s / _ $
  rs [vowel]$1 => r $1 s $1 / _

Tri:
  [central] w [vowel] r => ur
  ii => yi
  ww => wu / _ [!vowel]
  ww [vowel]$1 => w $1 w $1

nasalization:
  [vowel front] => ĩ / _ n
  [vowel back high] => ũ / _ n
  [vowel] => ã / _ n

nasal-syncope:
  n [central] => * / [nasalized] _
  n => * / _ [cons]
  n => * / _ $

glottal-loss:
  ʔ => * / {[cons] _, _ [cons]}