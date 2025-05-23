# Простая игра: Боец против монстра

## Описание

Данный проект демонстрирует применение принципа открытости/закрытости (Open/Closed Principle, OCP) из SOLID-принципов в объектно-ориентированном программировании на Python.  
В игре реализованы классы бойца, монстра и различных видов оружия. Боец может менять оружие и атаковать монстра, а у каждого оружия свой урон (`damage`). Монстр имеет очки жизни (`hit_points`), которые уменьшаются при атаке.

## Как добавить новое оружие

Чтобы добавить новый тип оружия, создайте новый класс, наследующийся от абстрактного класса `Weapon`, и реализуйте необходимые методы и свойства. При этом не требуется изменять существующий код бойца или монстра.

## Запуск

1. Установите Python 3.x.
2. Запустите файл `main.py`:
   ```
   python main.py
   ```

## Структура

- `main.py` — основной код игры.
- `.gitignore` — исключения для git.
- `README.md` — описание проекта.

## Пример работы

```
Оружие изменено на Меч
Атакую мечом!
Монстр получил 25 урона! Осталось жизней: 75
Оружие изменено на Лук
Атакую луком!
Монстр получил 15 урона! Осталось жизней: 60
Оружие изменено на Копье
Атакую копьем!
Монстр получил 20 урона! Осталось жизней: 40
```

