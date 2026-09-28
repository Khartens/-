# 08_CRM — жизненный цикл пользователя

Этап 15. Отдельно для владельцев (supply) и арендаторов (demand).

Lifecycle: **VISITOR → REGISTRATION → ACTIVATION → LISTING / REQUEST → FIRST TRANSACTION → REPEAT → REFERRAL**

| Файл (планируется) | Что |
|---|---|
| `lifecycle-map.md` | Этапы, триггеры переходов, метрики каждого шага |
| `flows-email.md` / `flows-telegram.md` / `flows-push.md` | Онбординг, брошенные действия, реактивация — только по каналам, которые реально есть в продукте |
| `referral.md` | Реферальная механика |

Перед проектированием проверяется, какие каналы коммуникации реально реализованы в продукте (см. `00_FOUNDATION/project-brief.md`).
