# Sahumank Print Packet

Sahumank / Sahumãk working notes

Generated: 2026-08-10

## Source Inventory

- `Sahumãk/sahumãk.md`
- `Sahumãk/SVG/Syllables.png`
- `Sahumãk/Grammar.md`
- `Sahumãk/vocab.csv`
- `Sahumãk/Adpositions.csv`
- `Sahumãk/MainVerbs.csv`
- `Sahumãk/WestWallCommentary.md`
- `Sahumãk/WestWall(Gloss).txt`
- `Sahumãk/WestWall_en.txt`
- `Sahumãk/Relay Final.txt`
- `Sahumãk/The Founding.md`
- `Sahumãk/Sahumãk Historical and Archaeological .md`
- `Sahumãk/SettingInfo.md`
- `Sahumãk/LaterHistoriography.md`
- `Sahumãk/Scribal Comprehension.md`

<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/sahumãk.md</code></p>

# Sahumãk

This is the earliest attested written language descended from PSA. Spoken among the Sahumãk, or Promised Water, refering to the lake known as Lake Nicaragua aka Cocibolca aka Granada in OTL.

The written language of the oldest items is sometimes refered to as Late PSA even though thats technically a misnomer, but there were significant phonological and orthographic changes just after this period so they really are in some ways more similar to the reconstructed PSA than they are to later writing.

# LATE PSA Ribbon Writing System (Final Summary)


## Overview

The PSA writing system is a **ribbon-based, knot-constructed featural syllabary**. Each written unit represents a syllable built from:

* **Onset (consonant class)**
* **Nucleus (vowel family + variant)**
* **Coda (termination behavior)**

The system is physically realized by pulling a backing thread through colored strands held by the fingers, producing visible **bands**.

---

## Core Structural Model

Each syllable =

**[Onset pattern] + [3-band nucleus] + [coda modification]**

* Onset and nucleus are distinguished by **position and structure**, not just sequence
* Reduced vowels may omit the nucleus entirely

---

## Band Encoding System

Two colors are used:

* **1 = red**
* **9 = black**

Bands are ordered sequences of these values.

---

## Nucleus System (Vowels)

All full nuclei use **3 bands**.

| Pattern | Value | Symbol  |
| ------- | ----- | -----   |
| 111     | i     | ☰      |
| 119     | ĩ     | ☴      |
| 191     | a     | ☲      |
| 199     | ã     | ☶      |
| 911     | o     | ☱      |
| 919     | e     | ☵      |
| 991     | u     | ☳      |
| 999     | ũ     | ☷      |

### System Logic

* First two bands = vowel family
* Final band = variant (oral vs nasal / paired vowel)

Families:

* 11_ → i / ĩ
* 19_ → a / ã
* 91_ → o / e
* 99_ → u / ũ

---

## Reduced Vowels

Reduced vowels:

* Usually **not written**
* Or written as nearest full vowel in formal contexts

Formal writing prefers filling all nuclei using:

* i, a, u (rarely e, almost never nasal)

---

## Onset System

Onsets are encoded as **variable-length band patterns** before the nucleus.

| Pattern | Onset | Symbol |
| ------- | ----- | ------ |
|   1     | p     | ⚊      |
|  11     | t     | ⚌      |
|  91     | m     | ⚍      |
| 191     | n     | ☲      |
| 111     | h     | ☰      |
|   9     | k     | ⚋      |
|  19     | s     | ⚎      |
| 119     | ts    | ☴      |
|  99     | l     | ⚏      |
| 199     | r     | ☶      |


### Notes

* j and w are treated as part of the nucleus
* Onset/nucleus ambiguity is resolved by **position in ribbon**

---

## Glide / Diphthong System

Glides (j, w) are encoded as **modifications to the nucleus**, not as independent onsets.

### Rule

A glide is represented by modifying one of the nucleus bands, usually making it slightly loose/larger:

* **Opposite-fronting**: (wi we ya yu yo) modify the **first band**
* **Same fronting:** (yi ye wa wu wo) modify the **second band**

### Interpretation

Thus a nucleus can represent:

* Pure vowel (no modification)
* jV / wV diphthong

Example (conceptual):

* 199 (a) → base
* modified first band → ya
* modified second band → wa

This keeps diphthongs within the **3-band nucleus system** without increasing glyph size.

---

## Coda System

Codas are not separate bands. They are expressed via **termination behaviors of the backing thread**:

| Coda | Behavior               |
| ---- | ---------------------- |
| L    | twist (raised texture) |
| R    | loosened loop          |
| N    | visible knot           |

---

## Compression Rule (High-Density Forms)

When onset + nucleus exceed physical capacity (e.g., l + u = 99 + 999):

* The form is **split across the ribbon edges**
* Example: LU → [99-99]

This occurs only in rare cases (primarily {l, r} + u)

---

## Ambiguity Resolution

Ambiguity between onset-only and nucleus-only forms is resolved by:

* Vertical position in ribbon

---

## Writing Modes

### Informal

* Reduced vowels omitted
* the three codas are often all written as an ambigous loose twist, even for n, or rn.
* Visible knots in the backing thread are use ambigously to me coda n, or just a generic punctuation, acting as word phrase or even paragraph boundry.

### Formal / Prestige

* All syllables filled
* Conventional vowel insertion (i/a/u)
* Knowledge of correct insertion is prestigious
* spacings are (in contrast to to infrormal writing) marked by pulling the backing thread back through so as to form a double think stich with no clearly visible bands.

---

## Glyph Inventory Size

Approximate capacity:

* ~8 nuclei × ~10 onsets = ~80 base syllables
* Fits within structural limits of ribbon construction

---

## Conceptual Summary

The system is:

* Featural (binary band patterns)
* Spatial (non-linear ribbon layout)
* Physically grounded (finger-thread manipulation)
* Partially under-specified (reduced vowels omitted)


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/SVG/Syllables.png</code></p>

## Syllables

![Syllables](Sahumãk/SVG/Syllables.png)


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/Grammar.md</code></p>

# 7 Main Verbs

There are seven verbs that can act as main verbs in main clauses: five verbs with governed adpositions, and two freer verbs.

The default sentence structure is a lexical verb or event clause, marked with the topic postposition, followed by one of these five main verbs with its governed adposition.

Destination and benefactive adpositions other than MYU occur after the verb, and are therefore prepositions. Most other adpositions are postpositions and occur before the verb.

MYU always goes before the verb, even when used in a benefactive sense, and can sometimes occur between the lexical verb and the governed adposition.

That is:

[lexical verb / event clause]-TOPIC [postpositional phrases]* [argument phrase]-GOVERNED_ADPOSITION [MYU argument-MYU] MAIN_VERB [prepositional phrases]*

Anything in [] is optional, and []* means repeat zero or more times. While the arguments of TOPIC and the governed adposition are optional, the adpositions themselves are always present in formal writing.

# iɾĩ

Used with MYU, this has a perfective or completive meaning: it implies that the action or task ended naturally and completely. There is also a slight connotation that the action was an assigned task from a higher authority. As often with MYU, the semantic role is flexible: it can mark that authority, the task itself instead of the TOPIC, a physical source, a physical destination, or affected objects. MYU is grammatically rigid here, but semantically flexible.

Used with PAT, it has an exhaustive aspectual meaning: something was completely exhausted, such as space on a wall, paint, or time. There is an implication that, if not for this exhaustion, the action could have continued. It can also be used to describe achievements.

# hiwehh

Used with LUS, this means "because" or anti-"therefore". It marks something as supporting or backgrounded causal ground, not as the asserted result. It may be better glossed as "given" or "supporting-ground" rather than simply "because". This is still a visible metaphor to speakers, since the verb is also used in the physical sense of support, as with a building's foundation.

# ãhh

Used with MYU, this means that a past event is hanging over, lurking behind, or impinging on the present: something backgrounded is now important. For example: "It didn't rain in winter, and now the river sinks low."

# gaiɾu

Used with LUS, this means that the TOPIC creates an exception, or that its absence allows a condition. For example, "[coming inside]-TOP [dinner eating]-LUS GAIɾU" means "You have to come inside to eat dinner", and "[Sun shining]-TOP escaping-LUS GAIɾU" means "He could escape because it was nighttime."

# lãnisuv

Used with RUS, this means "suddenly results from", "moves away from", or "starts from".

Used with MYU, this means "suddenly impacts", "includes", or "expands into, over, or around".

Used with PAT, it means "reached", "affected even this", "continued until", "got to", or "endured up until".

Used with YAIS, it means "latent transformation", "creation", "nurture", "harm", or "injury". It can also literally mean "impregnate", though by Classical Sahumãk this is a very legalistic way to say that. Think English "sire" or "impregnate", not "make love" or "father".

# 2 Free Verbs

There is also an alternate structure that uses "zur" or "luv" as the main verb. These verbs do not take governed adpositions, and they can even drop the topic clause. "luv" especially does not usually take a lexical verb as the topic.

Zur is basically synonymous with English "say", though in informal writing, mostly letters and plays, it can refer to something merely indicated, thought, or acted out. This is similar to quotative "like" in English phrases such as "They were like, 'ew'" or "He's like, 'I am Woman, hear me Roar'." There is no grammatical distinction between direct and indirect quotation. Both the speaker and the means of communication are optional and use the GET adposition, which can appear either as a postposition before the verb or as a preposition after it. However, the speaker always comes before the medium.

Luv does not have a clear translation into English, because it simply means that the TOPIC clause moved in some way. The accompanying adpositional phrases communicate what European languages would usually express with verb choice. For example, there is no basic verb meaning "throw"; instead, there is an adposition meaning "via", "carried by", or "propelled by", which is used in phrases for "throw" or "carry".

# Discourse State

Each of these seven verbs is conjugated for a discourse state. The discourse state describes how the temporal or deictic frame of the discourse is changing, or not changing.

Atemporal - Used for gnomic sentences, habituals, infinitives, and gerunds. When used for physically distant things, it implies shared knowledge. These clauses are invisible for the purposes of how the other three discourse states interact in a conversation or narrative.

Continual - Used to continue a narrative, or to start a section describing the here and now.

Remote - Used to start a section that takes place in the past, or to report distant or surprising events.

Departing - Used to end a section. If the next clause is Continual, then the narrative focus returns to the present. If the next clause is Remote, then the narrative focus moves to a different remote location or past event.


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/vocab.csv</code></p>

## vocab

| PPSA | PSA_gloss | PSA | Zahwãhh | Zahwãhh Gloss | Transliteration | Zahwãhh glyphs |
| --- | --- | --- | --- | --- | --- | --- |
| sohuhumanki | NICARAGUA | sa.hu.mã.k | zahwãhh | Zahwãhh | sa.hu.mã.k |  |
| sosesosetsene | MAYOR | sə.tsã | zetã | King | se.tã |  |
| sosesose | HOUSE | sə.s | zuz | Family | su.ts |  |
| hu | WATER | hu | hu | Water | hu |  |
| astro | GROUND | sə.te.r | zeɾer | Ground/Floor | se.te.r |  |
| iman | BREAST | mã | mã | Breast/Milk | mã |  |
| tsan | ROPE | tsã | dã | Rope | tsã |  |
| pak | BIG-TOE-CLAW | pa.k | bahh | Bigtoe-claw | pa.k |  |
| se | WOOD | se | ze | Wood | se |  |
| ram | DOMESTIC-PIG | ra.m | lã | PIG | ra.m |  |
| ʔhas | FISH | ʔə.ha.s | ehas | Fish | e.ha.ts |  |
| ʔrom | GREASE | ʔe.ro.m | eɾã | Grease/Paint | e.rã |  |
| sorom | RANCID | se.ro.m | zeɾã | Rancid | se.rã |  |
| ʔank | BONE | ʔã.k | ãhh | Bone | ã.k |  |
| upon | EDIBLE-PLANT-MATTER | pã | bã | EDIBLE-PLANT-MATTER | pã |  |
| pum | HANDCLAW | pu.m | buv | HANDCLAW | pũ |  |
| mus | GIVE | mu.s | mus | Give | mu.s |  |
| sik | TAKE | si.k | zihh | Own | si.k |  |
| kemi | USE | ke.m | gib | Use/make use of | ke.m |  |
| kemitsotan | SPEAK | kɪ.mi.tsɪ.sã | givitʃisã | Perform | ki.mi.tsi.sã |  |
| luma | MOTION | lu.m | luv | Move | lu.m |  |
| lante | SETTLE/LOWER | lã.t | lãt | Settle/Lower | lã.t |  |
| ʔen | RISE/STAND | ʔĩ | ĩ | Rise/Stand | ĩ |  |
| rokunk | HUNT | rʌ.kã.k | lehãhh | Sport | le.hã.k |  |
| utun | HOME | tũ | duv | Home | tu.m |  |
| ronst | COOK | sə.st | zet | Housework/Hospitality | se.t |  |
| uukani | CLUTCH | ʌ.ka | eha | Hoard | e.ha |  |
| tesint | BELLY/BIRTH-MOTHER | tsã.ni.t  | dãt | Birth-mother/bearer age people | tã.t |  |
| mank | OBLIGATION/DEBT | mã.k | mãhh | Debt/Obligation/Duty/Honor | mã.k |  |
| miw | ABOVE/FROM | myu | myu | MYU | myu |  |
| pai | INTERIOR/WITHIN | pai | bwi | In | pya |  |
| kun | TOWARD | kũ | guv | Towards | ku.m |  |
| ʔrap | AWAY/FROM | ʔe.ra.p | eɾap | AWAY-FROM | e.ra.p |  |
| kent | BY-HOLDING/CARRIED | kã.t | gãt | By-holding | kã.t |  |
| kept | BY-PROPELLING/THROWN | kə.pə.t | gepet | By-thrown | ke.pe.t |  |
| huhu | RIVER | hu.wu | hwu | Lake/good water | hu.wu |  |
| sohu | POND/CONTAINING-WATER | sou | zwu | Fish-pond | swu |  |
| tsanpak | BOUNDARY/BANK | tsã.pʌ.k | dãpehh | Border/River | tsa.pe.k |  |
| sesotsanpak | FENCE/ENCLOSURE | sə.tsã.pʌ.k | zetãpehh | Fence/wall | se.tsã.pa.k |  |
| imanastro | HILL | ɪ.mə.ste.r | iveter | Hill/slope | i.me.tse.r |  |
| astrosohu | MEADOW/OPEN-GROUND | sə.tsou | zetwu | Forum/Market/Public building | se.tswu |  |
| sohuram | MUD | sa.ra.m | zaɾã | Farm (noun)/ Exploit (verb) | sa.rã |  |
| astrostro | STONE | sto.ste.r | doter | Stone | tso.tse.r |  |
| sosesose | HOUSE | sə.s | zuz | Building/town/family | su.s |  |
| soseronst | Fire | sə.st | zet | HEARTH | se.t |  |
| pumahas | FISH-HOOK | pʌ.mʌ.s | beves | Fish-hook | pe.me.s |  |
| tsanurokunk | TRAP/SNARE | tsã.rʌ.kã.k | dãnehãhh | Ambush/Hunt/Contain | tsã.ne.hã.k |  |
| rokunkutun | BUTCHER | rʌ.kã.kʌ.tã | lehãher | BUTCHER | le.hã.he.r |  |
| musupon | FEED | sʌ.pã | zepã | Feed (verb) | se.pã |  |
| musisik | TRADE | sɪ.sɪ.k | zihh | Market | si.k |  |
| astrostrokimi | CRUSH | sto.ste.rɪ.ki.m | doteɾihib | Crush | tso.tse.ri.hi.m |  |
| sokemiman | NURSE-MOTHER | sə.ke.mə.mã | zehibevã | NURSE-MOTHER | se.hi.me.mã |  |
| sikimani | SIBLING | sɪ.kə.mã | zihevã | Sibling/Comrade | si.he.mã |  |
| tesikimani | YOUNG-SIBLING | tsɪ.kə.mã | tʃihevã | Younger sibling/Brat/underling | tsi.he.mã |  |
| sosikimani | ELDER-SIBLING | si.kə.mã | zihevã | Older sibling | si.he.mã |  |
| musiman | OLDER-SIBLING | sʌ.mã | zevã | Mentor/Sempai/Older sibling | ze.mã |  |
| kemihuhu | GUEST | ke.mwu | gibwu | Guest/Mr/Ms | ki.mwu |  |
| ronstuhu | BOIL | sə.stwu | zetwu | SOUP/Make Soup | se.tswu |  |
| ronstonst | ROAST/BAKE | sə.tsɪ.s | zetʃis | Roast/bake/cook | se.tsi.s |  |
| ronstastrosohuhu | SALT | sə.tsɪ.twu | zetʃiɾwu | Salt/Salted meat/wealth | se.tsi.twu |  |
| ronstastroronst | SMOKE | sə.tsɪ.sə.st | zetʃiset | SMOKE/BLACK/GREY/BLUE | se.tsi.se.ts |  |
| ro | BLOOD | ro | lo | Blood | lo |  |
| tsotan | BREATH | tsɪ.sã | tʃisã | Breath/Life | tsi.sã |  |
| nen | HAND | nĩ | nĩ | Hand | nĩ |  |
| amant | FOOT | ʌ.mã.ni.t | evãt | FOOT | e.mã.t |  |
| nepant | HUNGER | nə.pã.ni.t | nepãt | Need | ne.pã.t |  |
| sun | SLEEP | sũ | zuv | Sleep | su.m |  |
| miwhu | RAIN | mi.wu | miɾu | RAIN | mi.tu |  |
| hanst | DROUGHT | sə.st | zet | Disaster/badweather | se.ts |  |
| etna | WIND | ã.t | ãt | Spirit/Force | ã.t |  |
| etnahu | COLD | tã.nu | dã | Cold | tã |  |
| atup | DAWN | tu.p | dup | Dawn/Tomorrow | tu.p |  |
| hetnos | NIGHT | tə.s | des | Night | te.s |  |
| - |  NAME DAY |  - |  dĩɾup |  TIME |  tĩ.ru.p |  |
| tsene | NAME/WORD | tsĩ | dĩ | Name/WORD | tsĩ |  |
| tsenemank | OATH | tsã.ne.mã.k | dãɾãhh | Oath | tsã.te.k |  |
| tsanro | TABOO | tsã.r | dãr | Wrong | tsã.r |  |
| - | - | - | dãɾi | NEG prefix | tsan.r |  |
| sokemimanpai | ANCESTOR | sʌ.kɪ.mɪ.mã.p | zehivãp | Hero | se.hi.mã.p |  |
| - | 5 king home | nen.sə.tsã.u.tun | nĩtwuɾuv | City | nĩ.twu.tu.m |  |
| - | HAND-FENCE | nĩ.sə.tsã.pʌ.k | nĩsetãpehh | Gate | nĩ.se.tã.pe.k |  |
| - | Handclaw stake | pum.pa.k | bũɾipahh | Handclaw stake | pũ.ta.k |  |
| lin | Three | lin | lĩ | Three | lin |  |
| wa | Two | wa | wa | Two | wa |  |
| semank | promised wood | semãk | zibãhh | Shrine | si.man.k |  |
| kenthetnosʔromtsan | carried night grease rope | kã.t.te.s.ʔe.rom.tsan | gãneseɾãɾitã | Torch/Lamp | kã.ne.se.rã.ri.tsã |  |
| - | Ambusher | irrga | gaɾihh | Commander |  ka.ti.k |  |
| astrostrohuhu |  river stone/gem |  stosterwu |  doteɾu |  child |  sto.ste.wu |  |
| - |  not dawn towards |  tsã.r.tup kan |  dãɾidupagã |  Western |  tsan.ri.tu.pa.kan |  Not found in other PSA languages |
| - |  - |  - |  dazet |  Fire |  ta.sa.t |  Not found in other PSA languages |
| - |  - |  - |  behh |  Body/Flesh |  pe.k |  |
| astrostrohuhuhu |  gem water |  - |  heɾateɾeywu |  ice |  he.ra.te.rey.wu |  |
| - |  Terror Bird |  ʌlɪsə |  eɾise |  beast |  e.ri.se. |  probably from a pre-wind-tribe language of the highlands. |
| - |  - |  - |  wut |  many |  hu.t |  probably from a pre-wind-tribe language of the highlands |
| atupatup |  Dawn dawn |  atup-atup |  dutup |  the future |  tu.tu.p |  probably formed as redup of dup not directly from the PSA root. |


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/Adpositions.csv</code></p>

## Adpositions

| GLOSS | DictionaryForm | LONG-GLOSS | form | underling | surface | transliteration | sahumãk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UP | MYU | UP (sort of) | near-speaker | me.tĩ | mer | me.r |  |
| UP | MYU | UP (sort of) | near-listener | mi.ti.t | miɾit | mi.ri.t |  |
| UP | MYU | UP (sort of) | near-both | me.tĩ.ni.ti.t | meɾĩt | me.rĩ.t |  |
| UP | MYU | UP (sort of) | default | myu | myu | myu |  |
| UP | MYU | UP (sort of) | distal | mã.nũ | mã | mã |  |
| UP | MYU | UP (sort of) | relativised | mwi.r | mwir | mwi.r |  |
| UP | MYU | UP (sort of) | interrogative | mɪ.wi.yi.r | miwiɾir | mi.wi.ri.r |  |
| WITHIN | BAI | Within/between/bounded-by | near-speaker | pe.tĩ | ber | pe.r |  |
| WITHIN | BAI | Within/between/bounded-by | near-listener | pi.ti.t | biɾit | pi.ri.t |  |
| WITHIN | BAI | Within/between/bounded-by | near-both | pe.tĩ.ni.ti.t | beɾĩt | pe.rĩ.t |  |
| WITHIN | BAI | Within/between/bounded-by | default | pai | bwi | pwi |  |
| WITHIN | BAI | Within/between/bounded-by | distal | pã.nũ | bã | pã |  |
| WITHIN | BAI | Within/between/bounded-by | relativised | pyi.r | byir | pyi.r |  |
| WITHIN | BAI | Within/between/bounded-by | interrogative | pyi.r | byir | pyi.r |  |
| TOPIC | LAI | TOPIC | near-speaker | pe.tĩ | ber | pe.r |  |
| TOPIC | LAI | TOPIC | near-listener | pi.ti.t | biɾit | pi.ri.t |  |
| TOPIC | LAI | TOPIC | near-both | pe.tĩ.ni.ti.t | beɾĩt | pe.rĩ.t |  |
| TOPIC | LAI | TOPIC | default | rai | lwi | lwi |  |
| TOPIC | LAI | TOPIC | distal | sã.tã.nã | zãr | sã.r |  |
| TOPIC | LAI | TOPIC | relativised | sĩ.ti.r | zĩnir | sĩ.ni.r |  |
| TOPIC | LAI | TOPIC | interrogative | sĩ.tyi.r | zĩnyir | sĩ.nyi.r |  |
| DOWN-TO | BAT | DOWN-TO | near-speaker | pə.tə.tã | ber | pe.r |  |
| DOWN-TO | BAT | DOWN-TO | near-listener | pɪ.tɪ.ts | biɾit | pi.ri.t |  |
| DOWN-TO | BAT | DOWN-TO | near-both | pə.tə.tã.ni.ts | beɾet | pe.re.t |  |
| DOWN-TO | BAT | DOWN-TO | default | pa.t | bat | pa.t |  |
| DOWN-TO | BAT | DOWN-TO | distal | pə.tã.nã | ber | pe.r |  |
| DOWN-TO | BAT | DOWN-TO | relativised | pi.ti.r | biɾir | pi.ri.r |  |
| DOWN-TO | BAT | DOWN-TO | interrogative | pe.tyi.r | beɾyir | pe.ryi.r |  |
| AGAINST | LÃ | AGAINST / UP-TO | near-speaker | rã.tã | lãr | lã.r |  |
| AGAINST | LÃ | AGAINST / UP-TO | near-listener | rã.ts | lãt | lã.t |  |
| AGAINST | LÃ | AGAINST / UP-TO | near-both | rã.tã.ni.ts | lãnãt | lã.nã.t |  |
| AGAINST | LÃ | AGAINST / UP-TO | default | rã | lã | lã |  |
| AGAINST | LÃ | AGAINST / UP-TO | distal | rã.nã.nã | lã | lã |  |
| AGAINST | LÃ | AGAINST / UP-TO | relativised | rã.ni.r | lãr | lã.r |  |
| AGAINST | LÃ | AGAINST / UP-TO | interrogative | rã.nyi.r | lãɾir | lã.ri.r |  |
| UP-AWAY-FROM | LUS | UP-AWAY-FROM | near-speaker | sə.tã | zer | se.r |  |
| UP-AWAY-FROM | LUS | UP-AWAY-FROM | near-listener | sɪ.ts | zit | si.t |  |
| UP-AWAY-FROM | LUS | UP-AWAY-FROM | near-both | sə.tã.ni.ts | zeɾãt | se.rã.t |  |
| UP-AWAY-FROM | LUS | UP-AWAY-FROM | default | ru.s | lus | lu.s |  |
| UP-AWAY-FROM | LUS | UP-AWAY-FROM | distal | sã.nã | zã | sã |  |
| UP-AWAY-FROM | LUS | UP-AWAY-FROM | relativised | si.r | zir | si.r |  |
| UP-AWAY-FROM | LUS | UP-AWAY-FROM | interrogative | syi.r | zyir | syi.r |  |
| INTO | ZĨ | INTO | near-speaker | sã.tã | zãr | sã.r |  |
| INTO | ZĨ | INTO | near-listener | sã.ts | zãt | sã.t |  |
| INTO | ZĨ | INTO | near-both | sã.tã.ni.ts | zãnãt | sã.nã.t |  |
| INTO | ZĨ | INTO | default | sĩ | zĩ | sĩ |  |
| INTO | ZĨ | INTO | distal | sã.nã.nã | zã | sã |  |
| INTO | ZĨ | INTO | relativised | sã.ni.r | zãr | sã.r |  |
| INTO | ZĨ | INTO | interrogative | sã.nyi.r | zãɾir | sã.ri.r |  |
| PENTETRATE | YAIS | PENTETRATE/ENVELOP | near-speaker | i.sə.tã | iser | i.se.r |  |
| PENTETRATE | YAIS | PENTETRATE/ENVELOP | near-listener | i.sɪ.ts | isit | i.si.t |  |
| PENTETRATE | YAIS | PENTETRATE/ENVELOP | near-both | i.sə.tã.ni.ts | iseɾãt | i.se.rã.t |  |
| PENTETRATE | YAIS | PENTETRATE/ENVELOP | default | yai.s | wis | wi.s |  |
| PENTETRATE | YAIS | PENTETRATE/ENVELOP | distal | i.sã.nã | isã | i.sã |  |
| PENTETRATE | YAIS | PENTETRATE/ENVELOP | relativised | yi.swi.r | yiswir | yi.swi.r |  |
| PENTETRATE | YAIS | PENTETRATE/ENVELOP | interrogative | sa.wi.yi.r | zawiɾir | sa.wi.ri.r |  |
| HELD-BY | GET | HELD-BY/VIA/CONTROLED-BY | near-speaker | kə.tə.tã | ger | ke.r |  |
| HELD-BY | GET | HELD-BY/VIA/CONTROLED-BY | near-listener | kɪ.tɪ.ts | giɾit | ki.ri.t |  |
| HELD-BY | GET | HELD-BY/VIA/CONTROLED-BY | near-both | kə.tə.tã.ni.ts | geɾet | ke.re.t |  |
| HELD-BY | GET | HELD-BY/VIA/CONTROLED-BY | default | ke.t | get | ke.t |  |
| HELD-BY | GET | HELD-BY/VIA/CONTROLED-BY | distal | kə.tã.nã | ger | ke.r |  |
| HELD-BY | GET | HELD-BY/VIA/CONTROLED-BY | relativised | ki.tyi.r | giɾyir | ki.ryi.r |  |
| HELD-BY | GET | HELD-BY/VIA/CONTROLED-BY | interrogative | ki.tyi.r | giɾyir | ki.ryi.r |  |
| TO | GUV | TO/TOWARD/TARGET | near-speaker | kã.tã | gãr | kã.r |  |
| TO | GUV | TO/TOWARD/TARGET | near-listener | kã.ts | gãt | kã.t |  |
| TO | GUV | TO/TOWARD/TARGET | near-both | kã.tã.ni.ts | gãnãt | kã.nã.t |  |
| TO | GUV | TO/TOWARD/TARGET | default | kũ | guv | ku.m |  |
| TO | GUV | TO/TOWARD/TARGET | distal | kã.nã.nã | gã | kã |  |
| TO | GUV | TO/TOWARD/TARGET | relativised | kã.ni.r | gãr | kã.r |  |
| TO | GUV | TO/TOWARD/TARGET | interrogative | kã.nyi.r | gãɾir | kã.ri.r |  |
| ACROSS | BAV | ACROSS | near-speaker | pu.tĩ | bur | pu.r |  |
| ACROSS | BAV | ACROSS | near-listener | pu.ti.t | buɾit | pu.ri.t |  |
| ACROSS | BAV | ACROSS | near-both | pu.tĩ.ni.ti.t | buɾĩt | pu.rĩ.t |  |
| ACROSS | BAV | ACROSS | default | pau | bwu | pwu |  |
| ACROSS | BAV | ACROSS | distal | pũ.nũ | buv | pu.m |  |
| ACROSS | BAV | ACROSS | relativised | pu.wi.r | bwir | pwi.r |  |
| ACROSS | BAV | ACROSS | interrogative | pu.wi.yi.r | bwiɾir | pwi.ri.r |  |


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/MainVerbs.csv</code></p>

## MainVerbs

| GLOSS | DictionaryForm | LONG-GLOSS | SYSTEM | form | underlying | surface | tranliteration | sahumãk glyphs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COMP | IɾĨ | MYU Completative / PAT Exhaustive | MYU/PAT | atemporal | ʔi.tĩ | ir | i.r |  |
| COMP | IɾĨ | MYU Completative / PAT Exhaustive | MYU/PAT | continual | tyi.tĩ | dyir | tyi.r |  |
| COMP | IɾĨ | MYU Completative / PAT Exhaustive | MYU/PAT | remote | ʔi.tə.sa.r | iɾesar | i.te.sa.r |  |
| COMP | IɾĨ | MYU Completative / PAT Exhaustive | MYU/PAT | departing | ʔi.tã.nã | ir | i.r |  |
| SUPP | HIWEHH | RUS Supportive | RUS | atemporal | hɪ.we.k | hiwehh | he.we.ke |  |
| SUPP | HIWEHH | RUS Supportive | RUS | continual | hi.we.k | hiwehh | hi.we.ke |  |
| SUPP | HIWEHH | RUS Supportive | RUS | remote | hɪ.we.se.r | hiweser | he.we.se.r |  |
| SUPP | HIWEHH | RUS Supportive | RUS | departing | hɪ.we.kã | hiwehã | he.we.kã |  |
| LOOM | ÃHH | MYU Looming | MYU | atemporal | ã.k | ãhh | ã.k |  |
| LOOM | ÃHH | MYU Looming | MYU | continual | ã.nũ.k | ãhh | ã.kũ |  |
| LOOM | ÃHH | MYU Looming | MYU | remote | ã.si.r | ãsir | ã.si.r |  |
| LOOM | ÃHH | MYU Looming | MYU | departing | wã.kã | wãhã | wã.hã |  |
| EXCE | GAIɾU | RUS Exceptional | RUS | atemporal | kai.tu | gwir | kwi.r |  |
| EXCE | GAIɾU | RUS Exceptional | RUS | continual | kə.kai.tu | gehwir | ke.hwi.r |  |
| EXCE | GAIɾU | RUS Exceptional | RUS | remote | ki.tswi.sa.r | gitwisar | ki.tswi.sa.r |  |
| EXCE | GAIɾU | RUS Exceptional | RUS | departing | ki.twĩ | giɾwĩ | ki.twĩ |  |
| EXPA | LÃNISUV | RUS Explosive / MYU Expansive / PAT Reaching | RUS/MYU/PAT | atemporal | lã.na.ti.tsũ | lãnisuv | lã.ni.sũ |  |
| EXPA | LÃNISUV | RUS Explosive / MYU Expansive / PAT Reaching | RUS/MYU/PAT | continual | lã.tə.lã.ni.ti.tsã | lãnetã | lã.ne.tã |  |
| EXPA | LÃNISUV | RUS Explosive / MYU Expansive / PAT Reaching | RUS/MYU/PAT | remote | lã.ti.tsi.r | lãnitʃir | lã.ni.tsi.r |  |
| EXPA | LÃNISUV | RUS Explosive / MYU Expansive / PAT Reaching | RUS/MYU/PAT | departing | lã.ti.tsã.nã | lãnitã | lã.ni.tã |  |
| SAY | ZUR | SAY | BASIC | atemporal | su.r | zur | su.r |  |
| SAY | ZUR | SAY | BASIC | continual | sa.r | zar | sa.r |  |
| SAY | ZUR | SAY | BASIC | remote | sa.r | zar | sa.r |  |
| SAY | ZUR | SAY | BASIC | departing | se.rã | zer | se.r |  |
| MOVE | LUV | MOVE | MOTION | atemporal | lu.m | luv | lũ.p |  |
| MOVE | LUV | MOVE | MOTION | continual | lʌ.mʌ.lʌ.m | leveɾev | le.me.re.m |  |
| MOVE | LUV | MOVE | MOTION | remote | lʌ.mʌ.sa.r | levesar | le.me.sa.r |  |
| MOVE | LUV | MOVE | MOTION | departing | lə.mã | levã | le.mã |  |


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/WestWallCommentary.md</code></p>

# The West Wall Inscription

## Editorial Conventions

### Text Conventions

Sahumank monuments such as these were writen as strict matricies of glyph pairs, (but respecting word boundries when breaking lines). Because of this original glyph position is recored as XX:CC(:P) where XX is the line number, CC is the column number, and P is weather its the upper (onset), or lower (rhyme) half of the syllable marker. Importantly for reading, only a single half-syllable is needed for word breaks, this can create some differences between orthographic words, and linguistic or spoken units.

For the purposes of translation its often better to look at meaningful phrases, not the orthographic lines, these are writen XX::WW refering word WW of clause XX, obviously the choice of where to break clauses depends on the reading, and one should not assume that different commentaries on the same text agree, always double check.

Both the the transcription of the orthography use a convention of putting a period between every pair of syllables internal to a word. Given the syllabic nature of Sahumank orthography it actually quite important to being able to convert back and forth between glyphs and transcription.

### Notes on transliteration of Sahumank glyphs:

  The transliteration is syllable by syllable using "." to mark column boundries within a word, as is standard for romanizations of hemisyllabic scrips the onset and nuclus are writen together. Readers should note that in this script glides are part of the nuclear glyph, so "tswi" is the "ts" onset over the "wi" nucleous "", even though many other scrips the reader might be familiar with would render it as "tsw" + "i".

### Gloss abbreviations

`[` `]` are used in the gloss to bracket the clause structure.

a `-` is used for when the english gloss is multiple words for a single Sahumank lexeme (Such as Commander, or Away-From). A `.` is used to attach conjugational information to the lexeme, for Classical Sahumank this consists of two different sytems, one and another that conjugates adpositions for distance, and one that modifies the main (a.k.a gramatical) verb to attach discourse state.
Respectively the abreviations used for these are:

| Form | Meaning |
|---|---|
| `.1` | Near the speaker |
| `.1&2` | Near both speaker and listener |
| `.default` | Deictically unmarked |
| `.distal` | Distant from both |
| `.rel` | Relativizes an adpositional phrase |

  Interogative forms are both in related languages and later texts as a 6th form but haven't been found on an Sahumank Monument so far.

  Main verbs are instead conjugated with one of:
| Form | Meaning |
|---|---|
| `.atemp` | atemporal, this is used for the lexical verb in the lexical verb as topic standard sentence structure, and is also used to stating gnomic or otherwise expansive in time statements |
| `.cont` | continuing the current scene |
| `.remote` | indicates that this event starts a new distant or past tense scene. |
| `.depart` | indicates that this is the last event in the scene and we are departing that scene either to enter a new remote scene or the nearby/present scene |

- How uncertain readings are marked
- Difference between literal and literary translations
- Which grammatical interpretations remain disputed

## Monument Context

- Location and physical arrangement

  Located at 11°07'08.2"N, 84°46'07.3"W, the site contains several distinct archaeological layers. The earliest identified layer is a basal destruction deposit composed of rubble, wood ash, and scattered catgirl bone fragments. Above this deposit stood a rectangular central building surrounded by the paved floors of a larger complex. Most of the surrounding masonry appears to have been removed for reuse in nearby farming communities. The central building, however, collapsed before the site was built over, protecting the Isamã-period remains from later stone-robbing.

A later occupation phase is represented by a large stone oven and several cornerstones bearing mortise slots, both characteristic of Golden Empire garrisons. Most of the buildings and paving stones associated with this phase have also been removed.

The inscribed stone measures 1.3 by 1.6 by 0.3 meters and was discovered lying face down within the collapsed central building. Its carved joints align with those of the surrounding stones, allowing the lower portion of the fallen masonry to be reconstructed as a single, well-defined wall. This reconstruction indicates that the inscription, together with carvings of the Solar Disk and Burning Cage motifs, originally stood approximately two meters above the floor. Chemical or microscopic analysis identified crushed eggshell pigment indicating that all three carvings were painted white in use. Though it should be noted that other pigments could have been used also, eggshell paint can be used as a primer, and its chemical traces last longer then many other traces.

The wall appears to have fallen forward into the building while remaining largely intact. Whether its collapse was deliberate or caused accidentally by shifting foundations remains uncertain; both explanations are consistent with the surviving fractures and wear patterns where the wall met the floor and adjoining walls. Although individual stones shifted significantly during the collapse, the larger components generally retained their relative positions. The fallen masonry was subsequently buried beneath a gravel-and-mortar concrete layer and, later, a layer of brickwork. Remains of gravel-and-mortar concrete is also found under the oven, and samples of the gravel indicate that both were mined from the same gravel bar somewhere near by.

## Estimated Date

Radiocarbon samples taken from charcoal and burned bone within the basal destruction deposit produced statistically consistent calibrated ranges of approximately 120–80 BID. Because the central building was constructed above this deposit, both the building and the West Wall inscription must postdate that event.

Charcoal and soot associated with a later Golden Empire-style garrison oven produced calibrated dates between approximately 200 and 600 AID. This oven belongs to a secondary occupation phase and uses the same techniques and materials as the concrete and brickwork covers.

The inscription therefore postdates the 120-80 and predates the covering layers, which are consistant with the later Golden Empire ocupation.

Its language, iconography, and association with Isamã suggest a date near the beginning of that range,

- Material and preservation
- Relationship between carved lines and grammatical clauses
- Intended audience and political purpose

## Complete Text

### Monumental Text

The inscription exactly as arranged on the wall.

  
   

  
   
  

    
    

    

### Normalized Orthographic Text

The complete Classical Sahumãk text with standardized spacing.

          
        
      
             
       
           
          
           

### Normalized Transliteration

tsan.te.k se.ran pe.rin.t tsan.ri.tu.pa.kan sin.ni.r nin.twu.tu.m ke.t ka.ti.k i.sa.man se.ran.t ki.tswi.sa.r
ka.ti.k i.sa.man pe.rin.t so ke.re.t le.me.re.m pu.rin.t te.s hu.wu
le.me.re.m ke.re.t si.man.k sin.ni.r lin.tsan.r ki.ryi.r nin.se.tan.pe.k
an.k pe.rin.t se.tã sin.ni.r wa.so lan.nan.t ka.ti.k i.sa.man sin.ni.r te.se.t me.rin.t lan.ne.tã rã se.te.r
te kan.ne.se.ran.ri.tsã pe.rin.t ka.ti.k i.sa.man ke.re.t le.me.re.m ku.m
ka.ti.k i.sa.man sin.ni.r pe.k se.pã pe.rin.t ka.ti.k i.sa.man ke.re.t he.we.kã sã se.tun
sto.ste.wu sin.ni.r wa.so myu sa.r pe.r wa sin.ni.r nin.se.tan.pe.k sin.ni.r tsa.pe.k
su.r pe.rin.t ka.ti.k i.sa.man sin.ni.r su.r pe.rin.t te.hi.pe.man myu si.man.k mã tyi.r

## Reconstructed speach

dãɾãhh zeɾã beɾĩt dãɾidupagã zĩnir nĩtwuɾuv get gaɾihh Isamã zeɾãt gitwisar
gaɾihh Isamã beɾĩt zo geɾet leveɾev buɾĩt des hwu
leveɾev geɾet zibãhh zĩnir lĩ-dãr giɾyir nĩsetãpehh
ãhh beɾĩt zetã zĩnir wa-zo lãnãt gaɾihh Isamã zĩnir dezet meɾĩt lãnetã lã zeɾer
de gãneseɾãɾitã beɾĩt gaɾihh Isamã geɾet leveɾev guv
gaɾihh Isamã zĩnir behh zepã beɾĩt gaɾihh Isamã geɾet hiwehã zã ze-dov
doteɾu zĩnir wa-zo myu zar ber wa zĩnir nĩsetãpehh zĩnir dãpehh
zur beɾĩt gaɾihh Isamã zĩnir zur beɾĩt dehibevã myu zibãhh mã dyir.

### Gloss

[Oath-Rancid TOP.1&2] [WESTERN TOP.rel CITY HeldBy.default] [[Commander Isamã] away-from.1&2] Exceptional.remote
[Commander Isamã TOP.1&2] [NURSING HELD-BY.1&2] MOVE.cont [ACROSS.1&2 NIGHT LAKE]
MOVE.cont [VIA.1&2 [SHRINE TOP.rel THREE-TABOO HELD-BY.rel] GATE]
[GRAB.atemp TOP.1&2] [KING TOP.rel TWO-NURSING AGAINST.1&2] [Commander Isamã TOP.rel FIRE MYU.1&2] Explosive.cont [AGAINST GROUND]
[bearing LAMP TOP.1&2] [Commander Isamã HeldBy.1&2] MOVE.cont [TO.default NORTH]
[[Commander Isamã TOP.rel] BODY FEED TOP.1&2] [Commander Isamã HeldBy.1&2] Supportive.depart [INTO.distal NURSING SUN]
[[[child TOP.rel] Two NURSING] MYU.default] SAY.cont [DOWN-TO.1 [TWO [TOP.rel GATE [TOP.rel RIVER]]]]
[SAY.atemp TOP.1&2] [[[[Commander Isamã TOP.rel] SAY.atemp] TOP.rel] HEIR MYU.default] [Shrine MYU.distal] Completative.cont

### Literal Translation

The oath breaking by the western cities allowed Commander Isamã to
(Commander Isamã) carry herself across the Black Water.
[ She ] entered [the shrines] via the doors (the shrines) held.
Below her fire the pressing together between the two kings and the ground rang out!
Miss Lamp, carried by Isamã, moved north.
Commander Isamã's body was fed to Lady Sun by Commander Isamã, therefore
Two of her children command my river's gates.
The Heir spoken of by Commander Isamã speaks all the way to the Shrines.

### Loose Translation

When the western cities broke oath, Commander Isamã crossed the black water.

Three shrines opened their doors to her. Two kings bent knee before her fire. She carried the Lamp northward.

Because She fed the Sun Goddess with her own body, her daughters rule my river-mouths, and Commander Isamã's chosen heir's words reach the shrines.

## Commentary

### W1: The Western Cities Break Oath

#### Text and Gloss

**Orthographic text:**

          
tsan.te.k se.ran pe.rin.t tsan.ri.tu.pa.kan sin.ni.r nin.twu.tu.m ke.t ka.ti.k i.sa.man se.ran.t ki.tswi.sa.r

**Reconstructed speech:**

dãɾãhh zeɾã beɾĩt dãɾidupagã zĩnir nĩtwuɾuv get gaɾihh Isamã zeɾãt gitwisar

**Gloss:**
[Oath-Rancid TOP.1&2] [WESTERN TOP.rel CITY HeldBy.default] [[Commander Isamã] away-from.1&2] Exceptional.remote

**Literal translation:**
The oath breaking by the western cities allowed Isamã [to act].

**Loose translation:**
When the western cities broke oath,

#### Grammatical Commentary

For this clause the finite adpositional forms strongly constrain the clause’s syntactic structure, so the brackets on the gloss are entirely for the reader's convience.
"dãɾãhh zeɾã" was a fixed phrase, although one with transparent derivation, when used as an adjective zĩnir is needed for example "the rotten fish" is "zerã zĩnir ehas" or "ehas zĩnir zera"

Note that fully half the adpositions are in the 1&2 form, acting as more of an default then the 'default' conjugation. While "Get" is glossed as HeldBy, when the topic is an event, it denotes agency, closer to the "by" clause in an english passive.

Note that Sahumank has no mandatory number marking, so "the western city" or "the city from the west" would also be possible translations. We have chosen to use the plural because other depictions of the event usually record it as being either the three southwestern cities, or the whole Sahumank lake area as being responsible, and because the later line mentions multiple kings.

#### Lexical and Translation Commentary

The word glossed Western can be used both for "to the west" and "from the west", or even just "not from the east".

"Nĩtwuɾuv" glossed here as city, had become an opaque compound by this point, and denoted both the urban settlement it self, and the broader territory it controled. Some scholars translate it as county or even richestaat, but both drag in conotations of personal office holding that didn't exist in Sahumank landholding. The political unit in the Nĩtwuɾuv was not the individual but the House, an extended family with the resources to bring a child from infancy to bearing age and then rase that bearer's children, and often identified with the phisical building where bearers and children spent most of their time.

This also highlights a drifting in meaning from when the compound was constructed, to the time of monumental inscriptions, as Nĩtwuɾuv descended from a phrase meaning "five kings house", but by the the time of monumental instructions a Nĩtwuɾuv only has one ruling family who only has one "zeta" ("king") or ceremonial personification.

### Whole Text Commentary

#### Grammatical Commentary

The extensive use of the 1&2 form this is very common in monumental inscriptions like this one, but is unlikely to have been anywhere near that common in speach, or long form writing, but rather is a way to bring the reader into the community that these events affected. Similar uses are found in most mesoamerican desendents of PSA.

--- These two paragraphs need to be rewriten to be about the text as a whole:

Also note that while the literal translation is a complete sentence and the loose translation mearly a clause, the original Sehumank does not truely corespond to either cleanly, because of how Sehumank main verbs build a chain of discourse relationships, producing a discorse structure that is neither as obligatory as english clauses such as "when x, y" needing both halves to be gramatical, but also not as seperated as the complete sentence literal translation indicates.

In some sense "zĩnir", rendered TOP.rel in the gloss, is just a normal cojugated adposition, it's is a unusually gramatically flexible and mandatory. It binds adjectives to their nouns, links nouns to their numerals, and is even used to mark apposition. Here it is in the adjectival binding which is sometimes seen as an form of posesion, Some linguists have even argued that zĩnir was becoming a coupla, though that is an minority oppinion.

#### Lexical and Translation Commentary

Gaɾihh Isamã is an extreamly important character in latter sahumank quoting texts, eventually becoming a divine principle and diety and even overshadowing the Lamp and Sun gods she sacrafices herself to here.

Neither "garihh" or "Isamã" are thought to be native Sahumank words, instead borrowed from southern Wind Tribe languages spoken around the Lake of the Lamp Goddess.

Isama was just one variation on a common name of the region, gaɾihh is interesting because sacred texts of the Lamp Goddess shrine's record it as the "sotherners" pronuciation of "irrga". Several songs apparently writen for consumption by other Wind Tribe populations (and in those languages) "garihh" is called out as being a southern official title the highest any single person can reach, and interestingly explicitly considered to not be part of any 'House'. So we have chosen to translate it as Commander.

Among those tribes around the Lake of the Lamp Godess, Irrga is used to mean something like victor, experienced vetran, or warband organizer in the songs and plays set 'before the sotherners came', a phrase that can either mean something close to an actual historical period, or a fixed phrase mearly setting the genre of the story.

This is interesting linguisticly because irrga and its cognates are in most Wind Tribe languages actually quite negative in conotation, describing pit traps, the realm of the dead, evil, maneating wild beasts suposedly bright red because of the blood of their prey soaking their fur, betrayal, divine curses, and revenge. Though they also pop up as used in what the texts describe as an metaphore to describe clever tactics and strategy. A case that this folk etymology is correct but backwards, (that is it originately meant something like "cleaverly unexpected" or "ambush" and only later gained its moral/supernatural meanings) has been made and is far from settled one way or the other.


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/WestWall(Gloss).txt</code></p>

## WestWall(Gloss)

```text
How it actually appears on the monument
  
   

  
   
  

    
    

    

breaking at claus boundries --

   
  

     
   
       
  
    

          
tsan.te.k se.rã pe.rin.t tsan.ri.tu.pa.kan sin.ni.r nin.twu.tu.m ke.t ka.ti.k i.sa.man se.ran.t ki.tswi.sa.r
dãɾãhh zeɾã beɾĩt dãɾidupagã zĩnir nĩtwuɾuv get gaɾihh Isamã zeɾãt gitwisar
[Oath-Rancid TOP.1&2] [WESTERN TOP.rel CITY HeldBy.default] [[Commander Isamã] away-from.1&2] Exceptional.remote
The oath breaking by the western cities allowed Isamã [to]
When the western cities broke oath,

        
ka.ti.k i.sa.man pe.rin.t so ke.re.t le.me.re.m pu.rin.t te.s hu.wu
gaɾihh Isamã beɾĩt zo geɾet leveɾev buɾĩt des hwu
[Commander Isamã TOP.1&2] [NURSING HELD-BY.1&2] MOVE.cont [ACROSS.1&2 NIGHT LAKE]
Chief Isamã carried herself across the Black Water.
Chief Isamã crossed the black water.

      
le.me.re.m ke.re.t si.man.k sin.ni.r lin.tsan.r ki.ryi.r nin.se.tan.pe.k
leveɾev geɾet zibãhh zĩnir lĩ-dãr giɾyir nĩsetãpehh
MOVE.cont [VIA.1&2 [SHRINE TOP.rel THREE-TABOO HELD-BY.rel] GATE]
[She] entered [the shrines] via the doors (the shrines) opened.
Three shrines opened their doors to her.

             
an.k pe.rin.t se.tã sin.ni.r wa.so lan.nan.t ka.ti.k i.sa.man sin.ni.r te.se.t me.rin.t lan.ne.tã rã se.te.r
ãhh beɾĩt zetã zĩnir wa-zo lãnãt gaɾihh Isamã zĩnir dezet meɾĩt lãnetã lã zeɾer
[GRAB.atemp TOP.1&2] [KING TOP.rel TWO-NURSING AGAINST.1&2] [Commander Isamã TOP.rel FIRE MYU.1&2] Explosive.cont [AGAINST GROUND]
Below her fire the pressing together between the two kings and the ground rang out!
Two kings bent knee before her fire.

       
te kan.ne.se.ran.ri.tsã pe.rin.t ka.ti.k i.sa.man ke.re.t le.me.re.m ku.m
de gãneseɾãɾitã beɾĩt gaɾihh Isamã geɾet leveɾev guv
[bearing LAMP TOP.1&2] [Commander Isamã HeldBy.1&2] MOVE.cont [TO.default NORTH]
Miss Lamp, carried by Isamã, moved north.
She carried the Lamp northward.

           
ka.ti.k i.sa.man sin.ni.r pe.k se.pã pe.rin.t ka.ti.k i.sa.man ke.re.t he.we.kã sã se.tun
gaɾihh Isamã zĩnir behh zepã beɾĩt gaɾihh Isamã geɾet hiwehã zã ze-dov
[[Commander Isamã TOP.rel] BODY FEED TOP.1&2] [Commander Isamã HeldBy.1&2] Supportive.depart [INTO.distal NURSING SUN]
Commander Isamã's body was fed to Lady Sun by Commander Isamã, therefore
Because She fed the Sun Goddess with her own body,

          
sto.ste.wu sin.ni.r wa.so myu sa.r pe.r wa sin.ni.r nin.se.tan.pe.k sin.ni.r tsa.pe.k
doteɾu zĩnir wa-zo myu zar ber wa zĩnir nĩsetãpehh zĩnir dãpehh
[[[child TOP.rel] Two NURSING] MYU.default] SAY.cont [DOWN-TO.1 [TWO [TOP.rel GATE [TOP.rel RIVER]]]]
Two of her children command my river's gates.
her daughters rule my river-mouths,

           
su.r pe.rin.t ka.ti.k i.sa.man sin.ni.r su.r pe.rin.t te.hi.pe.man myu si.man.k mã tyi.r
zur beɾĩt gaɾihh Isamã zĩnir zur beɾĩt dehibevã myu zibãhh mã dyir.
[SAY.atemp TOP.1&2] [[[[Commander Isamã TOP.rel] SAY.atemp] TOP.rel] HEIR MYU.default] [Shrine MYU.distal] Completative.cont
The Heir spoken of by War Leader Isamã speaks all the way to the Shrines.
and Commander Isamã's chosen heir's words reach the shrines.
```


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/WestWall_en.txt</code></p>

## WestWall en

```text
When the western cities broke oath,
Chief Isamã crossed the black water.

Three shrines opened their doors to her.
Two kings bent knee before her fire.

She carried the Lamp northward.

Because She fed the Sun Goddess with her own body,
her daughters rule my river-mouths,
and Commander Isamã's chosen heir's words reach the shrines.
```


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/Relay Final.txt</code></p>

## Relay Final

```text
A forager walks on the mountain.

The traveler roamed over the mountain.

GUEST TOPIC.DIST MOVE.R  OVER.1&2 STONE-HILL

Gibwu zãr        levesar buɾĩt    doter-iveter.

Because before the villager formed the forager, the ice melted and made this river heard.

This was because of the roaring from the river from the ice melting, before the brat became a traveler.

BRAT    YAIS.DIST EXP.AT  TO.DIST GUEST RUS.REL TIME  AGAINST.DIST

Tʃihevã isã       lãnisuv gã      gibwu zir     dĩɾup lã

[[[[[ice penetrated/enveloped]-TOP soup/melt] from] [river-from]]-TOP roar]-TOP supports this

ICE         YAIS.DIST TOP.REL SOUP  RUS.DIST RIVER  RUS.DIST TOP.REL BEAST-SAY TOP.REL SUPP.C  RUS.1

heɾateɾeywu isã       zĩnir   zetwu zã       dãpehh zã       zĩnir   eɾisezar  zĩnir   hiwehh  zer

---
Godess Night Pelican  TOP.DIST ByThrow.DIST Stone-Hill   To.1&2 MOVE.Atemp TOP.default
zo-ãt  des   zosetãtĩ sãr      geper        doter-iveter gãnãt  lum        lwi

STAND LUS.default LUS.1&2 SUPP.Cont
ĩ     lus         zeɾãt   hiwehh

Godess TOP.REL STAND TOP.DIST EYE VIA.dist MOVE    TO.the village
zo-ãt  zĩnir   ĩ     sãr      dʒe ger      leverev gãnãt tenĩtwuɾuv.

Because Goddess Night Pelican flew, she stood on the mountain. Because she stood, the villagers saw her.

The bird spirit would fly into and stand itself upon the mountain, and the villagers would look upon the bird spirit.

---

doter-iveter mã zĩnir zo-ãt sãr hwan ger dʒe ger lum guv zo; lum sãr lãnetã isã lãkwu.

The women would look and hear the spirit bird in the mountain and transition their minds.

---

ĩ sãr Zo Okyaiti myu wut zo myu meɾĩt dyir.

Mrs. Okiaiti and the women stood over it.

Okiáíti and the women would be on it.

---

dup mã Zo Okyaiti zar

under dawn, Okiáíti would say

In the morning, Okiáíti would say

--

"Gibwu Zo De gãt! Mãhh biɾit dĩ ber zosetãtĩ zo-ãt gã zur zã gehwir"

"Ladies and gents! Your duty lets you say this word to the Pelican Goddess."

"You people! Say this word to the bird spirit!"
--

"Gibwu Zo De gãt! Mãhh biɾit luv zit evãt giɾit gehwir ra doter-iveter. Mãhh biɾit zosetãtĩ zo-ãt mwir dĩ ber lãnisuv zit"

"Ladies and gents! Your duty lets you walk upto the mountain and the word of the Pelican Goddess reach you."

"You people! Walk into the mountain and hear the word of the bird spirit!"

--

"zo-ãt zãr zo lus hiwehh. zo get levã gãnãt!"

"It has the woman and the woman gives it to us!"

--

Zo-ãt zãr zo lus hiweser.

Goddess TOP.DIST nurser AWAY-FROM.Default SUPP.remote.

Zo zãr zo-ãt ger leveɾev gãr.

Nurser TOP.DIST Goddess VIA, MOVE.Cont TO.1.

Kemi zĩnir lis biɾit zo-ãt giɾit levã gãt.

Use TOP.rel thing TOP.1&2 Goddess VIA.

This bird spirit had and gave this woman to me and it gave you want you want:

--

dutup myuzãr, zo zĩnir doter-iveter lã zĩnir lum zãr zo zã zo isã zo-ãt zã lãnisuv zã giɾwĩ.



In the future, a woman's walking to the mountain lets her become a goddess.

A woman will walk into the mountain and transition from human to bird spirit.

--

lwi zĩnir dar zur ber levã bur dar.

To call this wrong would be wrong.

Let her do so.
```


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/The Founding.md</code></p>

Good catch—you’re right. I pulled in elements from the war-generation. That muddies the baseline.

Let’s reset cleanly and pin **Late PSA (end of Generation 1, pre-war shock)** as it actually stands.

---

# **Myth of the Discovery of Sahumank (Late PSA — Corrected Snapshot)**

## **Core Narrative (5-Beat Structure)**

1. **Fall and Rejection (De-emphasized)**

* Black Albatross is cast down from the sky after conflict with the Sun.
* This event is no longer central; the Sun’s role is largely diminished in ritual life.

---

2. **Betrayal in the Empire of Snakes**

* Black Albatross seeks guest-right from the Empress.
* Insulted by **Viper and Boa**, she seduces the Empress, killing her, and steals the **Baton of Rulership**.

---

3. **The Poisoning of the Waters**

* Wounded and enraged, her blood spreads through the rivers and seas, making water **dangerous and transformative**.

---

4. **The War of the Sisters**

* Viper and Boa plunge the land into destructive conflict.
* Society collapses into war that consumes ordinary life.
* Auchir, raised among mortals, kills her commander and flees north instead of killing innoceents.

---

5. **Auchir and the Founding**

* Guided by vision, she finds the **bleeding Baton** in a lake and founds **Sahumank (the Promised Waters)**.
* Builds shrine to Bone-white Shark.

---

6. **Black Albatross**
* Black Albatross sleeps under (what is called in OTL) Lake Managua, pregant with a fire spirit.

## **Cosmology (Pre-War Form)**

### **Black Albatross (Core Figure)**

* Source of:

  * the wound
  * the poisoned waters
  * the Baton

* Increasingly central as Sun elements fade

---

### **Bone Shark (Water Power)**

* Associated with:

  * the lake
  * stability vs danger

* Key belief:

  > The waters of Sahumank are distinct from other waters

---

### **The Little Sister (Early Fire Concept)**

* Not yet a war goddess

* Understood as:

  * a **developing / unborn / emerging** force tied to the north

* Function:

  > consumes impurity (burning flawed things)

---

### **The Sun (Reduced / Displaced)**

* Formerly important
* Now:

  * ritually diminished
  * partially replaced by:

    * Black Albatross
    * Bone Shark

---

## **Major Structural Splits**

### **1. Shore vs River Traditions**

#### **Shore (Lake-Centered)**

* Lake = safe, contained, sacred
* Emphasis on:

  * stability
  * purification
  * boundary

---

#### **River / Movement-Oriented**

* Flowing water = transformative, dangerous
* Emphasis on:

  * change
  * exposure
  * movement

---

## **Institutional Structure (Key for Late PSA)**

### **Northern Shrine Requirement**

* Black Albatross is believed to reside (sleeping or forming) in the **northern lake**
* To rule:

  * elites must perform **labor in the north**

👉 This creates:

* a shared elite pathway
* dependency on northern ritual space

---

### **Ritual Economy**

* Shift from:

  * sacrifice (older Sun-linked forms)
* To:

  * labor at shrines
  * communal purification practices

---

## **Symbolic System (Clean at This Stage)**

* **Water:** danger + containment
* **Blood:** corruption + transformation
* **Fire:** purification of impurity (limited scope)

👉 Not yet militarized
👉 Not yet coercive

---

## **State of the System**

* Stable and internally coherent

* Structured around:

  * ritual labor
  * geographic legitimacy
  * controlled interpretation

* Tensions exist, but are:

  * **latent, not explosive**


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/Sahumãk Historical and Archaeological .md</code></p>

# Sahumãk Historical and Archaeological Framework (Current Summary)

## General Perspective

The project has shifted from constructing isolated myths and linguistic features toward constructing the corpus and historiography available to future archaeologists and philologists.

The primary insight is that modern understanding of Sahumãk is heavily shaped by preservation bias. The civilization was likely highly literate, but the overwhelming majority of texts were produced on perishable media, especially textiles and coated wooden surfaces.

As a result, scholars possess:

* numerous monumental inscriptions,
* large quantities of graffiti and labels,
* fragments of ritual and literary traditions,
* later manuscript copies,

while lacking most of the books and documents that originally connected these materials.

---

# Chronology

Dates are currently given relative to the death of Isamã (0 AID).

## PPSA / Orinoco Horizon

### ~4000 BID

* Aquaculture supplements hunting.
* Managed cultivation of aquatic resources develops.

### ~3500–3000 BID

* Domestication and management of ram-herds expands.
* Feed cultivation appears.
* Permanent settlements become possible.

### ~3000 BID

* First cities emerge.
* Linguistic and material-cultural commonality develops across a broad region.
* Political unity remains limited.

### ~2000 BID

* Southern cultural traditions expand northward into Panama.
* Textile symbolism and early ritual iconography spread.

---

## Late PSA / Tar-Bird Horizon

### ~400 BID to ~50 AID

Collapse of earlier multi-city systems in both the Orinoco region and southern Mesoamerica.

New symbolic systems emerge:

* Birds and snakes become active narrative figures rather than passive symbols.
* Panama Gulf traditions increasingly identify solar authority with serpents.
* Lake Sahumãk traditions depict conflict, wrestling, mating, and separation between birds and snakes.

This period also sees:

* textile motifs becoming ubiquitous,
* evidence for textile-writing traditions,
* no surviving readable textile texts,
* emergence of Tar-Bird Altars.

The pregnant Sun motif largely replaces older PSA solar imagery focused on light, rain, and lightning.

---

## Isamã Horizon

### 0 AID

Death and self-immolation of Isamã.

This event becomes the chronological anchor of later scholarship.

### ~0–120 AID

Monumental boom.

Previously localized shrine imagery spreads rapidly throughout the southern Lake Sahumãk region.

Competent Classical Sahumãk inscriptions appear suddenly on:

* stone,
* wood,
* shell,
* public monuments.

This is interpreted as a shift from pre-existing textile literacy into durable media rather than the invention of writing itself.

---

## Classical Sahumãk

### ~0–370 AID

Characteristics:

* widespread literacy,
* extensive use of writing,
* flourishing monumental tradition,
* shrine networks,
* flame succession system.

Most books remain lost because they were produced on textile media.

---

## Post-Classical Sahumãk

### ~370–800 AID

Monumentality declines.

Writing survives in:

* ritual contexts,
* scholarship,
* local inscriptions,
* graffiti.

Language drift increases.

Eventually:

* Classical Sahumãk ceases to be spoken,
* ritual copying survives,
* scribal reproduction outlasts comprehension.

---

## Mythic Period

### ~1500–2000 AID

Sahumãk is widely regarded as a mythical location.

Even communities living around the historical lake often fail to identify it with the legendary Sahumãk of literature and ritual tradition.

---

# Writing and Literacy

## Textile Origin Theory

Current reconstruction suggests:

woven symbolic traditions
→ mnemonic textile systems
→ readable textile writing
→ carved textile imitations
→ monumental glyph system

The earliest stone inscriptions resemble woven forms.

Many scholars believe inscriptions were read partly by touch, inherited from textile reading practices.

Evidence includes:

* unusual wear patterns,
* polished glyph surfaces,
* asymmetrical erosion.

---

## Preservation Pattern

High survival:

* monuments,
* shrine inscriptions,
* painted pottery,
* graffiti,
* curse stones,
* ownership marks.

Low survival:

* books,
* correspondence,
* archives,
* contracts,
* administrative records,
* educational materials.

This creates major distortions in modern understanding.

---

# The Isamã Cycle

The title is somewhat misleading.

The famous Isamã inscription preserves only the final portion of a larger mythological cycle.

The cycle itself contains:

1. Wounded Descent
2. False Priests of the Sun
3. Poisoning of the Waters
4. War of the Sisters
5. Auchir's Trial
6. Founding of Sahumãk
7. Rising of the Little Sister
8. Burning of the Shrine
9. Law of Fire and Water
10. Transformation into the Sun-Queen
11. First Passing of the Flame

The monument focuses primarily on events 8–11.

---

# Political Structure

## Before Isamã

Cities competed for legitimacy through shrine systems.

Authority flowed approximately:

Shrines
→ Kings
→ Cities
→ Hired Warriors

Kings resembled:

* Dark Age Greek basileis,
* lineage elders,
* heads of major houses,

rather than territorial monarchs.

Cities were coalitions of powerful houses.

---

## Houses

The true social unit is the House or Pack.

A typical house contains multiple life stages:

* elders,
* nursing adults,
* travelers,
* bearers,
* children.

Political authority originates primarily from houses rather than cities.

---

## Flame Succession

The major innovation of the Isamã settlement.

Authority can pass through:

* sacrifice,
* recognition,
* appointment,

rather than solely through descent.

The Flame line becomes a parallel legitimacy network crossing:

* houses,
* cities,
* shrine systems.

This does not abolish local government.

Instead it subordinates and links existing institutions.

---

# Interpretation of the Isamã Reform

## Traditional Interpretation

The Lamp Goddess revealed a new form of legitimate authority.

The Isamã succession system reflects divine truth.

---

## Materialist Interpretation

The reform was driven by changing social realities:

* expansion northward,
* pressure from Panama Gulf powers,
* increasing importance of mobile warriors,
* weakening ability of shrines and central cities to monopolize legitimacy.

The Flame system institutionalized networks that already existed among frontier war leaders.

---

# Religion

## Classical Sahumãk Attitude Toward Earlier Traditions

Older PSA and Orinoco imagery was not rejected.

Instead it was reinterpreted.

Classical theologians likely argued:

* old solar imagery referred imperfectly to the Pregnant Sun,
* serpent cults misunderstood deeper truths,
* earlier traditions possessed partial knowledge.

The distinction resembles the relationship between Olympians and Titans more than a simple replacement of one religion by another.

The old gods were viewed as primitive, incomplete, or uncivilized rather than entirely false.

---

# Archaeological Signature

Most common finds:

* household ceramics,
* paint flakes,
* resin coatings,
* sealants from wooden objects.

Bone middens are less common than expected because:

* bones were processed into broth,
* fed back into ram husbandry,
* ground into fertilizer.

The archaeology therefore preserves more traces of containers and coatings than of food waste.

This contributes to the impression that much of the civilization was built from materials that no longer survive.


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/SettingInfo.md</code></p>

# Feather Beasts, Color Vision, and Prestige Materials

## Overview

The world experienced a less severe extinction of New World fauna than OTL because the evolution of sapient species was more gradual and geographically widespread. As a result, many large animal lineages survived that disappeared in OTL.

Large flightless birds remained especially successful. Mammalian predators never developed true cat analogues, allowing bird lineages to occupy many large-animal niches for tens of millions of years.

---

# Pack and Fiber Birds

## Wild Ancestor

The principal domesticated transport animal of Mesoamerica and parts of western North America descends from a lineage of large herbivorous birds.

Characteristics:

* Capable of running but not true flight.
* Retain large functional wings.
* Wings are used for balance, display, climbing steep slopes, and slowing descents.
* Wild individuals inhabit broken terrain, cliffs, hills, and mountain environments.
* Large predators include terror-bird analogues and ambush-hunting mammals.

### Social Structure

Wild populations typically consist of:

* One adult territorial male.
* One to three adult females.
* Juvenile offspring.

Young males remain in the natal group longer than females.

After reaching adolescence:

* Females disperse into neighboring territories.
* Males are driven out and form bachelor groups.

Adult males eventually establish territories of their own.

### Territorial Displays

Males compete primarily through display rather than combat.

Typical display behaviors include:

* Wing spreading.
* Calls.
* Posturing.
* Patrols of territorial boundaries.
* Demonstrations of endurance and mobility.

Actual combat is uncommon because injuries are extremely costly in predator-rich environments.

Females prefer:

* Large territories.
* Bright plumage.
* Large display wings.
* Males capable of sustaining lengthy territorial displays.

Territorial contests therefore function as demonstrations of fitness rather than battles.

---

# Domestication

Domestication likely began through:

1. Collection of eggs and chicks.
2. Rearing of orphaned juveniles.
3. Management of bachelor males.
4. Gradual selection for reduced territoriality.

Humans primarily domesticated traits already present in the bachelor stage rather than those of fully mature territorial males.

Selected traits include:

* Increased sociality.
* Reduced aggression.
* Larger body size.
* Greater carrying capacity.
* Reduced ornamentation.
* Greater tolerance of human handling.

The result is an animal broadly analogous to llamas, mules, or pack reindeer rather than horses.

---

# Domestic Breeds

## Transport Breeds

Used throughout Mesoamerica and mountain regions.

Selected for:

* Endurance.
* Calm temperament.
* Route memory.
* Carrying capacity.

Often retain some wing-assisted balance behavior on steep trails.

## Fiber Breeds

Common in southern regions.

Selected for:

* Dense down production.
* Annual feather yields.
* High-quality ornamental feathers.

These animals occupy a niche partly analogous to sheep.

Products include:

* Down for insulation and textiles.
* Large ornamental display feathers.
* Ritual and prestige materials.

## Prestige Breeds

Maintained by elites.

Selected for:

* Exceptional plumage.
* Large display feathers.
* Rare feather patterns.
* Strong iridescence.

---

# Feather Economy

Display feathers are a major prestige commodity.

Advantages:

* Difficult to counterfeit.
* Require living breeding stock.
* Depend on biological structures rather than pigments.
* Often harvested during annual molts.

Iridescent feathers are especially prized because their appearance changes with viewing angle.

This dynamic visual effect is nearly impossible to reproduce through dyes, paint, or metalwork.

As a result, feather husbandry remains economically important even in complex state societies.

---

# Catgirl Color Vision

Catgirls are dichromats.

Their visual system contains two cone types:

* One biased toward shorter wavelengths.
* One biased toward longer wavelengths.

Neither cone is centered on the middle of the visible spectrum.

## Consequences

Humans distinguish:

* Red.
* Orange.
* Yellow.
* Green.
* Blue.
* Purple.

Catgirls instead perceive color along a much simpler axis:

* Short-biased colors.
* Long-biased colors.
* Intermediate/blended colors.

As a result:

* Blue and red appear highly distinct.
* Green, yellow, tan, grey, and purple occupy overlapping perceptual territory.
* Many human secondary colors collapse into broad intermediate categories.

Color perception is therefore organized more like a spectrum between two poles than a color wheel.

---

# Iridescence

Iridescence is culturally important because it crosses perceptual categories.

A feather may shift:

* From blue-dominant to red-dominant.
* From one visual pole to the other.

This makes iridescence especially prestigious and symbolically powerful.

The effect is perceived not merely as a color but as a transformation.

---

# Metal Symbolism

Before metallurgy:

* Native gold is known and valued.
* Native copper is known in some regions.
* Silver is much rarer because most silver exists in ores requiring smelting.

Gold is therefore often encountered before silver despite silver's geological abundance.

## Golden Empire

The Golden Empire tends to associate sacredness with permanence.

Gold is valued because:

* It remains bright.
* It resists corrosion.
* It changes little over time.

Its symbolic role aligns with concepts of continuity, order, and enduring authority.

## Sahumank

Sahumank religious traditions place greater value on maintained relationships and continual renewal.

As a result, sacred objects need not be permanent.

Materials requiring care may actually be preferred.

Examples include:

* Feather regalia.
* Textiles requiring repair.
* Polished silver ornaments.

The necessity of maintenance becomes part of the object's sacred significance.

A tarnishing silver vessel may be more ritually meaningful than a gold one because its condition visibly reflects ongoing devotion.

This mirrors broader Sahumank themes:

* Renewal.
* Obligation.
* Sustained relationships.
* The continual maintenance of social and sacred order.


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/LaterHistoriography.md</code></p>

# Later Historiography, Imperial Reinterpretation, and Wind Tribe Literary Culture

## The Problem of Historical Memory

A major conclusion of recent discussion is that the disappearance of historical understanding is not caused by a lack of sources.

Instead, it is caused by an overabundance of traditions, commentaries, reinterpretations, and political uses of older narratives.

By the late periods:

* the monuments still exist,
* the myths still exist,
* the shrines still exist,
* the lake still exists,
* portions of the script still survive,

but the realization that these all belong to the same historical tradition has largely disappeared.

Historical memory is obscured by accumulation rather than loss.

---

# Imperial Reinterpretation of Isamã

The Golden Empire does not erase Isamã.

Instead it absorbs her.

Imperial scholars generally know:

* Isamã fought southern imperial forces,
* Isamã was associated with major northern shrines,
* Isamã became connected with solar symbolism.

Rather than denying these facts, imperial theology reinterprets them.

The standard imperial position becomes:

* Isamã opposed corrupt rulers rather than the Sun itself.
* Isamã defended true solar principles when imperial officials failed to do so.
* Isamã's sacrifice revealed a partial understanding of truths later perfected by the Empire.

In this interpretation, Isamã becomes:

* a saint,
* a solar heroine,
* a local manifestation of wider imperial virtues.

The revolutionary and constitutional aspects of her actions become increasingly obscured.

---

# Isamã as a Branching Point

Different traditions eventually claim different versions of Isamã.

## Historical Isamã

* War leader.
* Architect of a specific political settlement.
* Founder of Flame succession.

## Sahumãk Isamã

* Defender of the northern shrines.
* Founder of the Flame line.
* Hero of local memory.

## Imperial Isamã

* Solar saint.
* Defender of civilized order.
* Forerunner of imperial values.

These traditions overlap but are not identical.

---

# Mythic Time and Historical Time

Later societies increasingly sort figures into narrative categories rather than chronological ones.

A common mental model develops:

Age of Gods
→ Age of Kings
→ Age of Empires

However archaeological reconstruction suggests that these systems often coexisted.

Examples include:

* forest shamans receiving visions,
* shrine federations,
* house-based city politics,
* imperial officers,
* military legitimacy networks,

all existing simultaneously.

The "ages" are later narrative categories rather than true historical periods.

---

# The Auchir Problem

Auchir becomes a particularly important example of this distortion.

Later audiences often assume:

* Auchir belongs to the remote age of origins,
* Auchir predates organized states,
* Auchir lived long before imperial institutions.

Archaeological reconstruction suggests something quite different.

Auchir may have lived only a few generations before the emergence of the first imperial administrative systems.

The figure feels ancient because:

* she occupies mythic narrative space,
* she speaks with gods,
* she participates in world-ordering events.

Her stories are categorized as foundational rather than historical.

---

# Imperial Treatment of Auchir

The Empire is generally comfortable with:

* Auchir the founder,
* Auchir the wanderer,
* Auchir the culture hero,
* Auchir the saint.

These reinforce imperial ideas of ordered civilization.

The Empire is less comfortable with:

* Auchir as a response to political dysfunction,
* Auchir as a reformer,
* Auchir as a precedent for challenging institutions.

Mythic founders are safe.

Historical founders are politically dangerous.

---

# Northern Federation ("Wind Tribes")

The northern highland and coastal peoples eventually develop a loose federation partly in response to expanding imperial influence.

Later traditions remember their founders as belonging to a distant heroic age.

Historically these founders may be surprisingly late.

Many may postdate:

* Classical Sahumãk,
* Isamã,
* major imperial institutions.

The result is another major chronological distortion in later historical memory.

---

# Wind Tribe Historiography

The Wind Tribes become notable for widespread literacy combined with weak canonization.

Unlike either the Empire or Sahumãk shrine traditions, there is no overwhelming pressure toward a single authoritative version of events.

A scholar is often expected to preserve multiple traditions.

A respected scholar comments on them.

A great scholar creates new works that place them in dialogue.

Contradiction is often treated as intellectually productive rather than problematic.

---

# Narrative as Conversation

Wind Tribe literature treats stories less as records and more as participants in ongoing conversations.

The highest literary achievement is not necessarily:

* preserving a story,
* proving a story true,
* establishing orthodoxy.

Instead it is often:

* placing stories into dialogue,
* contrasting versions,
* revealing hidden relationships,
* generating new interpretations.

Texts may deliberately reference multiple traditions simultaneously.

Meaning emerges through comparison and contrast.

---

# Attitude Toward Historical Accuracy

A characteristic Wind Tribe response to historical criticism might be:

"But that is not what actually happened."

Answer:

"That is not the question being asked."

This does not mean history is ignored.

Rather, narrative serves functions beyond historical reporting.

Stories are used to:

* think,
* compare,
* interpret,
* argue,
* explore possibilities.

Historical accuracy is only one possible value among many.

---

# Performance Traditions

The three major traditions develop different relationships between narrative and performance.

## Imperial Tradition

Purpose:

* reinforce legitimacy,
* renew social order,
* teach moral meaning.

Comparable in social role to:

* civic ritual,
* coronations,
* morality plays.

The audience generally knows the conclusion beforehand.

---

## Sahumãk Tradition

Purpose:

* make sacred events present,
* connect participants to ritual continuity.

Dance, prayer, celebration, and story are often inseparable.

The performance is itself a sacred act.

---

## Wind Tribe Tradition

Purpose:

* explore ideas through narrative,
* compare traditions,
* generate interpretations.

Performance functions as an intellectual medium.

The audience is expected to recognize references, contrasts, and alternative versions.

---

# Relationships Between Traditions

The three traditions are not opposites.

Each shares important features with the others.

## Empire ↔ Sahumãk

Both preserve canon.

Both resist casual alteration of foundational narratives.

Difference:

* Empire protects legitimacy.
* Sahumãk protects continuity.

---

## Empire ↔ Wind Tribes

Both are deeply interested in interpretation.

Difference:

* Empire seeks conclusions.
* Wind Tribes seek conversations.

---

## Sahumãk ↔ Wind Tribes

Both value ambiguity and narrative tension.

Difference:

* Sahumãk mystery is sacred.
* Wind Tribe mystery is intellectual.

---

# Historical Sources

Modern historians increasingly realize:

The Empire preserves what institutions wanted remembered.

The Wind Tribes preserve what people argued about.

The Sahumãk traditions preserve what people continued to do.

None are wholly reliable.

All are indispensable.

Historical reconstruction depends on comparing all three traditions simultaneously.


<div class="pagebreak"></div>

<p class="source-note">Source: <code>Sahumãk/Scribal Comprehension.md</code></p>

## The Question of Scribal Comprehension in Post-Classical Copies

Many modern students are unaware of how recently Sahumãk came to be understood as both a historical language and a geographic-cultural tradition, rather than merely a place-name preserved in mythological, esoteric, and ritual literature. Earlier scholarship frequently treated references to Sahumãk as entirely legendary, while later writers often erred in the opposite direction, projecting the contents of much later ritual texts directly onto periods that preceded them by centuries or even millennia.

Nevertheless, there is little doubt that many post-Classical chants, narratives, and ritual manuals ultimately derive from genuine Sahumãk sources. The Isamã Cycle, in particular, is repeatedly quoted, referenced, paraphrased, and occasionally condemned throughout the later literature. Such references provide valuable evidence for the continued prestige of Sahumãk texts long after the decline of the language itself. At the same time, they also reveal the limited extent of scribal comprehension. Numerous manuscripts contain misplaced quotations, internally contradictory translations, or passages that appear to have been selected solely for their perceived ritual or rhetorical value rather than their semantic content. In some cases, authors seem to have copied visually similar passages while remaining unaware that they had substituted entirely different sections of a text.

The largest surviving ritual compilations present an even more striking picture. These works typically provide detailed instructions concerning the recitation, sequencing, and ceremonial use of Sahumãk passages, yet rarely attempt sustained translation or linguistic analysis. The glyphs are treated not as the representation of a language with grammar and meaning, but as authoritative ritual formulae whose power derives from correct reproduction and performance. For many post-Classical scribes, Sahumãk appears to have occupied a position analogous to that of a sacred liturgical language: something to be copied, recited, and interpreted symbolically, but only rarely understood in a philological sense.


<div class="notes-page">

## Field Notes 1

</div>

<div class="notes-page">

## Field Notes 2

</div>

<div class="notes-page">

## Field Notes 3

</div>
