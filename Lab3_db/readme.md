Лабораторна робота No3.
Виконав: Володимир Пюрко ІР23.

Проєктування та реалізація реляційної бази даних для предметної області агентства свят та аніматорів у MySQL.


Структура бази даних
Довідники та основні сутності city, agency, animator/, skill, client, holiday_type
Події та зв'язки (M:N): event animator_skill agency_animator event_animator
Цілісність та індексація:первинні й зовнішні ключі FOREIGN KEY, каскадне видалення у зв'язкових таблицях ON DELETE CASCADE та індекси idx_event_date і idx_client_phone