# CRM: поля, стадии, KPI

**Дата:** 2026-10-02
**Где вести:** закрытый инструмент (Google-таблица с ограниченным доступом, amoCRM, Битрикс24, Notion). **Не в этом репозитории**: персональные данные сюда не попадают (см. [`README.md`](README.md)).

## 1. Поля карточки лида

| Поле | Тип | Пример | Обязательно |
|---|---|---|---|
| `lead_id` | ID | L-0001 | ✅ |
| `segment` | список | spec_owner / spec_company / rental / taxi_fleet / multi_car / single_car / company_renter / partner | ✅ |
| `city` | текст | [город] | ✅ |
| `category` | список | экскаватор-погрузчик / манипулятор / Газель / … | ✅ |
| `units` | число | 3 | ✅ |
| `org_name` | текст | ИП или компания (если публично) | — |
| `contact_name` | текст | только имя | ✅ |
| `contact_channel` | список | phone / telegram / whatsapp / email / visit | ✅ |
| `contact_value` | текст | рабочий телефон или ник | ✅ |
| `source` | список | 2gis / yandex_maps / site / visit / inbound_content / inbound_chat / referral / partner | ✅ |
| `consent` | да/нет + дата | согласие на дальнейшие сообщения | ✅ |
| `do_not_contact` | да/нет | — | ✅ |
| `status` | список | new / contacted / conversation / agreed / listing_published / active / paying / lost / do_not_contact | ✅ |
| `qualification_score` | 0–10 | 8 | ✅ |
| `pain` | текст | «простой 10 дней, диспетчер 15%» | — |
| `objection` | список | no_demand / has_avito / no_time / price / trust / other | — |
| `lost_reason` | список | no_response / not_interested / wrong_fit / later | — |
| `listing_urls` | ссылки | mashinarf.ru/car-ad?slug=… | — |
| `telegram_bot_connected` | да/нет | — | — |
| `founder_program` | да/нет + дата окончания | «Плюс» бесплатно до ГГГГ-ММ-ДД (выдаётся помесячно) | — |
| `first_contact_at` / `last_contact_at` / `next_step_at` | даты | — | ✅ |
| `next_step` | текст | «напомнить про фото» | ✅ |
| `touches` | число | 2 (не больше 3 без ответа) | ✅ |
| `owner` | текст | кто ведёт лид | ✅ |

## 2. Стадии и правила перехода

| Стадия | Вход | Выход | SLA |
|---|---|---|---|
| new | Добавлен в список | Первый контакт | ≤3 дня |
| contacted | Звонок или сообщение | Ответ | — |
| conversation | Состоялся разговор | Согласие или отказ | — |
| agreed | Согласие разместиться | Опубликовано | ≤2 дня |
| listing_published | Объявление в каталоге | Отклик или контакт в течение 14 дней | — |
| active | Активность за 14 дней | — | Ежемесячная проверка |
| paying | Оплатил тариф | — | — |
| lost / do_not_contact | Отказ, нет ответа или запрет | — | Не трогать (lost — через сезон) |

## 3. KPI воронки (еженедельно)

| KPI | Формула | Цель (HYPOTHESIS) |
|---|---|---|
| Новых контактов | count(contacted за неделю) | 75 (≈300 за 4 недели) |
| Contact rate | conversation / contacted | ≥60% |
| Agree rate | agreed / conversation | ≥50% |
| Publish rate | listing_published / agreed | ≥80% |
| Activation | active / listing_published (14 дней) | ≥50% |
| Paid conversion (после бесплатного периода) | paying / founder_program ended | ≥20% |
| Время на лид | часов / listing_published | ≤0,25 ч |
| do_not_contact rate | do_not_contact / contacted | следить: если >10% — пересмотреть подход |
