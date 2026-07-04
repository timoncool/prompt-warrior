<div align="center">

<img src="assets/logo.svg" alt="Эмблема Prompt Warrior" width="112">

# Prompt Warrior

**Преврати логи Claude Code в геймифицированный аналитический портрет своей работы с ИИ.**

[![License](https://img.shields.io/github/license/timoncool/prompt-warrior?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/timoncool/prompt-warrior?style=flat-square)](https://github.com/timoncool/prompt-warrior/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/timoncool/prompt-warrior?style=flat-square)](https://github.com/timoncool/prompt-warrior/commits)
[![Python](https://img.shields.io/badge/python-3.8%2B%20stdlib--only-3776AB?style=flat-square)](scripts/analyze.py)

**[English](README.md)** · **[Русский](README_RU.md)**

![Карточка Prompt Warrior](docs/screenshots/hero.png)

</div>

Prompt Warrior — скилл для Claude Code, который анализирует локальные логи сессий и
показывает, как вы на самом деле общаетесь с ИИ: реальные цифры по фиксированной шкале,
сравнимой между людьми. На выходе — карточка со статистикой, прикольный титул, ачивки
с редкостью и советы по промпт-инженерингу с опорой на исследования. Работает полностью
локально на stdlib Python — наружу не уходит ничего.

## Возможности

- **Фиксированная шкала (SCALE v1)** — формулы и пороги заморожены, все измеряются одинаково, профили сравнимы
- **Настоящая аналитика** — объём реплик, топ императивов, маркеры тона, активность по часам, сильное и слабое строго из ваших цифр
- **Прикольные статусы** — титул из поведения (эпитет + звание + уровень), 74 ачивки от common до legendary, шесть шкал (Ярость, Теплота, Дотошность, Совиность, Нетерпеливость, Кэш-скряга)
- **Глубокие сигналы** — прерывания, точка кипения сессий, индекс оборотня (ночной мат против дневного), фирменный словарь, дабл-тексты, «нет»-открытия, RU/EN код-свитчинг, микс типов вопросов
- **Экономика и арсенал** — токены (с дедупом как в ccusage) и кэш-эффективность, профиль инструментов (оператор / хирург / археолог), модели, проекты, PR, топ MCP-серверов, расширения файлов, армии субагентов, самые дорогие сессии
- **Советы с пруфами** — каждая рекомендация ссылается на проверенный источник; опровергнутые клеймы тоже перечислены ([sources.md](references/sources.md))
- **Любой период** — по умолчанию всё время; неделя, месяц, точные даты — ваш выбор
- **100% локально и приватно** — только stdlib Python, ноль зависимостей, без ключей и сетевых вызовов
- **RU / EN** — лексиконы и вывод на обоих языках

## Быстрый старт

1. **Клонировать**
   ```powershell
   git clone https://github.com/timoncool/prompt-warrior "$env:USERPROFILE\.claude\skills\prompt-warrior"
   ```
   Linux/macOS:
   ```bash
   git clone https://github.com/timoncool/prompt-warrior ~/.claude/skills/prompt-warrior
   ```

2. **Попросить Claude Code**
   ```
   /prompt-warrior
   ```
   или просто: *«построй мой промпт-профиль»*.

3. **Получить карточку** — инлайн-виджет плюс автономный `ai-profile.html`, который
   можно открыть, заскринить и зашарить.

## Использование

- *«построй мой промпт-профиль»* — за всё время
- *«профиль за последнюю неделю»* — последние 7 дней
- *«профиль за июнь»* — точный диапазон дат
- Период — всегда ваш выбор; скилл никогда не решает за вас молча.

Под капотом: `scripts/analyze.py` читает JSONL-логи из `~/.claude/projects` (только
чтение), дедуплицирует ваши реплики, считает метрики и пишет `profile.json`; Claude
собирает карточку по шаблону из [references/widget.md](references/widget.md).

## Документация

- [SCALE v1 — замороженные формулы](references/scale.md)
- [Звания, эпитеты, ачивки](references/rpg.md)
- [Рекомендации по триггерам метрик](references/recommendations.md)
- [База источников с вердиктами проверки](references/sources.md)

## Другие проекты [@timoncool](https://github.com/timoncool)

| Проект | Описание |
|--------|----------|
| [telegram-api-mcp](https://github.com/timoncool/telegram-api-mcp) | Telegram Bot API как MCP-сервер |
| [civitai-mcp-ultimate](https://github.com/timoncool/civitai-mcp-ultimate) | Civitai API как MCP-сервер |
| [trail-spec](https://github.com/timoncool/trail-spec) | TRAIL — протокол трекинга контента |
| [GitLife](https://github.com/timoncool/gitlife) | Жизнь в неделях — интерактивный календарь |
| [ACE-Step Studio](https://github.com/timoncool/ACE-Step-Studio) | AI-студия музыки — песни, вокал, каверы, клипы |
| [VideoSOS](https://github.com/timoncool/videosos) | AI-видеопродакшн в браузере |

## Авторы

- **Nerual Dreming** — [Telegram](https://t.me/nerual_dreming) | [neuro-cartel.com](https://neuro-cartel.com) | [ArtGeneration.me](https://artgeneration.me)

## Поддержать автора

Я создаю опенсорс софт и занимаюсь исследованиями в области ИИ. Большая часть всего, что я делаю, находится в открытом доступе. Ваши пожертвования позволяют мне создавать и исследовать больше, не отвлекаясь на поиск еды для продолжения существования =)

**[Все способы поддержки](https://github.com/timoncool/ACE-Step-Studio/blob/master/DONATE.md)** | **[dalink.to/nerual_dreming](https://dalink.to/nerual_dreming)** | **[boosty.to/neuro_art](https://boosty.to/neuro_art)**

- **BTC:** `1E7dHL22RpyhJGVpcvKdbyZgksSYkYeEBC`
- **ETH (ERC20):** `0xb5db65adf478983186d4897ba92fe2c25c594a0c`
- **USDT (TRC20):** `TQST9Lp2TjK6FiVkn4fwfGUee7NmkxEE7C`

## Star History

<a href="https://www.star-history.com/?repos=timoncool%2Fprompt-warrior&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=timoncool/prompt-warrior&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=timoncool/prompt-warrior&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=timoncool/prompt-warrior&type=date&legend=top-left" />
 </picture>
</a>

## Лицензия

[MIT](LICENSE)
