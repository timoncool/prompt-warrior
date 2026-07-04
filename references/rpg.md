# Fun statuses — ranks, epithets, achievements

Геймификация без RPG-цирка: никаких классов и стат-листов. Прикольный титул, уровень,
ачивки с редкостью — приправа к аналитике. Все условия зафиксированы в
`scripts/analyze.py` (SCALE v1); тут — справочник для рендера и нарратива.

## Title

`{Эпитет} {Звание} {N} уровня[, {суффикс топ-ачивки}]`
`{Epithet} {Rank}, level {N}[, {top achievement suffix}]`

Суффикс добавляется только если самая редкая ачивка — epic или legendary.
Пример: «Неистовый Командир Терминала 89 уровня, Железная Длань».

## Rank — звание по доминирующему поведению

Выбирается по наибольшему внутреннему поведенческому индексу (см. scale.md);
tie-break по порядку строк:

| Индекс | RU | EN |
|--------|----|----|
| command (директивность) | Командир Терминала | Terminal Commander |
| tempo (темп правок) | Мастер Молниеносных Правок | Master of Lightning Edits |
| endurance (марафоны) | Марафонец Сессий | Session Marathoner |
| context (спеки) | Архитектор Спек | Spec Architect |
| verification (проверки) | Верховный Ревизор | High Auditor |
| diplomacy (вежливость) | Дипломат Машин | Machine Diplomat |

## Epithet (первое сработавшее условие)

| Condition | RU | EN |
|-----------|----|----|
| RAGE ≥ 70 | Неистовый | Furious |
| night share ≥ 30% | Полуночный | Midnight |
| verify ≥ 10% | Недоверчивый | Skeptical |
| politeness ≥ 3% | Учтивый | Courteous |
| median words ≥ 25 | Обстоятельный | Thorough |
| profanity ≥ 30/1000 | Сквернословящий | Foul-mouthed |
| default | Странствующий | Wandering |

## Achievements (24, редкость по паттерну bronze/silver/gold + legendary)

| ID | RU | EN | Rarity | Condition |
|----|----|----|--------|-----------|
| sprinter | Спринтер | Sprinter | common | median voice message ≤ 8 words |
| hundred_club | Клуб ста | Hundred Club | common | ≥ 100 messages |
| interrogator | Дознаватель | Interrogator | common | questions ≥ 30% |
| epic_wall | Стена текста | Wall of Text | common | avg words/message ≥ 30 |
| novelist | Романист | Novelist | rare | ≥ 3% messages of 200+ words |
| trust_verify | Доверяй, но проверяй | Trust but Verify | rare | verify ≥ 10% |
| capslock | Капслок-гладиатор | Capslock Gladiator | rare | CAPS ≥ 20% |
| night_watch | Ночной дозор | Night's Watch | rare | night share ≥ 30% |
| surgeon | Хирург | Surgeon | rare | self-correction ≥ 4% |
| librarian | Библиотекарь | Librarian | rare | memory/rules ≥ 3% |
| sisyphus | Сизиф | Sisyphus | rare | self-corr + categorical ≥ 8% |
| why_child | Почемучка | The Why Child | rare | why ≥ 8% |
| daily_grind | Ежедневный гринд | Daily Grind | rare | ≥ 75% active days over ≥ 14-day span |
| thousand_voices | Тысяча голосов | Thousand Voices | rare | ≥ 1000 messages |
| polyglot | Полиглот | Polyglot | rare | voice language mix 25–75% RU |
| categorical_imperative | Категорический императив | Categorical Imperative | rare | categorical ≥ 8% |
| gentle_soul | Добрая душа | Gentle Soul | rare | praise ≥ 5% |
| marathon | Марафонец | Marathoner | epic | a session with ≥ 300 messages |
| eruption | Извержение | Eruption | epic | profanity ≥ 40/1000 words |
| agent_bane | Гроза агентов | Bane of Agents | epic | insults ≥ 20% |
| zen | Дзен | Zen | epic | RAGE ≤ 5 with ≥ 300 messages |
| tyrant | Тиран | Tyrant | legendary | negativity : praise ≥ 10:1 |
| saint | Святой | Saint | legendary | politeness ≥ 5% and profanity < 1/1000 |
| volcano_heart | Сердце вулкана | Volcano Heart | legendary | RAGE ≥ 85 |

Нарратив: сначала legendary/epic, в конце 1-2 самых смешных common. Не стыдить —
ачивки это флейвор, включая «Тирана» (см. recommendations.md про влияние тона).
