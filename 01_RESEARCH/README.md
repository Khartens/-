# 01_RESEARCH — исследования

Начинается **после** первого блока discovery-интервью (этап 4). Здесь — только проверяемые данные и их интерпретация.

## Содержание

| Путь | Что | Статус |
|---|---|---|
| [`site-audit-2026-10-02.md`](site-audit-2026-10-02.md) | Аудит сайта: тексты, CTA, формы, тарифы, аналитика, SEO, «заявлено ↔ реализовано» | ✅ v1 |
| [`market.md`](market.md) | Рынок: 5 подрынков, факты, тренды, динамика маркетплейса | ✅ v1 |
| [`demand-and-seasonality.md`](demand-and-seasonality.md) | Спрос, сезонность по категориям, регионы | ✅ v1 (частотность Wordstat — UNKNOWN) |
| [`competitors/`](competitors/) | Файл на каждого конкурента + [`competitor-matrix.md`](competitors/competitor-matrix.md) | ✅ v1 |
| [`audience/`](audience/) | Сегменты SUPPLY и DEMAND, customer profiles | ✅ v1 (гипотезы до custdev) |
| `reviews-voc.md` | Голос клиента: отзывы о конкурентах | ⚪ нужен доступ к сайтам отзывов |
| `interviews/` | Записи интервью с владельцами и арендаторами (без персональных данных) | ⚪ после первых интервью |

## Стандарт источников (обязателен)

Каждый важный факт оформляется так:

| Source | URL | Date accessed | Claim | Confidence |
|---|---|---|---|---|
| Название источника | ссылка | ГГГГ-ММ-ДД | Что именно утверждается | High / Medium / Low |

Внутри документа разделяем блоки: **FACT** → **INTERPRETATION** → **HYPOTHESIS** → **RECOMMENDATION**.
Все использованные источники дублируются в [`../00_FOUNDATION/sources.md`](../00_FOUNDATION/sources.md).
