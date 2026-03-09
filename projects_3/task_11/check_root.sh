#!/bin/bash

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "ОШИБКА: Скрипт должен запускаться от имени root (суперпользователя)."
        echo "Текущий UID: $EUID"
        echo "Запустите с sudo: sudo ./check_root.sh"
        exit 1
    fi
    echo "Проверка пройдена: скрипт запущен от root (UID=$EUID)"
}

check_root

echo "Скрипт успешно выполняется с правами root..."
done

